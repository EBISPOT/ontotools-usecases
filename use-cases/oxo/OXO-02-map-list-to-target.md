# OXO-02: Map a list of identifiers to one target ontology

**Question:** I have a list of terms from one ontology. What are their equivalents in a specific target — for example, which ICD-10-CM codes correspond to my Mondo disease terms — and which of my terms have no equivalent there?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** the identifiers, one per line, typed or in a `.txt`, `.csv` or `.tsv` file; and the prefix of the target ontology (for example `ICD10CM`).

**You get:** a table of mappings into the target that you can download, and (through the API) the list of inputs for which nothing was found.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/oxo> and select **Multiple terms**.
2. Enter your terms in the box, one per line. Alternatively drop a file of terms onto the dashed area (or click it to choose a file); the file's terms are added to the box so that you can check them. A counter shows how many terms will be mapped.
3. In **To ontologies**, choose the target, for example `ICD10CM`. Leave **From ontologies** empty.
4. Click **Search**. (In this mode **Enter** starts a new line, so use the button.)
5. Review the table. One input can have several rows: asserted mappings, and mappings OxO inferred from them. To keep only published mappings, click the filter icon in the **Type** column header and choose **Asserted only**.
6. Click the download icon next to **Mappings found** to save the result as `oxo2-mappings.tsv`. The file is in SSSOM format, contains every row that passes your filters (not just the page on screen) and has one line per mapping.
7. To find the inputs that have no mapping, compare the **Subject** column of the downloaded file with your list — or use the API below, which reports them for you.

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/batch-map' \
  -H 'Content-Type: application/json' \
  -d '{
        "terms": ["MONDO:0005068", "MONDO:0005148", "MONDO:0004979", "MONDO:0005015", "MONDO:0005002"],
        "objectPrefixes": ["ICD10CM"],
        "inferenceType": ["ASSERTED"],
        "page": 0,
        "size": 100
      }'
```

The response has three parts:

- `summary` — how many inputs were sent, how many were mapped and how many were not;
- `unmappedInputs` — the inputs with no mapping into the target;
- `mappings.mappings.content` — the mappings themselves.

Leave out `inferenceType` to include inferred mappings as well. Add `?format=sssom-tsv` to the address to receive the mappings as an SSSOM file instead of JSON. A request can carry up to 1,000 terms.

## Example

Mapping five Mondo terms to ICD-10-CM, asserted mappings only:

| Input | Label | ICD-10-CM |
|---|---|---|
| `MONDO:0005068` | myocardial infarction | `ICD10CM:I21` Acute myocardial infarction |
| `MONDO:0005148` | type 2 diabetes mellitus | `ICD10CM:E11` Type 2 diabetes mellitus |
| `MONDO:0004979` | asthma | `ICD10CM:J45` Asthma |
| `MONDO:0005015` | diabetes mellitus | `ICD10CM:E08-E13` Diabetes mellitus (E08-E13) |
| `MONDO:0005002` | chronic obstructive pulmonary disease | — (reported in `unmappedInputs`) |

The API's summary reads `"inputCount": 5, "mappedCount": 4, "unmappedCount": 1`.

## Good to know

- Use identifiers rather than labels in a batch. A label is matched against terms in every ontology, so *type 1 diabetes mellitus* brings back mappings for the term of that name in Mondo, DOID, NCIT, UMLS and others, not just the one you meant.
- An input with no asserted mapping may still have an inferred one. Run the search again without the **Asserted only** filter (or without `inferenceType`) for the terms that were left over, and review what comes back (see [OXO-04](OXO-04-check-mapping-provenance.md)).
- Whether **Asserted only** is the right filter depends on direction. Mappings are stored in the direction their source published them, and Mondo publishes its mappings *from* Mondo. Going the other way — from ICD-10-CM codes *to* Mondo — the same mappings appear as **SSSOM inference** with distance 1, so there you would filter on **Distance** (**Max distance** 1) instead of on **Type**.
- One term can map to several codes, and several terms to the same code. Decide how you will handle these before you load the result into your own data.

## See also

- [OXO-03: Get all the mappings between two ontologies](OXO-03-all-mappings-between-ontologies.md)
- [PAIR-04: Build a code list for a disease area](../two-tools/PAIR-04-code-list-for-branch.md)
- [PAIR-05: Convert free-text values into identifiers of a specific vocabulary](../two-tools/PAIR-05-free-text-to-vocabulary-codes.md)

*Checked against the live service on 5 October 2026 (data release of 4 October 2026). Results change with each data release.*
