# OLS-09: Let an AI assistant look up ontology terms

**Question:** How can my AI assistant, or an application built on a large language model, look terms up in OLS instead of guessing identifiers?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) (the hosted Model Context Protocol server)

**You need:** an AI assistant or agent framework that can connect to remote MCP servers.

**You get:** an assistant that can search OLS, fetch terms and walk the hierarchy while it answers you.

## Steps

1. Open <https://www.ebi.ac.uk/ols4> and click **MCP Server** in the menu at the top. The page gives the address of the server and lists the tools it offers.
2. In your assistant's settings, add a remote MCP server with:
   - address: `https://www.ebi.ac.uk/ols4/api/mcp`
   - transport: **Streamable HTTP** (not the older SSE transport)
   - authentication: none

   How you do this depends on the assistant; look for "MCP servers", "connectors" or "tools" in its documentation. In Claude Code, for example:

   ```
   claude mcp add --transport http ols https://www.ebi.ac.uk/ols4/api/mcp
   ```

3. Check that the assistant now lists the OLS tools. There are twelve, among them `searchClasses`, `fetch`, `getAncestors`, `getChildren`, `getDescendants`, `listOntologies` and `searchClassesWithEmbeddingModel`.
4. Ask a question that needs a lookup, and say that OLS should be used. For example: *"Use OLS to find the Mondo term for heart attack, then list its parent terms."*
5. Check the answer against OLS: the identifiers the assistant reports should be ones it retrieved through the tools, and you can open them in OLS to confirm (see [OLS-02](OLS-02-look-up-identifier.md)).

### Checking the server without an assistant

You can confirm that the server is reachable from your network with three requests. The first starts a session and returns a session identifier in the `Mcp-Session-Id` response header:

```bash
curl -s -i -X POST 'https://www.ebi.ac.uk/ols4/api/mcp' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"check","version":"0.1"}}}'
```

Send the session identifier back with every later request. Replace `SESSION` in the two commands below with the value you received:

```
curl -s -X POST 'https://www.ebi.ac.uk/ols4/api/mcp' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Mcp-Session-Id: SESSION' \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'

curl -s -X POST 'https://www.ebi.ac.uk/ols4/api/mcp' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'Mcp-Session-Id: SESSION' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
```

The last request returns the list of tools with their parameters.

## Example

Asked for the Mondo term for *heart attack* and its parents, an assistant connected to the server typically calls:

1. `searchClasses` with `query: "heart attack"` and `ontologyId: "mondo"` — which returns *myocardial infarction* (`MONDO:0005068`) with its definition;
2. `getAncestors` with `ontologyId: "mondo"` and `classIri: "http://purl.obolibrary.org/obo/MONDO_0005068"` — which returns *myocardial disorder*, *heart disorder*, *cardiovascular disorder* and the terms above them.

## Good to know

- The server only reads from OLS. It cannot change anything.
- For searching by meaning, the assistant should first call `listEmbeddingModels` and then `searchClassesWithEmbeddingModel` with a model that has `can_embed: true`. This is the tool equivalent of [OLS-07](OLS-07-semantic-search.md).
- The tools `search` and `fetch` follow the conventions that some assistants expect of a "search and fetch" connector; `fetch` takes an identifier of the form `ontologyId+entityIri`, for example `go+http://purl.obolibrary.org/obo/GO_0008150`.
- An assistant can still misread or misreport what a tool returned. Treat its answer as a pointer and confirm important identifiers yourself.

## See also

- [OLS-01: Find the ontology term for a concept](OLS-01-find-term-for-concept.md)
- [OLS-03: See where a term sits in the hierarchy](OLS-03-explore-hierarchy.md)

*Checked against the live service on 5 October 2026. The list of tools may grow.*
