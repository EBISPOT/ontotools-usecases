# OLS-05: Check whether a term is obsolete and find its replacement

**Question:** Is the term I am using still current? If it has been made obsolete, which term should I use instead?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4)

**You need:** the identifier of the term, for example `EFO:0000612`.

**You get:** whether the term is obsolete and, where the ontology records one, its replacement.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4>.
2. Tick **Include obsolete terms** under the search box. Without this, obsolete terms are left out of search results, so a search for an obsolete identifier finds nothing.
3. Paste the identifier into the **Search OLS...** box and press **Enter**.
4. Open the result from the ontology that owns the identifier (for `EFO:0000612`, the result with **Ontology: EFO**).
5. Look at the top of the term's page:
   - if the term is obsolete, a red box says **This class is deprecated.** and the label carries a **DEPRECATED** badge;
   - the box may also give the version in which the term was deprecated (**Deprecated since version**), the term that takes its place (**Replaced by**) and the **Reason**.
6. Under **Class Information**, find **term replaced by** and click the replacement to open its page. Check its definition before you switch to it.
7. If there is no red box, the term is current and you can keep using it.

### With the API

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/efo/terms?obo_id=EFO:0000612'
```

In `_embedded.terms[0]`, `is_obsolete` is `true` for an obsolete term and `term_replaced_by` holds the IRI of its replacement (or `null` if the ontology does not record one).

To include obsolete terms in an API search, add `obsoletes=true`:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/search?q=EFO:0000612&obsoletes=true'
```

## Example

`EFO:0000612` is labelled *obsolete_myocardial infarction*. Its page shows:

| Field | Value |
|---|---|
| Deprecated since version | 3.88.0 |
| Replaced by | `http://purl.obolibrary.org/obo/MONDO_0005068` (myocardial infarction, `MONDO:0005068`) |
| Reason | Replaced by Mondo term MONDO_0005068, with which this term was previously merged. |

## Good to know

- Not every obsolete term has a replacement. Some ontologies give a reason or suggest alternatives to consider instead; others give nothing. In that case, see [TRIO-02](../three-tools/TRIO-02-update-outdated-annotations.md) for ways to find a successor with OxO and Zooma.
- In the hierarchy, obsolete terms are hidden unless you tick **Show obsolete terms** in the **Tree** panel.
- An obsolete term keeps its identifier and its page, so old data can still be interpreted.

## See also

- [OXO-06: Find mappings when a search comes back empty](../oxo/OXO-06-search-returns-nothing.md)
- [TRIO-02: Bring outdated annotations up to date](../three-tools/TRIO-02-update-outdated-annotations.md)

*Checked against the live service on 5 October 2026.*
