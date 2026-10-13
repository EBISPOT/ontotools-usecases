# PAIR-05: Convert free-text values into identifiers of a specific vocabulary

**Question:** My values are free text, but the system I am loading them into wants identifiers from one particular vocabulary — MeSH headings for literature searching, say, or ICD-10-CM codes. How do I get from the text to those identifiers?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) to turn the text into ontology terms; [OxO](https://www.ebi.ac.uk/spot/oxo) to translate those terms into the target vocabulary.

**You need:** the values, and the prefix of the target vocabulary (for example `MESH` or `ICD10CM`).

**You get:** for each value, an ontology term and the corresponding identifier in the target vocabulary.

## Why two steps

Zooma suggests terms from the ontologies loaded in OLS. Some vocabularies are not there at all — ICD-10-CM is one — so Zooma cannot suggest their codes. Others are there, but everyday wording is matched to them less reliably (see the example below). It works better to let Zooma map the text to an ontology that is rich in synonyms, and then let OxO carry the result over to the target vocabulary using mappings that the ontology's maintainers have published.

## Steps

### 1. Zooma — map the text to a bridging ontology

1. Open <https://www.ebi.ac.uk/spot/zooma> and enter your values (see [ZOOMA-01](../zooma/ZOOMA-01-map-list-of-values.md)).
2. Open **3 Which ontologies to map to?**, select **Choose custom ontologies** and add one ontology that covers your subject and is well mapped to other vocabularies. For diseases, choose **MONDO**. Leave **Include results from other ontologies** unticked (see [ZOOMA-02](../zooma/ZOOMA-02-choose-target-ontologies.md)).
3. Click **Map … strings** and review the results. Carry forward only the suggestions you are satisfied with (see [PAIR-01](PAIR-01-check-zooma-suggestions.md)).
4. Collect the identifiers of the accepted terms from the **Term ID** column, or download the results and take them from the `ontologyTermID` column. In the file, identifiers are written with an underscore (`MONDO_0005068`); change the first underscore to a colon (`MONDO:0005068`) before the next step.

### 2. OxO — translate the terms

5. Open <https://www.ebi.ac.uk/spot/oxo>, select **Multiple terms** and paste the identifiers, one per line.
6. In **To ontologies**, choose the target vocabulary, for example `MESH`.
7. Click **Search**, then set the **Type** filter to **Asserted only** (see [OXO-02](../oxo/OXO-02-map-list-to-target.md)).
8. Click the download icon to save the mappings.

### 3. Put the two results together

9. Join the two files on the term identifier: Zooma's file gives *value → term* (`textToMap` → `ontologyTermID`), and OxO's gives *term → target identifier* (`subject_id` → `object_id`).
10. List the values that fell out along the way — those Zooma could not map with confidence, and those whose term has no mapping in OxO — and handle them by hand.

### With the APIs

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "heart attack"}, {"textToMap": "T2DM"}, {"textToMap": "high blood pressure"}
        ],
        "targetOntologies": ["mondo"],
        "includeOtherOntologies": false
      }'
```

Take the `termId` of the best candidate for each value, change `_` to `:`, and send the list to OxO:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/batch-map' \
  -H 'Content-Type: application/json' \
  -d '{
        "terms": ["MONDO:0005068", "MONDO:0005148", "MONDO:0005044"],
        "objectPrefixes": ["MESH"],
        "inferenceType": ["ASSERTED"],
        "page": 0,
        "size": 100
      }'
```

## Example

Six values, mapped to Mondo by Zooma and on to MeSH by OxO:

| Value | Zooma: Mondo term | Confidence | OxO: MeSH |
|---|---|---|---|
| heart attack | *myocardial infarction* `MONDO:0005068` | 100% | `MESH:D009203` |
| T2DM | *type 2 diabetes mellitus* `MONDO:0005148` | 100% | `MESH:D003924` |
| asthma | *asthma* `MONDO:0004979` | 100% | `MESH:D001249` |
| high blood pressure | *hypertensive disorder* `MONDO:0005044` | 100% | `MESH:D006973` |
| COPD | *chronic obstructive pulmonary disease* `MONDO:0005002` | 100% | `MESH:D029424` |
| Alzheimers | *Alzheimer disease* `MONDO:0004975` | 84.61% | `MESH:D000544` |

All six Mondo terms have an asserted exact match in MeSH.

For comparison, asking Zooma to map the same text straight to MeSH does much worse: *heart attack* reaches *Myocardial Infarction* with a confidence of only 17%, and *high blood pressure* is matched to the heading *Blood Pressure* (`MESH:D001794`) instead of the disease.

## Good to know

- Each step can lose values, and each can introduce errors. Review Zooma's suggestions before you translate them; a wrong term translated faithfully is still wrong.
- One term can have several identifiers in the target vocabulary, or none. Decide in advance what to do in each case.
- When the terms have no asserted mapping to your target, look at inferred mappings and judge them one by one (see [OXO-04](../oxo/OXO-04-check-mapping-provenance.md)).
- For a workflow that adds a review of the doubtful values and a way to rescue the ones without a code, see [TRIO-01](../three-tools/TRIO-01-harmonise-free-text-to-codes.md).

## See also

- [ZOOMA-02: Choose the ontologies Zooma maps to](../zooma/ZOOMA-02-choose-target-ontologies.md)
- [OXO-02: Map a list of identifiers to one target ontology](../oxo/OXO-02-map-list-to-target.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Results change as the data are updated.*
