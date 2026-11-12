# TRIO-02: Bring outdated annotations up to date

**Question:** My data were annotated with ontology terms some years ago. Which of those terms have since been made obsolete, and what should each be replaced with?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) tells you which terms are obsolete and what the ontology says replaces them; [OxO](https://www.ebi.ac.uk/spot/oxo) finds a successor through mappings when the ontology names none; [Zooma](https://www.ebi.ac.uk/spot/zooma) finds one from the term's wording when there are no mappings either.

**You need:** the term identifiers used in your data, each different identifier listed once, and, if you still have them, the original free-text values the terms were assigned to.

**You get:** a table of *old term → new term* with a note of how each replacement was found.

## Overview

Work through three questions for each term, and stop at the first that gives an answer.

| | Question | Tool |
|---|---|---|
| 1 | Is the term obsolete, and does its ontology name a replacement? | OLS |
| 2 | If not, is the obsolete term mapped to a current term? | OxO |
| 3 | If not, which current term matches the old term's wording? | Zooma |

Whatever the route, finish by checking the proposed replacement in OLS.

## Steps

### 1. OLS — find the obsolete terms and their stated replacements

1. For each identifier, look the term up in OLS with **Include obsolete terms** ticked (see [OLS-05](../ols/OLS-05-check-obsolete-term.md)). For more than a few terms, use the API below instead of the website.
2. Sort the terms into three groups:
   - **current** — nothing to do;
   - **obsolete, with a replacement** — the term's page says **Replaced by**, and **term replaced by** appears under **Class Information**;
   - **obsolete, no replacement** — the page says the term is deprecated but names no successor. Read the **Reason** if there is one: it sometimes suggests what to use instead.
3. For the second group, open the replacement and check that its definition fits the way the old term was used in your data. Record *old → new, replacement stated by the ontology*.

### 2. OxO — find a successor through mappings

For each term in the *obsolete, no replacement* group:

4. Open <https://www.ebi.ac.uk/spot/oxo> and enter the identifier.
5. Click **▸ More options** and tick **Obsolete terms** under **Also show**. Without this, mappings that involve an obsolete term are hidden.
6. In **To ontologies**, choose the ontology or ontologies you now annotate with, and click **Search**.
7. If rows come back, prefer an exact match with a small **Distance**, and one whose label matches the old term's label. Open the candidate with the **OLS** link and check that it is current and that its definition fits. Record *old → new, found through mappings*.

### 3. Zooma — find a successor from the wording

For each term that is still unresolved:

8. Take the best description you have of what was meant: the original free-text value if you still have it; otherwise the old term's label with any "obsolete" prefix removed.
9. Open <https://www.ebi.ac.uk/spot/zooma>, enter the text, and choose the ontologies you now annotate with under **3 Which ontologies to map to?** (see [ZOOMA-02](../zooma/ZOOMA-02-choose-target-ontologies.md)).
10. Click **Map … strings**. Open the suggested term in OLS through its **Term ID** and check it as before (see [PAIR-01](../two-tools/PAIR-01-check-zooma-suggestions.md)). Record *old → new, re-mapped from text*.
11. Terms that remain unresolved after all three steps need a decision by someone who knows the data.

### 4. Apply the changes

12. Replace the old identifiers in your data using the table, and keep the table — with the date — as a record of what was changed and why.

### With the APIs

Check a term's status and stated replacement in OLS:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/efo/terms?obo_id=EFO:0000612'
```

In `_embedded.terms[0]`, read `is_obsolete` and `term_replaced_by`.

Ask OxO for mappings from an obsolete term into the ontologies you use:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["DOID:4025"], "includeObsolete": true, "objectPrefixes": ["MONDO", "EFO"], "page": 0, "size": 100, "groupBySpo": true}'
```

Ask Zooma to map the old label:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{"properties": [{"textToMap": "infiltrating ductal carcinoma"}], "targetOntologies": ["mondo", "efo"], "includeOtherOntologies": false}'
```

## Example

Four identifiers from an old dataset, to be brought up to date for annotation with Mondo and EFO.

| Old term | OLS | OxO | Zooma | New term |
|---|---|---|---|---|
| `MONDO:0005068` myocardial infarction | current | | | unchanged |
| `EFO:0000612` obsolete_myocardial infarction | obsolete; **Replaced by** `MONDO:0005068` | | | `MONDO:0005068` myocardial infarction |
| `DOID:4025` obsolete steatitis | obsolete; no replacement named | with **Obsolete terms** ticked: exact match to `MONDO:0006979` (*steatitis*), distance 1 | | `MONDO:0006979` steatitis |
| `EFO:0000184` obsolete_infiltrating ductal carcinoma | obsolete; no replacement named | no mappings | `infiltrating ductal carcinoma` → *invasive ductal breast carcinoma* `MONDO:0004953`, 100% | `MONDO:0004953` invasive ductal breast carcinoma |

In the last row Zooma succeeds because the old label, *infiltrating ductal carcinoma*, is recorded as a synonym of the Mondo term.

## Good to know

- An obsolete term is not always replaced one for one. A term may have been split into several narrower terms, or merged into a broader one. Where the ontology offers several alternatives rather than one replacement, choosing between them needs the original context.
- The mappings OxO finds for an obsolete term usually exist because another source still maps one of its own, current terms to the retired identifier; OxO turns that mapping around. Treat the result as a candidate and confirm it in OLS.
- Zooma itself swaps obsolete terms for their stated replacements when it maps text; such suggestions have the **Prediction Type** *Replace obsolete*. Text annotated afresh with Zooma therefore does not bring obsolete terms back in.
- Doing this once a year is far less work than doing it once a decade. Ontologies record when a term was deprecated (**Deprecated since version**), so you can also tell how long an annotation has been out of date.

## See also

- [OLS-05: Check whether a term is obsolete and find its replacement](../ols/OLS-05-check-obsolete-term.md)
- [OXO-06: Find mappings when a search comes back empty](../oxo/OXO-06-search-returns-nothing.md)
- [PAIR-01: Check Zooma's suggestions before you accept them](../two-tools/PAIR-01-check-zooma-suggestions.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Results change as the data are updated.*
