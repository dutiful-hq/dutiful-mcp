# Dutiful - Company background reports for agents

Research you can cite. Dutiful generates company background reports combining official registry data, a company-level screen against the OFAC SDN and UK Sanctions List, and a news and web scan. Registry facts vary by country; US coverage is limited to SEC-reporting companies and Canada to federal corporations. EU and UN sanctions lists are not screened. Every finding cites its source. Company reports cost $3 in USDC on Base via x402. Check country coverage before paying.

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

## Try the report path before paying

1. [Read a sample company report](https://dutiful.work/sample/sainsburys). It shows the report format and sources, not a current assessment of a company you choose.
2. [Check coverage for your company - free](https://dutiful.work/check). Enter the company and country, then review the exact matched entity and country-specific fields before paying.
3. If the coverage fits, [use the API or MCP flow](https://dutiful.work/developers). Buying a report requires USDC on Base and an x402-compatible wallet flow. `create_order` returns payment requirements; it does not pay.

A report is not a compliance certificate, credit check or legal opinion. Registry fields vary by country. US coverage is limited to SEC-reporting entities and Canada to federal corporations; EU and UN sanctions lists are not screened.

[Sample PDF](https://dutiful.work/sample/sainsburys.pdf) · [Second sample](https://dutiful.work/sample/vodafone)

## Badge for integrators

If your agent or service screens counterparties with Dutiful, add this badge to your README:

```markdown
[![counterparties screened: dutiful](https://dutiful.work/badge.svg)](https://dutiful.work/developers)
```

It links to our developer docs so your users can see how the checks work.

Links: https://dutiful.work - https://dutiful.work/developers - https://dutiful.work/check
