# Dutiful - Company background reports for agents

Research you can cite. Dutiful generates company background reports from official public data - registry profile, officers and owners where published, and a sanctions screen against the OFAC SDN and UK Sanctions List plus a news and web scan, with every finding cited to its source. Reports cost $3 in USDC on Base, paid over the x402 protocol: one wallet signature, no account.

## For agents (MCP)

Streamable HTTP MCP server: `https://dutiful.work/mcp`

Tools:

- `check_coverage` - check whether a company is in a covered registry (free)
- `create_order` - create a report order and get x402 payment requirements
- `get_report` - fetch the finished report

Server card: `https://dutiful.work/.well-known/mcp/server-card.json`

## For agents (HTTP + x402)

- `POST /api/order` `{company, country}` -> JSON candidates (free)
- `POST /api/order/{order}/entity` `{idx}` -> 402 with x402 v2 payment requirements
- `POST /api/order/{order}/pay` with `PAYMENT-SIGNATURE` header -> paid report
- `GET /api/order/{order}` -> status and report

Discovery: `/.well-known/x402.json` and `/openapi.json`.

## Coverage and limits

12 registries. US coverage is SEC-reporting companies; Canada is federal corporations. The screen covers the OFAC SDN and UK Sanctions List plus a news and web scan; EU and UN lists are not screened. A report is not a credit check or a legal opinion.

## See a real report

- https://dutiful.work/sample/sainsburys (PDF: https://dutiful.work/sample/sainsburys.pdf)
- https://dutiful.work/sample/vodafone

Links: https://dutiful.work - https://dutiful.work/developers - https://dutiful.work/check
