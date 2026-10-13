# TRIO-01: Harmonise free-text values into ontology terms and codes

**Question:** A column of my dataset holds diagnoses as people typed them. How do I turn that column into standard ontology terms and into codes of a coding system such as ICD-10-CM — and know which results I can rely on?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) proposes a term for each value; [OLS](https://www.ebi.ac.uk/ols4) is where you check the doubtful proposals and find terms by hand; [OxO](https://www.ebi.ac.uk/spot/oxo) translates the agreed terms into codes.

**You need:** the different values that occur in the column, each listed once; the ontology you want to annotate with (here Mondo); the prefix of the coding system (here `ICD10CM`).

**You get:** a table giving, for every value, an ontology term and a code, with a note of how each was arrived at — and a short list of values that need a person's decision.

## Overview

| Stage | Tool | What happens |
|---|---|---|
| 1. Propose | Zooma | each value gets a suggested term and a confidence |
| 2. Review | OLS | doubtful suggestions are checked, wrong ones replaced |
| 3. Translate | OxO | the agreed terms are mapped to codes |
| 4. Resolve | OxO and OLS | terms without a published code are looked at one by one |
| 5. Assemble | — | everything is put into one table |

## Steps

### 1. Zooma — propose a term for each value

1. Make a list of the different values that occur in the column, with each value listed once — the column with its duplicates removed (in a spreadsheet, *Remove duplicates*; on the command line, `sort -u`). A column of 10,000 diagnoses may contain only a few hundred different strings. Mapping each of them once is quicker than mapping every row, and makes sure that every row holding the same value ends up with the same term; step 14 joins the results back onto the full column.
2. Open <https://www.ebi.ac.uk/spot/zooma> and enter the values (or upload the file — see [ZOOMA-03](../zooma/ZOOMA-03-annotate-spreadsheet-column.md)).
3. Open **3 Which ontologies to map to?**, select **Choose custom ontologies** and add **MONDO** (see [ZOOMA-02](../zooma/ZOOMA-02-choose-target-ontologies.md)).
4. Click **Map … strings**, and when the results are complete, sort the values into three groups:
   - **accept** — one green suggestion (confidence of 90% or more);
   - **review** — yellow or grey suggestions, or several green ones;
   - **unmapped** — **Did not map**.

### 2. OLS — review the doubtful suggestions

5. For each value in the *review* group, click its **Term ID** to open the term in OLS, and check the definition, the synonyms and the parent terms (see [PAIR-01](../two-tools/PAIR-01-check-zooma-suggestions.md)). Accept the suggestion, or reject it.
6. For each rejected or unmapped value, look for a term: first among Zooma's alternatives (**thumbs down**), then by searching and browsing OLS (see [PAIR-06](../two-tools/PAIR-06-find-term-when-zooma-cannot.md)).
7. Write down the term you settle on for each value, and how you arrived at it: *accepted from Zooma*, *accepted after review*, *chosen by hand*, or *no term*.

### 3. OxO — translate the agreed terms into codes

8. Open <https://www.ebi.ac.uk/spot/oxo>, select **Multiple terms** and paste the identifiers of the agreed terms, one per line.
9. In **To ontologies**, choose `ICD10CM` and click **Search**.
10. Set the **Type** filter to **Asserted only**, and download the result (see [OXO-02](../oxo/OXO-02-map-list-to-target.md)).
11. Where a term has more than one asserted code, choose between them: read the labels, and prefer the code at the same level of generality as the term.

### 4. OxO and OLS — resolve the terms without a published code

12. For each term that has no asserted code, search OxO for that term again without the **Asserted only** filter.
    - If there is an inferred mapping, open it with the eye icon and read what it rests on (see [OXO-04](../oxo/OXO-04-check-mapping-provenance.md)). Accept it if the published mappings behind it link terms with the same meaning.
    - If there is none, open the term in OLS, go up the **Tree** to its parent, and look for the parent's code in OxO. A parent's code is broader than the term; mark it as such.
    - If that fails too, leave the value for manual coding.

### 5. Assemble the result

13. Put the pieces into one table with one row for each different value: the value, the term, how the term was decided, the code, and how the code was obtained.
14. Join the table back to your dataset on the value.

### With the APIs

The same pipeline in three calls. First Zooma:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "heart attack"}, {"textToMap": "T2DM"}, {"textToMap": "asthma"},
          {"textToMap": "high blood pressure"}, {"textToMap": "COPD"}, {"textToMap": "Alzheimers"},
          {"textToMap": "broken leg"}, {"textToMap": "sugar diabetes"}
        ],
        "targetOntologies": ["mondo"],
        "includeOtherOntologies": false
      }'
