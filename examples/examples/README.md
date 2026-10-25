# Examples

Agent-framework snippets that call the Dutiful MCP server at `https://dutiful.work/mcp`.

- `langchain_agent.py` - LangChain + langgraph, via `langchain-mcp-adapters`
- `crewai_agent.py` - CrewAI, via `crewai_tools.MCPServerAdapter`

Tools: `check_coverage` (free), `create_order` and `get_report` (x402-paid, $3 USDC on Base).
Paid tools need a wallet-enabled x402 client. Machine-readable details: https://dutiful.work/llms.txt
