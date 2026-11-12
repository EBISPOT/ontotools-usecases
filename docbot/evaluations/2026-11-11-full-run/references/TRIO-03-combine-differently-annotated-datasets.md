# TRIO-03: Combine two datasets that describe the same things differently

**Question:** I want to analyse two datasets together. One records diagnoses as free text, the other as codes from several coding systems. How do I bring both to a common set of terms, so that I can match records and group them?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) turns the free text into terms of a common ontology; [OxO](https://www.ebi.ac.uk/spot/oxo) translates the codes into the same ontology; [OLS](https://www.ebi.ac.uk/ols4) supplies the hierarchy for checking the terms and for grouping them.

**You need:** the different values that occur in the free-text dataset, each listed once; the different codes used in the coded dataset, each listed once and written as *prefix:code* (for example `ICD10CM:I21`, `MESH:D009203`); and a choice of common ontology (here Mondo).

**You get:** for every value and every code, a term of the common ontology — so that equal terms mean equal things across the two datasets — and, for every term, the broader groups it belongs to.

## Steps

### 1. OLS — choose the common ontology

1. Choose an ontology that covers the subject of both datasets and is well connected to the coding systems in use. Browse the candidates in OLS (see [OLS-04](../ols/OLS-04-find-and-inspect-ontology.md)). For diseases, Mondo is a good choice: its maintainers publish mappings to many coding systems.

### 2. Zooma — bring the free-text dataset to the common ontology

2. Open <https://www.ebi.ac.uk/spot/zooma> and enter the values of the free-text dataset, each different value once (its column with the duplicates removed — see step 1 of [TRIO-01](TRIO-01-harmonise-free-text-to-codes.md)).
3. Under **3 Which ontologies to map to?**, select **Choose custom ontologies** and add the common ontology (see [ZOOMA-02](../zooma/ZOOMA-02-choose-target-ontologies.md)).
4. Click **Map … strings**. Accept the green suggestions, and check the others in OLS before accepting or replacing them (see [PAIR-01](../two-tools/PAIR-01-check-zooma-suggestions.md)).
5. Record *value → term* for the first dataset.

### 3. OxO — bring the coded dataset to the common ontology

6. Open <https://www.ebi.ac.uk/spot/oxo>, select **Multiple terms** and paste the codes used in the coded dataset, each different code once and one per line. Codes from different coding systems can go in together.
7. In **To ontologies**, choose the common ontology (`MONDO`) and click **Search**.
8. Click the filter icon in the **Distance** column header and set **Max distance** to 1. This keeps the direct mappings and drops the ones that OxO reached through a chain of other terms.
   - Do not use **Asserted only** here. Mappings are stored in the direction their publisher gave them — from Mondo to the coding systems — so in the direction you are searching, from code to Mondo, even a direct mapping appears as **SSSOM inference**.
9. Check that each code now has one row. If a code has several, compare the candidates in OLS and choose; if it has none, raise **Max distance** for that code and review what appears (see [PAIR-03](../two-tools/PAIR-03-validate-a-mapping.md)).
10. Download the result and record *code → term* for the second dataset.

### 4. OLS — group the terms

11. For each term now in use, open its page in OLS and read its path in the **Tree** panel (see [OLS-03](../ols/OLS-03-explore-hierarchy.md)), or fetch its ancestors with the API below.
12. Choose the level at which you want to group — a level that separates the groups you care about, and under which each of your terms falls.
13. Record *term → group* for every term.

### 5. Combine

14. Add the term and the group to every record of both datasets, using the tables from steps 5, 10 and 13.
15. Records with the same term are about the same thing; records with the same group belong together at the broader level.

### With the APIs

Free text to Mondo:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "heart attack"}, {"textToMap": "heart failure"},
          {"textToMap": "atrial fibrillation"}, {"textToMap": "asthma"}
        ],
        "targetOntologies": ["mondo"],
        "includeOtherOntologies": false
      }'
```

Codes to Mondo, direct mappings only:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{
        "queries": ["ICD10CM:I21", "MESH:D009203", "DOID:5844", "ICD10CM:I50", "MESH:D001281", "ICD10CM:J45"],
        "objectPrefixes": ["MONDO"],
        "columnFilters": [{"id": "distance", "value": "1"}],
        "page": 0,
        "size": 100,
        "groupBySpo": true
      }'
```

Ancestors of a term, for grouping:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068/hierarchicalAncestors?size=100'
```

## Example

**Dataset A — free text, through Zooma**

| Value | Mondo term | Confidence |
|---|---|---|
| heart attack | `MONDO:0005068` myocardial infarction | 100% |
| heart failure | `MONDO:0005252` heart failure | 100% |
| atrial fibrillation | `MONDO:0004981` atrial fibrillation | 100% |
| asthma | `MONDO:0004979` asthma | 100% |

**Dataset B — codes, through OxO** (to `MONDO`, **Max distance** 1)

| Code | Mondo term | Predicate |
|---|---|---|
| `ICD10CM:I21` | `MONDO:0005068` myocardial infarction | `SKOS:exactMatch` |
| `MESH:D009203` | `MONDO:0005068` myocardial infarction | `SKOS:exactMatch` |
| `DOID:5844` | `MONDO:0005068` myocardial infarction | `SKOS:exactMatch` |
| `ICD10CM:I50` | `MONDO:0005252` heart failure | `SKOS:exactMatch` |
| `MESH:D001281` | `MONDO:0004981` atrial fibrillation | `SKOS:exactMatch` |
| `ICD10CM:J45` | `MONDO:0004979` asthma | `SKOS:exactMatch` |

Without the distance filter the same six codes return 23 rows, most of them to neighbouring terms such as *acute myocardial infarction*, *coronary thrombosis* and *congestive heart failure*.

**Grouping, from OLS**

| Mondo term | Group |
|---|---|
| `MONDO:0005068` myocardial infarction | heart disorder (`MONDO:0005267`) |
| `MONDO:0005252` heart failure | heart disorder (`MONDO:0005267`) |
| `MONDO:0004981` atrial fibrillation | heart disorder (`MONDO:0005267`) |
| `MONDO:0004979` asthma | respiratory system disorder (`MONDO:0005087`) |

A record that says *heart attack* in dataset A and records coded `ICD10CM:I21`, `MESH:D009203` or `DOID:5844` in dataset B now all carry `MONDO:0005068`, and all fall in the group *heart disorder*.

## Good to know

- Coding systems and ontologies do not always divide a subject in the same way, so some codes will have no direct counterpart, and some will have several. Expect to make a few decisions by hand, and note them.
- Translation loses detail when a code is more specific than any term (or the reverse). Keep the original value or code next to the new term in your combined data.
- A term can have more than one parent, and so can belong to more than one group. Decide whether a record may be counted in several groups, or which group takes precedence.
- Grouping by an ancestor only works for ancestors within the one ontology. That is the reason for bringing both datasets to a single ontology first.
- Write down the date, the ontology version (shown on the ontology's page in OLS) and the OxO data release (shown in the **Data Content** box on OxO's home page). All three change.

## See also

- [TRIO-01: Harmonise free-text values into ontology terms and codes](TRIO-01-harmonise-free-text-to-codes.md)
- [OXO-05: Keep only the mappings that meet your evidence requirements](../oxo/OXO-05-filter-by-evidence.md)
- [OLS-03: See where a term sits in the hierarchy](../ols/OLS-03-explore-hierarchy.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Results change as the data are updated.*
