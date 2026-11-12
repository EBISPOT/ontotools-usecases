# ZOOMA-01: Map a list of free-text values to ontology terms

**Question:** I have a list of free-text values — sample attributes, column values, questionnaire answers. Which ontology term best matches each of them?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma)

**You need:** the values, one per line. Optionally, for each value, the kind of thing it describes (for example *disease* or *organism part*).

**You get:** for each value, one or more suggested terms with a confidence, where the suggestion came from and how it was found — on screen and as a file.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/zooma>.
2. Under **1 Enter strings to map**, stay on the **Map Strings** tab and type or paste your values into the box, one per line. To try Zooma out, click **Load examples**.
3. Optionally say what kind of thing a value is: after the value, press the **Tab** key and type the kind, for example `heart disease` *Tab* `disease`. Zooma uses this as context when it ranks suggestions.
4. Click the green button. Its label counts your values, for example **Map 10 strings**.
5. Wait while the values are processed. The button reads **Searching...**, a bar shows how many values have been done (for example *3 out of 10 processed*), and rows appear in the **Results** table as each value is finished.
6. Read the **Results** table. Each row is one suggested term for one value; a value with several suggestions has several rows.

   | Column | Meaning |
   |---|---|
   | **Text to Map** | your value |
   | **Term Type** | the kind you gave, if you gave any |
   | **Term Label** | the label of the suggested term |
   | **Confidence** | how confident Zooma is in the suggestion, as a percentage |
   | **Term ID** | the term's identifier; click it to open the term in OLS |
   | **Source** | the ontology the term was found in, or the data resource whose curators made the mapping |
   | **Prediction Type** | how the suggestion was found: **Lexical** (matching words), **Embedding** (matching meaning), **Curated** (a curator mapped this text before) or **Replace obsolete** (an obsolete term was swapped for its successor) |

7. Use the row colours to decide where to look:
   - **green** — confidence of 90% or more;
   - **yellow** — worth checking: the confidence is below 90%, or several suggestions for the same value all reached 90%;
   - **grey** with a warning sign — a low score, below 20%;
   - **Did not map** in the **Confidence** column — Zooma found nothing.
8. Click the download icon next to the **Results** heading (**Download as TSV**) to save the table as `zooma_results.tsv`.

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "heart disease", "propertyType": "disease"},
          {"textToMap": "cerebellum", "propertyType": "organism part"}
        ],
        "targetOntologies": ["mondo", "uberon"],
        "includeOtherOntologies": false
      }'
```

The response has one entry in `mappings` per value. Its `candidates` are the suggestions, best first, each with a `termId`, `label`, `uri`, `confidence` (between 0 and 1), `datasource` and `mappingProvenance`. An empty `candidates` list means nothing was found. `propertyType`, `targetOntologies` and `includeOtherOntologies` are optional.

## Example

With **Load examples** and the settings Zooma starts with, the results include:

| Text to Map | Term Type | Term Label | Confidence | Term ID | Prediction Type |
|---|---|---|---|---|---|
| Homo sapiens | organism | Homo sapiens | 100.00% | `NCBITaxon:9606` | Lexical |
| heart disease | disease | heart disorder | 100.00% | `MONDO:0005267` | Lexical |
| cerebellum | organism part | cerebellum | 100.00% | `UBERON:0002037` | Lexical |
| CD4-positive | cell type | T cell | 100.00% | `CL:0000084` | Curated |
| C57Black/6 | strain | C57BL/6ByJ Mouse | 84.93% | `NCIT_C37382` | Embedding |

The first four rows are green and can be accepted as they are. The last is yellow: a near miss that a person should look at. The heading above the table reads **Results (11 out of 10 mapped)**, because one of the ten values (`BRCA1`) has five suggestions at 100%.

## Good to know

- The count in the heading, **Results (*m* out of *n* mapped)**, is the number of rows with a confidence of 90% or more. When one value has several such rows, *m* can be larger than *n*.
- The confidence is Zooma's ranking score, not a guarantee. Check anything that is not green, and spot-check the green rows too (see [PAIR-01](../two-tools/PAIR-01-check-zooma-suggestions.md)).
- Which terms are suggested depends on the ontologies Zooma is allowed to use. It starts with a broad preset; choosing the ontologies you actually want gives better results (see [ZOOMA-02](ZOOMA-02-choose-target-ontologies.md)).
- The downloaded file contains every suggestion Zooma returned — whatever you approve, replace or remove on the screen (see [ZOOMA-05](ZOOMA-05-review-and-choose-alternative.md)) — with the columns `textToMap`, `propertyType`, `ontologyTermLabel`, `ontologyTermID`, `ontologyURI`, `mappingConfidence` and `datasource`. Confidence is written as a number between 0 and 1. The rows are in the order in which the results came back, which need not be the order of your list.
- Identifiers in the API and in the file use an underscore (`MONDO_0005267`); elsewhere the same term is written `MONDO:0005267`.
- For terms whose identifier does not have a digit straight after the prefix — NCI Thesaurus terms such as `NCIT_C37382` — the **Term ID** column keeps the underscore, and its link leads to an error page in OLS instead of the term. Search OLS for the identifier instead (see [OLS-02](../ols/OLS-02-look-up-identifier.md)).
- Zooma remembers the settings of sections **2** and **3** in your browser. A **customized** label next to a section heading reminds you that settings are in force.
- For values that sit in a spreadsheet, see [ZOOMA-03](ZOOMA-03-annotate-spreadsheet-column.md). For running text, see [ZOOMA-04](ZOOMA-04-annotate-free-text.md).

## See also

- [ZOOMA-05: Understand why Zooma suggested a term, choose a better one, and keep a record](ZOOMA-05-review-and-choose-alternative.md)
- [TRIO-01: Harmonise free-text values into ontology terms and codes](../three-tools/TRIO-01-harmonise-free-text-to-codes.md)

*Checked against the live service on 5 October 2026. Suggestions and confidences change as ontologies and curated mappings are updated.*
