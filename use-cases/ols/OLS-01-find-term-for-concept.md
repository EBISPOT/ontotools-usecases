# OLS-01: Find the ontology term for a concept

**Question:** Which ontology term represents the concept I have in mind — for example *heart attack* — and what is its identifier?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4)

**You need:** a word or phrase that describes the concept.

**You get:** the term's label, identifier, definition and the ontology it belongs to.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4>.
2. Type your word or phrase into the **Search OLS...** box, for example `heart attack`. While you type, a drop-down offers completions, a **Jump to** list of matching terms and ontologies, and a **Search OLS for …** entry.
3. Press **Enter** or click **Search**. The results page tells you how many entities matched ("Showing 10 from a total of …") and shows one card per match.
4. Narrow the results with the panel on the left:
   - under **Type**, tick **Class** to hide properties and individuals;
   - under **Ontology**, tick the ontology (or ontologies) you want to annotate with, for example **MONDO** for diseases. Type in the **Search id...** box to find an ontology in the list.
5. Read the result cards. Each card shows the term's label, its identifier in an orange badge (with a copy icon next to it), its IRI, its description, the **Ontology** it was found in and, under **Also appears in**, other ontologies that reuse the same term.
6. Click the label of the best match to open the term's page, and confirm the definition and synonyms before you use the term.

### With the API

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/search?q=heart%20attack&ontology=mondo&type=class&rows=5'
```

`response.numFound` is the number of matches. Each entry of `response.docs` has the term's `label`, `obo_id` (the identifier), `iri`, `ontology_name` and `description`. Leave out `ontology` to search all ontologies, or give several separated by commas (`ontology=mondo,efo`).

## Example

Searching for `heart attack` across all of OLS returns well over a hundred matches from many ontologies, most of them only loosely related ("Fear of having a heart attack", "Anxiety about having a heart attack", …). After ticking **MONDO** under **Ontology**, six matches remain and the first is:

| Label | Identifier | Ontology |
|---|---|---|
| myocardial infarction | `MONDO:0005068` | MONDO |

The term was found although its label does not contain the words you typed, because *heart attack* is one of its synonyms.

## Good to know

- The same term can be listed several times: once in the ontology that defines it and once for every ontology that imports it. The imported copies carry an **IMPORTED** badge. Untick **Include imported terms** to see each term only in the ontology that defines it.
- Tick **Exact match** to keep only results that contain your search text exactly as you typed it.
- Obsolete terms are left out unless you tick **Include obsolete terms** (see [OLS-05](OLS-05-check-obsolete-term.md)).
- If you do not know the wording ontologies use for your concept, search by meaning instead (see [OLS-07](OLS-07-semantic-search.md)).
- If you have many values to look up, let Zooma propose terms for the whole list (see [ZOOMA-01](../zooma/ZOOMA-01-map-list-of-values.md)).

## See also

- [OLS-02: Find out what an identifier means](OLS-02-look-up-identifier.md)
- [PAIR-02: Find a term and get its code in another vocabulary](../two-tools/PAIR-02-find-term-and-translate.md)

*Checked against the live service on 5 October 2026. Result counts change as ontologies are updated.*
