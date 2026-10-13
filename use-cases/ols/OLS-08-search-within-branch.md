# OLS-08: Search only within one branch of an ontology

**Question:** How do I look for terms in just one part of an ontology — for example, offer only *heart disorders* when someone types "infarc" into a form field?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) (API)

**You need:** the ontology (for example `mondo`) and the IRI of the term at the top of the branch (for example *heart disorder*, `http://purl.obolibrary.org/obo/MONDO_0005267`). Find the IRI with [OLS-01](OLS-01-find-term-for-concept.md); it is shown under the label on the term's page.

**You get:** matching terms that lie beneath the chosen term, and nothing from the rest of the ontology.

## Steps

### With the API

1. Find the term that sits at the top of the branch you want, and copy its IRI.
2. URL-encode the IRI **once** (`:` becomes `%3A` and `/` becomes `%2F`).
3. Call the `select` endpoint, which is designed for search-as-you-type, with the text typed so far (`q`), the ontology (`ontology`) and the branch (`childrenOf`):

   ```bash
   curl -s 'https://www.ebi.ac.uk/ols4/api/select?q=infarc&ontology=mondo&childrenOf=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0005267&rows=10'
   ```

4. Read the suggestions from `response.docs`. Each has a `label`, an `obo_id` (identifier), an `iri` and the `ontology_name`. `response.numFound` is the total number of matches.
5. In a form, call the endpoint again each time the user types another character, and show the labels as suggestions. Store the `obo_id` or `iri` of the suggestion the user picks, not the label.

The same `childrenOf` parameter works on the full search endpoint, which you would use for a results page rather than for suggestions:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/search?q=infarction&ontology=mondo&childrenOf=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0005267&rows=10'
```

### On the website

The website has no branch filter for searches. To see what a branch contains, open the term at the top of the branch and expand it in the **Tree** panel (see [OLS-03](OLS-03-explore-hierarchy.md)).

## Example

Searching Mondo for `infarction` without a restriction returns 96 terms, including *cerebral infarction* and *multi-infarct dementia*. With `childrenOf` set to *heart disorder* (`MONDO:0005267`), 31 remain, all of them heart disorders:

| Label | Identifier |
|---|---|
| myocardial infarction | `MONDO:0005068` |
| anterolateral myocardial infarction | `MONDO:0006652` |
| acute subendocardial myocardial infarction | `MONDO:0000990` |
| … | … |

## Good to know

- `childrenOf` follows "is a" (subclass) links. `allChildrenOf` also follows the relationships the ontology treats as hierarchical, such as "part of" — useful for anatomy, where *heart left ventricle* is part of, not a kind of, *heart*.
- The restriction only finds terms that the ontology named in `ontology` places beneath the term you give. If a restricted search returns nothing, open that term in that ontology and check in the **Tree** panel that the branch you expect really sits beneath it. In EFO, for example, diseases sit beneath Mondo's *disease* (`MONDO:0000001`).
- Add `type=class` to leave out properties and individuals. Obsolete terms are left out unless you add `obsoletes=true`.

## See also

- [OLS-03: See where a term sits in the hierarchy](OLS-03-explore-hierarchy.md)
- [PAIR-04: Build a code list for a disease area](../two-tools/PAIR-04-code-list-for-branch.md)

*Checked against the live service on 5 October 2026. Counts change as ontologies are updated.*
