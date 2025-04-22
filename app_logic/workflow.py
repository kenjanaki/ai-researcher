from langgraph.graph import StateGraph, END
from .nodes import research_node, answer_node, summarizer_node

def run_research(query, add_summary):
    graph = StateGraph(dict)
    graph.add_node("ResearchAgent", research_node)
    graph.add_node("AnswerAgent", answer_node)
    if add_summary:
        graph.add_node("SummarizerAgent", summarizer_node)

    graph.set_entry_point("ResearchAgent")
    graph.add_edge("ResearchAgent", "AnswerAgent")
    if add_summary:
        graph.add_edge("AnswerAgent", "SummarizerAgent")
        graph.add_edge("SummarizerAgent", END)
    else:
        graph.add_edge("AnswerAgent", END)

    app = graph.compile()
    return app.invoke({"query": query})
