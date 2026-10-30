# Dutiful - Company background reports for agents

Research you can cite. Dutiful generates company background reports combining official registry data, a company-level screen against the OFAC SDN and UK Sanctions List, and a news and web scan. Registry facts vary by country; US coverage is limited to SEC-reporting companies and Canada to federal corporations. EU and UN sanctions lists are not screened. Every finding cites its source. Company reports cost $3 in USDC on Base via x402. Check country coverage before paying.

## For agents (MCP)

Streamable HTTP MCP server: `https://dutiful.work/mcp`

Tools:

- `check_coverage` - check whether a company is in a covered registry (free)
- `create_order` - create a report order and get x402 payment requirements
- `get_report` - fetch the finished report

Server card: `https://dutiful.work/.well-known/mcp/server-card.json`

## Run a free MCP check (no wallet)

Requires Node.js 22 and npm. Run once in a new folder:

```sh
mkdir dutiful-free-check && cd dutiful-free-check
npm init -y
npm install --ignore-scripts --no-audit --no-fund --save-exact @modelcontextprotocol/sdk@1.32.2
cat > free-check.mjs <<'JS'
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

const client = new Client({ name: 'dutiful-free-check', version: '1.0.0' }, { capabilities: {} });
const transport = new StreamableHTTPClientTransport(new URL('https://dutiful.work/mcp'));
try {
  // connect sends initialize and notifications/initialized.
  await client.connect(transport);
  const { tools } = await client.listTools();
  console.log('Tools:', tools.map(tool => tool.name).join(', '));
  // One free public-company lookup. Do not select a candidate or call create_order.
  const result = await client.callTool({
    name: 'check_coverage',
    arguments: { company: 'J SAINSBURY PLC', country: 'GB' }
  }, undefined, { timeout: 60000 });
  if (result.isError) throw new Error('Coverage check failed; no paid follow-up was attempted.');
  const data = result.structuredContent ?? JSON.parse(result.content.find(item => item.type === 'text').text);
  if (!Array.isArray(data.candidates) || data.candidates.length === 0) throw new Error('No suitable match; stop without a paid call.');
  // Print public registry fields only, not the pending order ID.
  console.log(JSON.stringify({ candidates: data.candidates.map(({ idx, ref, name }) => ({ idx, ref, name })) }, null, 2));
} finally {
  await client.close();
}
JS
node free-check.mjs
```

This calls only `check_coverage`, not `create_order` or a payment endpoint. No account, API key, wallet or signature is needed. The free check creates or reuses a pending order/cache record internally; it is zero-payment, not stateless. Rate limits apply, so do not run it repeatedly to poll.

A separate smoke test with SDK 1.32.2 / Node 22.23.4 on 2026-10-29 observed initialization negotiating protocol `2025-06-18`, tools/list returning the three tools, and this GB lookup returning five candidates. The SDK's optional background SSE GET returned 405, but the POST-based check completed. This shortened quickstart was syntax-checked and replayed offline, not rerun against the remote service. This is evidence for this client and free flow, not every client or the paid flow.

Example output, abbreviated to public fields (matches can change):

```text
Tools: check_coverage, create_order, get_report
{
  "candidates": [
    { "idx": 0, "ref": "00185647", "name": "J SAINSBURY PLC" },
    ...
  ]
}
```

No candidate is selected and no report is purchased. Keep pending order IDs and session headers out of public logs. If the check fails or finds no suitable match, stop; do not proceed to a paid call.

## A free coverage-check example

Question: "Does this name point to the company I mean, and what would a report leave out?"

For a UK company, compare the legal name and company number, not just the trading name. The free [Sainsbury's sample](https://dutiful.work/sample/sainsburys) identifies J SAINSBURY PLC as company 00185647 and links to its [Companies House record](https://find-and-update.company-information.service.gov.uk/company/00185647). The sample is a dated example, not a current check of that company.

Before paying for your own company check, run `check_coverage` with the company name and country (for example, `{"company":"J SAINSBURY PLC","country":"GB"}`). Review the returned matching entities and country-specific report scope. The check is free and does not buy a report. Do not assume which match index will be returned.

The sample's gaps matter: it does not cover credit scores/payment behaviour, PEP screening or civil litigation, and it does not identify beneficial owners beyond what the register publishes. A registry match is not a verdict that a company is safe to trade with. US coverage is limited to SEC-reporting entities and Canada to federal corporations; the company-level sanctions screen covers the OFAC SDN and UK Sanctions List; EU and UN lists are not screened.

If you choose to continue, `create_order` returns payment requirements, not payment. Company Reports cost $3.00 USDC on Base via x402, with a separate wallet-signing/payment step. [Connection and payment quickstart](https://dutiful.work/developers).

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
