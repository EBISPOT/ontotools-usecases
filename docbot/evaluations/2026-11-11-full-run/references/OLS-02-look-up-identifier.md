# OLS-02: Find out what an identifier means

**Question:** I have an ontology identifier such as `MONDO:0005068` in my data — what does it mean?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4)

**You need:** the identifier, in any of these forms: a CURIE (`MONDO:0005068`), the underscore form (`MONDO_0005068`) or the full IRI (`http://purl.obolibrary.org/obo/MONDO_0005068`).

**You get:** the term's label, definition, synonyms, cross-references and relations.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4>.
2. Paste the identifier into the **Search OLS...** box.
3. In the drop-down, look under **Jump to** and click the entry for the term. If the term is listed more than once, choose the entry whose ontology badge matches the identifier's prefix (here **MONDO**); the other entries are copies of the term imported into other ontologies.
   - Alternatively press **Enter** and, on the results page, open the result that is *not* marked **IMPORTED**.
4. Read the term's page:
   - the **label** at the top, with the IRI and a **Copy** button beneath it;
   - the **Definition**;
   - the synonyms, grouped by kind (for example **Exact Synonyms**);
   - **Also appears in** — other ontologies that reuse the term;
   - **Class Information** — the term's other annotations, such as database cross-references;
   - **Class Relations** — its parent classes and other relationships.
5. To see the full record as data, click the **JSON** icon at the top right of the page.

### With the API

If you know which ontology the identifier belongs to:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0005068'
```

The term is in `_embedded.terms[0]`, with `label`, `description`, `synonyms`, `obo_xref` (cross-references), `is_obsolete` and links to its parents and children.

If you do not know the ontology, leave it out:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/terms?obo_id=MONDO:0005068'
```

This returns one record for every ontology that contains the term. Use the record with `"is_defining_ontology": true`.

To look a term up by IRI, put the IRI in the path, URL-encoded **twice**:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068'
```

## Example

`MONDO:0005068` resolves to:

| Field | Value |
|---|---|
| Label | myocardial infarction |
| Definition | Gross necrosis of the myocardium, as a result of interruption of the blood supply to the area, as in coronary thrombosis. |
| Synonyms (some) | heart attack, MI, myocardial infarct |
| Also appears in | EFO, GENEPIO, OOSTT, PRIDE |

Its page is <https://www.ebi.ac.uk/ols4/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068>.

## Good to know

- The prefix of an identifier usually tells you the ontology: `MONDO:` is Mondo, `GO:` is the Gene Ontology, `HP:` is the Human Phenotype Ontology. In OLS addresses and API calls the ontology is written in lower case (`mondo`, `go`, `hp`).
- If a search for an identifier finds nothing, the term may be obsolete. Tick **Include obsolete terms** and search again (see [OLS-05](OLS-05-check-obsolete-term.md)).
- Properties and individuals work the same way; in the API use `/properties` or `/individuals` in place of `/terms`.

## See also

- [OLS-03: See where a term sits in the hierarchy](OLS-03-explore-hierarchy.md)
- [OXO-01: Find equivalent terms in other ontologies](../oxo/OXO-01-find-equivalent-terms.md)

*Checked against the live service on 5 October 2026.*
