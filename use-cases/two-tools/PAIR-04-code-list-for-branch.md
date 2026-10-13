# PAIR-04: Build a code list for a disease area

**Question:** I need every code that belongs to a subject area — for example, to select all records about diabetes. Which terms does an ontology place under *diabetes mellitus*, and which codes in my coding system (say ICD-10-CM) correspond to them?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) to list the terms in the branch; [OxO](https://www.ebi.ac.uk/spot/oxo) to translate them into the coding system.

**You need:** the concept that defines the area, and the prefix of the target coding system (for example `ICD10CM`).

**You get:** the list of terms in the branch, the codes that map to them, and the terms for which no code was found.

## Steps

### 1. OLS — choose the top term and list its branch

1. Open <https://www.ebi.ac.uk/ols4> and find the term that defines your area (see [OLS-01](../ols/OLS-01-find-term-for-concept.md)) — here *diabetes mellitus*, `MONDO:0005015`.
2. On the term's page, look at the **Tree** panel. The number in brackets after the term is the number of terms beneath it. Expand the term and glance through its children to confirm that the branch covers what you want, and nothing you do not want.
3. List the branch. For a handful of terms you can copy them from the tree. For anything larger, ask the API for the descendants (below), which returns them in one go.

### 2. OxO — translate the branch

4. Open <https://www.ebi.ac.uk/spot/oxo> and select **Multiple terms**.
5. Paste the identifiers — the top term and all its descendants — one per line.
6. In **To ontologies**, choose the coding system, for example `ICD10CM`, and click **Search**.
7. Click the filter icon in the **Type** column header and choose **Asserted only** to keep the published mappings.
8. Click the download icon to save the result as an SSSOM file.

### 3. Deal with the terms that have no code

9. Compare the **Subject** column of the result with your list to find the terms without a code. Expect many: an ontology usually divides an area more finely than a coding system does.
10. For each term without a code, decide between:
    - **using its parent's code** — look the term up in OLS, go up the **Tree** to the nearest ancestor that does have a code, and record that the code is broader than the term;
    - **reviewing inferred mappings** — repeat the OxO search for these terms without the **Asserted only** filter, and check what comes back (see [PAIR-03](PAIR-03-validate-a-mapping.md)).

### With the APIs

The two steps chain together. This example uses [`jq`](https://jqlang.org/) to pass the output of OLS to OxO.

List the branch — the descendants plus the top term itself:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005015/hierarchicalDescendants?size=500' \
  | jq '[._embedded.terms[].obo_id] + ["MONDO:0005015"]' > branch.json
```

Map the branch to ICD-10-CM:

```bash
jq '{terms: ., objectPrefixes: ["ICD10CM"], inferenceType: ["ASSERTED"], page: 0, size: 100}' branch.json \
  | curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/batch-map' \
      -H 'Content-Type: application/json' -d @- > codes.json
```

Read the summary, the codes, and the terms without a code:

```bash
jq '.summary' codes.json
jq -r '.mappings.mappings.content[] | [.subject_id, .subject_label, .object_id, .object_label] | @tsv' codes.json
jq -r '.unmappedInputs[]' codes.json
```

If the branch has more than 500 terms, request further pages from OLS (`&page=1`, …); OxO accepts up to 1,000 terms per request, and returns its mappings in pages of up to 100.

## Example

*Diabetes mellitus* (`MONDO:0005015`) has 48 descendants in Mondo, so the branch has 49 terms. Six of them have an asserted exact match in ICD-10-CM:

| Mondo term | | ICD-10-CM |
|---|---|---|
| `MONDO:0005015` | diabetes mellitus | `ICD10CM:E08-E13` Diabetes mellitus (E08-E13) |
| `MONDO:0005147` | type 1 diabetes mellitus | `ICD10CM:E10` Type 1 diabetes mellitus |
| `MONDO:0005148` | type 2 diabetes mellitus | `ICD10CM:E11` Type 2 diabetes mellitus |
| `MONDO:7770003` | cystic fibrosis-related diabetes | `ICD10CM:E13` Other specified diabetes mellitus |
| `MONDO:0005406` | gestational diabetes | `ICD10CM:O24.4` Gestational diabetes mellitus |
| `MONDO:0016391` | neonatal diabetes mellitus | `ICD10CM:P70.2` Neonatal diabetes mellitus |

OxO's summary reads `"inputCount": 49, "mappedCount": 6, "unmappedCount": 43`. The 43 terms without a code are mostly rare, genetically defined forms of diabetes that ICD-10-CM does not distinguish.

## Good to know

- The result is only as good as the choice of top term. Two of the six codes above lie outside the E08–E13 block (`O24.4` and `P70.2`): the ontology treats gestational and neonatal diabetes as kinds of diabetes mellitus, while ICD-10-CM files them under pregnancy and newborn conditions. Whether they belong in your list is for you to decide.
- A code list built this way goes from terms to codes. It will not contain codes that have no matching term in the branch — for example the many subdivisions of `E10` and `E11`. If you need every subdivision, expand the codes in the coding system itself.
- `hierarchicalDescendants` follows "is a" and other hierarchical relationships such as "part of"; use `descendants` to follow "is a" only (see [OLS-03](../ols/OLS-03-explore-hierarchy.md)).
- Record the date and the ontology version (shown on the ontology's page in OLS) with your list. Both the branch and the mappings change over time.

## See also

- [OLS-03: See where a term sits in the hierarchy](../ols/OLS-03-explore-hierarchy.md)
- [OXO-02: Map a list of identifiers to one target ontology](../oxo/OXO-02-map-list-to-target.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Counts change as the data are updated.*