```

Accept automatically the values whose best candidate has a `confidence` of 0.9 or more, and queue the rest for review. For a term under review, fetch its definition and parents from OLS:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0005408'
```

Then send the agreed terms to OxO, which also reports the ones it could not map:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/batch-map' \
  -H 'Content-Type: application/json' \
  -d '{
        "terms": ["MONDO:0005068", "MONDO:0005148", "MONDO:0004979", "MONDO:0005044",
                  "MONDO:0005002", "MONDO:0004975", "MONDO:0005015", "MONDO:0005315"],
        "objectPrefixes": ["ICD10CM"],
        "inferenceType": ["ASSERTED"],
        "page": 0,
        "size": 100
      }'
```

## Example

Eight values from a diagnosis column.

**Stages 1 and 2 — terms**

| Value | Zooma's suggestion | Confidence | Decision |
|---|---|---|---|
| heart attack | *myocardial infarction* `MONDO:0005068` | 100% | accepted from Zooma |
| T2DM | *type 2 diabetes mellitus* `MONDO:0005148` | 100% | accepted from Zooma |
| asthma | *asthma* `MONDO:0004979` | 100% | accepted from Zooma |
| high blood pressure | *hypertensive disorder* `MONDO:0005044` | 100% | accepted from Zooma |
| COPD | *chronic obstructive pulmonary disease* `MONDO:0005002` | 100% | accepted from Zooma |
| Alzheimers | *Alzheimer disease* `MONDO:0004975` | 84.61% | accepted after review in OLS |
| sugar diabetes | *diabetes mellitus type 2 associated cataract* `MONDO:0005408` | 79.53% | rejected in OLS (an eye disease); *diabetes mellitus* `MONDO:0005015` chosen from Zooma's alternatives |
| broken leg | *fracture of pelvic limb tibia, non-human animal* `MONDO:1015393` | 75.14% | rejected in OLS (an animal disease); *bone fracture* `MONDO:0005315` chosen by hand — broader than the value |

**Stages 3 and 4 — codes**

| Term | ICD-10-CM | How obtained |
|---|---|---|
| `MONDO:0005068` myocardial infarction | `I21` Acute myocardial infarction | asserted exact match |
| `MONDO:0005148` type 2 diabetes mellitus | `E11` Type 2 diabetes mellitus | asserted exact match |
| `MONDO:0004979` asthma | `J45` Asthma | asserted exact match |
| `MONDO:0004975` Alzheimer disease | `G30` Alzheimer's disease | asserted exact match |
| `MONDO:0005015` diabetes mellitus | `E08-E13` Diabetes mellitus | asserted exact match |
| `MONDO:0005044` hypertensive disorder | `I10-I16` | two asserted codes, `I10-I16` and `I15` (Secondary hypertension); the block chosen, because the term is general |
| `MONDO:0005002` chronic obstructive pulmonary disease | `J44.9` | no asserted code; inferred through `DOID:3083` (*chronic obstructive pulmonary disease*), accepted after reading the derivation |
| `MONDO:0005315` bone fracture | — | no mapping to ICD-10-CM in OxO; left for manual coding |

Of the eight values, five got their term straight from Zooma and three needed a person to look at the term. Of the eight terms, five got their code from a published mapping without further thought, two needed a decision (which of two codes to use; whether to accept an inferred mapping), and one could not be coded with these tools.

## Good to know

- The proportion needing review is the number to plan around. Run a sample of your values through stage 1 first; it tells you how much manual work the whole column will take.
- Every wrong term in this example had a confidence between 75% and 85% — and so did one right term. Review everything below 90% rather than relying on a lower cut-off.
- OxO sources do not always include a label for every code (`I10-I16` and `J44.9` above have none). Look such codes up in the coding system itself before you accept them.
- Keep the working table. When the same values come round again next year, you can reuse your decisions and only work on the new values.
- Record the date. Ontologies, curated mappings and mapping sets all change, and a later run may give different results (see [TRIO-02](TRIO-02-update-outdated-annotations.md)).

## See also

- [PAIR-01: Check Zooma's suggestions before you accept them](../two-tools/PAIR-01-check-zooma-suggestions.md)
- [PAIR-05: Convert free-text values into identifiers of a specific vocabulary](../two-tools/PAIR-05-free-text-to-vocabulary-codes.md)
- [OXO-04: Check where a mapping comes from and how it was derived](../oxo/OXO-04-check-mapping-provenance.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Results change as the data are updated.*
