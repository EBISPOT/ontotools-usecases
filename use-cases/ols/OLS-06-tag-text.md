# OLS-06: Find the ontology terms mentioned in a text

**Question:** Which ontology terms are mentioned in this piece of text — a sample description, an abstract, a protocol?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) (the **Tag Text** page)

**You need:** the text, typed, pasted or in a plain text file.

**You get:** every stretch of the text that matches the label of a term (or a text that a curator has previously mapped to a term), with the term's IRI and ontology.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4> and click **Tag Text** in the menu at the top.
2. Paste or type your text into the box, or drag a text file onto it. OLS tags the text as soon as it is entered; there is no button to press.
3. Read the results:
   - **Tagged Text** repeats your text with the matched stretches highlighted;
   - **Matched Terms** lists each match with its **Matched Text**, **Term IRI**, **Term Label**, **Ontology** and **Match Type** (`LABEL` when the text matches a term's label, `CURATION` when it matches a text that a curator has previously mapped to the term).
4. Limit the results to the ontologies you care about. In the **Ontologies** panel on the right, tick one or more ontologies; only their matches are kept. The number of matches is shown next to each ontology, and **Search ontologies...** helps you find one.
   - Drag the ticked ontologies into order to set their priority.
   - Click the **×** next to an ontology to exclude it altogether.
   - Click **Clear filter** to go back to all ontologies.
5. Tune how much is matched:
   - move the **Min match length** slider to ignore matches shorter than the chosen number of characters (the default is 6);
   - tick **Include substrings** to also show shorter matches that lie inside a longer one.
6. Click **Download CSV** above the **Matched Terms** table to save the matches. Untick the box at the end of a row to leave that match out of the file.

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/ols4/api/v2/tag_text?ontologyId=mondo&minLength=6&includeSubstrings=false' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Liver biopsy from a patient with type 2 diabetes mellitus and prior myocardial infarction."}'
```

Each entry of `entities` has the `start` and `end` position of the match in the text, the `term_label`, `term_iri` and `ontology_id`, and the `string_type` (`LABEL` or `CURATION`).

The API's own defaults are looser than the website's (`minLength=3`, `includeSubstrings=true`), so set both explicitly as above to get the same results as the page. Leave out `ontologyId` to tag against every ontology, or give several separated by commas.

## Example

Text: *Liver biopsy from a patient with type 2 diabetes mellitus and prior myocardial infarction.*

With no ontology selected, the tagger finds 30 matches spread over many ontologies (NCIT, SNOMED, DOID, HP, MONDO, …). After ticking **MONDO**, two remain:

| Matched Text | Term Label | Term IRI |
|---|---|---|
| type 2 diabetes mellitus | type 2 diabetes mellitus | `http://purl.obolibrary.org/obo/MONDO_0005148` |
| myocardial infarction | myocardial infarction | `http://purl.obolibrary.org/obo/MONDO_0005068` |

You can open this example directly: <https://www.ebi.ac.uk/ols4/tag-text?text=Liver%20biopsy%20from%20a%20patient%20with%20type%202%20diabetes%20mellitus%20and%20prior%20myocardial%20infarction.&ontologyId=mondo>

## Good to know

- The tagger matches text against term labels and previously curated texts. It does not interpret meaning, so a concept worded differently from any label is not found. To match by meaning, use [OLS-07](OLS-07-semantic-search.md) for a single phrase or [ZOOMA-04](../zooma/ZOOMA-04-annotate-free-text.md) for a passage.
- The same stretch of text often matches terms in several ontologies. Choosing ontologies in the **Ontologies** panel is the quickest way to get one answer per match.
- The page keeps your text and ontology selection in its address (`?text=…&ontologyId=…`), so you can bookmark or share a tagged text.

## See also

- [ZOOMA-04: Find ontology terms in a passage of free text](../zooma/ZOOMA-04-annotate-free-text.md)
- [OLS-02: Find out what an identifier means](OLS-02-look-up-identifier.md)

*Checked against the live service on 5 October 2026.*
