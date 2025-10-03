# Production Planning AI with LangChain + OpenAI

This project builds an agentic framework for automating production planning using LangChain and OpenAI. It includes modular agents for planning, optimization, data ingestion, and reporting.

## Features
- Excel ingestion and ERP integration
- Demand forecasting and constraint solving
- Agentic reasoning and plan generation
- KPI reporting and simulation

## Getting Started
1. Clone the repo
2. Copy `.env.example` to `.env` and add your OpenAI key
3. Install dependencies: `pip install -r requirements.txt`
4. Run `main.py` to launch the agentic planner

## Agents
- PlannerAgent: Breaks down goals into subtasks
- OptimizerAgent: Applies heuristics and solvers
- IngestionAgent: Parses Excel/API inputs
- ReportingAgent: Summarizes KPIs and exceptions
- MemoryAgent: Stores historical decisions

## Roadmap
- [ ] Add Streamlit dashboard
- [ ] Integrate OR-Tools for constraint solving
- [ ] Add multi-site planning support
