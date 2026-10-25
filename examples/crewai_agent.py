"""Use the Dutiful MCP server from a CrewAI crew.

Install:  pip install "crewai[mcp]"
Docs:     https://github.com/dutiful-hq/dutiful-mcp
Endpoint: https://dutiful.work/mcp (streamable HTTP MCP, x402 paid tools)
"""
from crewai import Agent, Crew, Task
from crewai_tools import MCPServerAdapter

server_params = {
    "url": "https://dutiful.work/mcp",
    "transport": "streamable-http",
}

with MCPServerAdapter(server_params) as tools:
    # Tools exposed: check_coverage, create_order, get_report.
    # create_order/get_report are x402-paid ($3 USDC on Base) - call them
    # from a wallet-enabled client; see https://dutiful.work/llms.txt.
    researcher = Agent(
        role="Vendor researcher",
        goal="Check companies against official registries and sanctions lists",
        backstory="You verify counterparties before any payment is approved.",
        tools=tools,
    )
    task = Task(
        description="Check registry coverage for the vendor 'Nestle'.",
        expected_output="Coverage summary listing the registries that apply.",
        agent=researcher,
    )
    Crew(agents=[researcher], tasks=[task]).kickoff()
