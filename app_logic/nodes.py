import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from .utils import split_thoughts

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY") 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

search_tool = TavilySearchResults(api_key=TAVILY_API_KEY, max_results=5)
llm = ChatGroq(api_key=GROQ_API_KEY, model="deepseek-r1-distill-llama-70b")

#ResearcherAgent
def research_node(state):
    query = state["query"]
    context = search_tool.run(query)
    return {"query": query, "context": context}

#AnswerAgent
def answer_node(state):
    prompt = HumanMessage(
        content=f"Use the following research context to answer the question:\n\nContext:\n{state['context']}\n\nQuestion:\n{state['query']}"
    )
    response = llm.invoke([prompt])
    thinking, answer = split_thoughts(response.content)
    return {**state, "answer": answer, "thinking": thinking}

#SummaryAgent
def summarizer_node(state):
    prompt = HumanMessage(
        content=f"Please summarize the following answer in 20 words:\n\n{state['answer']}"
    )
    response = llm.invoke([prompt])
    _, summary = split_thoughts(response.content)
    return {**state, "summary": summary}
