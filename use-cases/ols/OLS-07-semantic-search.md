# OLS-07: Find a term by meaning when you do not know the wording

**Question:** I can describe what I mean in everyday words — for example *ringing in the ears* — but I do not know what ontologies call it. Which terms mean the same thing?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) (embedding-based search)

**You need:** a phrase that describes the concept.

**You get:** terms ranked by how similar their meaning is to your phrase, each with a similarity score.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4>.
2. Type your phrase into the **Search OLS...** box, for example `ringing in the ears`.
3. Open the **Search Model** list under the search box and choose an embedding model instead of **Lexical** (at the time of writing, `llama-embed-nemotron-8b_pca512`).
4. Click **Search**. A blue bar confirms **Embedding search using model: …**, and each result shows a percentage next to its label: the similarity between your phrase and the term.
5. To keep only certain ontologies, type their identifiers into **Filter by ontology** in the blue bar (for example `hp`).
6. Click a result to open the term and check its definition.
7. To find terms similar to a term you already have, open that term's page and scroll to **Similar Classes**. **Predicted similar entities** lists the closest terms across all ontologies; you can switch the **Embedding Model** used.

### With the API

List the available models and note one with `"can_embed": true`:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/v2/llm_models'
```

Search with that model (the `model` parameter is required):

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/v2/classes/llm_search?q=ringing%20in%20the%20ears&model=llama-embed-nemotron-8b_pca512&size=5'
```

Each entry of `elements` has a `curie`, `label`, `ontologyId` and a `score` between 0 and 1. To search a single ontology, put it in the path:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/v2/ontologies/hp/classes/llm_search?q=ringing%20in%20the%20ears&model=llama-embed-nemotron-8b_pca512&size=5'
```

## Example

For `ringing in the ears` the first result of the embedding search is:

| Label | Identifier | Similarity |
|---|---|---|
| Tinnitus | `HP:0000360` | 88.3% |

The default (lexical) search for the same phrase puts terms that merely share its words first — such as *Ear ring embedded in ear lobe* — and Tinnitus is not among the top results.

You can open this example directly: <https://www.ebi.ac.uk/ols4/search?q=ringing+in+the+ears&model=llama-embed-nemotron-8b_pca512>

## Good to know

- The similarity score ranks candidates; it is not a judgement that a term is correct. Results are computed from language-model embeddings and have not been curated, so always read the definition of the term you pick.
- Embedding search is slower than lexical search. Expect to wait a few seconds.
- The models on offer change over time. Only models marked `can_embed: true` can search for a phrase you type; all listed models can be used for **Similar Classes**.
- When your wording is close to what ontologies use, the lexical search in [OLS-01](OLS-01-find-term-for-concept.md) is quicker and more predictable.

## See also

- [OLS-01: Find the ontology term for a concept](OLS-01-find-term-for-concept.md)
- [PAIR-06: Find a term by hand when Zooma cannot map a value](../two-tools/PAIR-06-find-term-when-zooma-cannot.md)

*Checked against the live service on 5 October 2026. Scores and available models change over time.*
