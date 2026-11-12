# OXO-04: Check where a mapping comes from and how it was derived

**Question:** Can I rely on this mapping? Who published it and on what basis — and if OxO inferred it, from which published mappings?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** a mapping in an OxO results table (see [OXO-01](OXO-01-find-equivalent-terms.md)).

**You get:** everything recorded about the mapping, and, for an inferred mapping, the chain of published mappings it rests on.

## Steps

### On the website

1. Run a search and find the row you want to check, for example the row *myocardial infarction* (`MONDO:0005068`) `SKOS:exactMatch` *Myocardial infarction* (`HP:0001658`) in the results for `MONDO:0005068`.
2. Look at the **Type** column. **Asserted** means the mapping was published by somebody; **SSSOM inference** means OxO derived it.
3. Click the eye icon at the end of the row. The **Mapping Details** page opens. It has its own address, so you can bookmark it or cite it.
4. Read the sections that are present (empty sections are left out):
   - **Mapping** — the statement itself: subject, predicate, object;
   - **Justification** — how the mapping was made (**Mapping Justification**) and the publisher's confidence, if given;
   - **Provenance** — authors, creators, reviewers and dates, where the source recorded them;
   - **Mapping Set** — the collection the mapping belongs to; click its identifier to open the set's page (see [OXO-07](OXO-07-browse-mapping-sets.md));
   - **Additional Information** — licence, comments and the tool that produced the mapping.
5. For an inferred mapping, read **Inference Details** as well:
   - **Asserted Mappings** lists the published mappings the inference rests on, each with its own justification, confidence and mapping set;
   - **Explanation of inferred mapping** draws the derivation as a graph. Arrows point from the mappings used to the mapping derived from them. Boxes with a solid border are published mappings and name their **Source mapping set**; boxes with a dashed border are derived and name the **Rule applied**. You can drag the graph and zoom it.
6. Judge the inference by its weakest ingredient. An inference from manually curated exact matches deserves more trust than one that passes through a mapping made by matching labels automatically.
7. Click **Back to results** to return to your search with its filters intact.

### With the API

Every mapping has a stable identifier, `mapping_id`, which appears in search results and in the address of its details page. Fetch a mapping by it:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/sssom/mappings/b82408bc-1aa0-373e-8d32-4b90a83ac25b'
```

For an inferred mapping, `asserted_mappings` holds the published mappings it rests on, and `explanation` holds the full derivation: the rule applied at each step and the mappings it was applied to.

## Example

The details page for `MONDO:0005068` `SKOS:exactMatch` `HP:0001658` (<https://www.ebi.ac.uk/spot/oxo/mapping/b82408bc-1aa0-373e-8d32-4b90a83ac25b>) shows **Mapping Justification: MappingChaining** and two asserted mappings under **Inference Details**:

| Subject | Predicate | Object | Justification | Confidence | Mapping set |
|---|---|---|---|---|---|
| `MONDO:0005068` | `SKOS:exactMatch` | `NCIT:C27996` | UnspecifiedMatching | — | `http://purl.obolibrary.org/obo/mondo/mappings/mondo.sssom.tsv` |
| `NCIT:C27996` | `SKOS:exactMatch` | `HP:0001658` | LexicalMatching | 0.85 | `https://w3id.org/sssom/mappings/67df215d-fffd-4d37-b42f-268fa6cea80c` |

So OxO concluded *Mondo term = HPO term* because Mondo says its term equals the NCIt term, and a second source says the NCIt term equals the HPO term. The second of these was made by matching labels automatically. That is worth knowing: the Mondo term is a disease and the HPO term is a phenotype, and Mondo's own, separately published mapping between the two is only a `SKOS:closeMatch`. Whether to treat the two as equivalent is your decision (see [PAIR-03](../two-tools/PAIR-03-validate-a-mapping.md)).

## Good to know

- An inferred mapping follows logically from the published mappings it rests on. It is exactly as reliable as they are — no more.
- **Distance** in the results table tells you how many ontologies an inference passes through. The larger the distance, the more published mappings had to be right for the inference to be right.
- A red **not** in front of a predicate means the source states that the mapping does *not* hold.
- If you believe a published mapping is wrong, the **Mapping Set** section tells you which source to contact (see [OXO-08](OXO-08-find-source-of-incorrect-mapping.md)).

## See also

- [OXO-08: Find where an incorrect mapping came from](OXO-08-find-source-of-incorrect-mapping.md)
- [OXO-05: Keep only the mappings that meet your evidence requirements](OXO-05-filter-by-evidence.md)
- [PAIR-03: Decide whether two mapped terms really mean the same thing](../two-tools/PAIR-03-validate-a-mapping.md)

*Checked against the live service on 5 October 2026 (data release of 4 October 2026).*
