"""Use the Dutiful MCP server from a LangChain agent.

Install:  pip install langchain-mcp-adapters langchain
Docs:     https://github.com/dutiful-hq/dutiful-mcp
Endpoint: https://dutiful.work/mcp (streamable HTTP MCP, x402 paid tools)
"""
import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "dutiful": {
                "transport": "http",
                "url": "https://dutiful.work/mcp",
            }
        }
    )
    tools = await client.get_tools()
    # Tools exposed: check_coverage, create_order, get_report.
    # create_order/get_report are x402-paid ($3 USDC on Base) - call them
    # from a wallet-enabled client; see https://dutiful.work/llms.txt.
    agent = create_agent(
        model="anthropic:claude-sonnet-4-5",  # any model your LangChain install supports
        tools=tools,
    )
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Check which registries cover Nestle."}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
