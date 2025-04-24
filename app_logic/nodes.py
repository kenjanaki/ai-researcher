import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from .utils import split_thoughts

env_file_path = ".env"
if os.path.exists(env_file_path):
    load_dotenv(env_file_path)

def init_agents(tavily_key=None, groq_key=None):
    if not tavily_key:
        tavily_key = os.getenv("TAVILY_API_KEY")
    if not groq_key:
        groq_key = os.getenv("GROQ_API_KEY")

    if not tavily_key or not groq_key:
        return None, None, None

    os.environ["TAVILY_API_KEY"] = tavily_key
    os.environ["GROQ_API_KEY"] = groq_key

    tavily_wrapper = TavilySearchAPIWrapper()
    search_tool = TavilySearchResults(api_wrapper=tavily_wrapper)
    llm = ChatGroq(api_key=groq_key, model="deepseek-r1-distill-llama-70b")

    def research_node(state):
        query = state["query"]
        context = search_tool.run(query)
        return {"query": query, "context": context}

    def answer_node(state):
        prompt = HumanMessage(
            content=f"Use the following research context to answer the question:\n\nContext:\n{state['context']}\n\nQuestion:\n{state['query']}"
        )
        response = llm.invoke([prompt])
        thinking, answer = split_thoughts(response.content)
        return {**state, "answer": answer, "thinking": thinking}

    def summarizer_node(state):
        prompt = HumanMessage(
            content=f"Please summarize the following answer in 20 words:\n\n{state['answer']}"
        )
        response = llm.invoke([prompt])
        _, summary = split_thoughts(response.content)
        return {**state, "summary": summary}

    return research_node, answer_node, summarizer_node