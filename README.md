# Deep Research AI Agentic System

This is a multi-agent research assistant that:
- Uses Tavily to collect fresh data from the web.
- Uses LangChain and LangGraph to organize dual-agent workflows.
- Drafts final answers using DeepSeek R1 Distill LLaMA 70B.
- Has an interactive Streamlit UI.

## Features

- Real-time information gathering using Tavily search
- Multi-agent architecture: Research + Answer Drafting + Summarization
- Built using LangChain + LangGraph
- Interactive UI using Streamlit

## Installation

1. Clone this repo

```bash
git clone https://github.com/yourusername/deep-research-ai.git
cd deep-research-ai
```

2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Add your API keys in a `.env` file  

   You'll need your own keys from [Groq](https://console.groq.com/keys) and [Tavily](https://app.tavily.com/home) which are free-tier accessible.  

```bash
TAVILY_API_KEY=tavily-api-key
GROQ_API_KEY=groq-api-key
```

## Running the App

```bash
streamlit run main.py
```

## Tech Stack

- LangChain
- LangGraph
- Tavily
- Streamlit
- Groq API

## How It Works

1. User enters a question
2. ResearchAgent queries Tavily and collects information
3. AnswerAgent drafts a coherent response using DeepSeek R1
4. SummaryAgent summarizes the answer received from AnswerAgent
5. Final answer is displayed on the Streamlit interface along with the thinking process