# src/agents/planner_agent.py

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(temperature=0.3, openai_api_key=openai_api_key)

# Import tools (mocked for now)
from src.tools.excel_parser import parse_excel
from src.chains.forecasting_chain import run_forecast

# Define tools for the planner agent
tools = [
    Tool(
        name="ExcelParser",
        func=parse_excel,
        description="Parses production input sheets and returns structured data"
    ),
    Tool(
        name="Forecaster",
        func=run_forecast,
        description="Forecasts demand based on historical production data"
    ),
]

# Initialize the agent
planner_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Optional wrapper for external calls
def run(goal: str):
    return planner_agent.run(goal)
