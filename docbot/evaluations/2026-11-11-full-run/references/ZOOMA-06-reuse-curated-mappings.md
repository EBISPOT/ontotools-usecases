# ZOOMA-06: Reuse mappings that curators have already made

**Question:** Has a curator at one of the EMBL-EBI data resources already mapped this text to an ontology term? And how do I control which resources' curated mappings Zooma draws on?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma)

**You need:** your values, and an idea of which data resources are closest to your own data (for example the GWAS Catalog or Expression Atlas).

**You get:** suggestions that repeat decisions curators have made before, labelled with the resource they come from.

## Background

Curators at EMBL-EBI data resources map free-text descriptions to ontology terms as part of their daily work. Zooma draws on these curated mappings: when your text is one that a curator has mapped before, Zooma suggests the same term with high confidence and tells you which resource the decision came from. The resources are listed in section **2 Where to get mappings?**.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/zooma> and enter your values (see [ZOOMA-01](ZOOMA-01-map-list-of-values.md)).
2. Click the heading **2 Where to get mappings?** to open the section. Each green label is a data resource whose curated mappings Zooma can use. The number in front of a name is its priority.
3. Decide which resources to use:
   - click the **×** on a label to exclude that resource; it moves below the others and loses its number;
   - click an excluded resource to bring it back; it returns at the end of the order;
   - use **Select all** or **Select none** to change all of them at once.
4. Decide which resources to prefer. Drag the labels into order: the resource numbered 1 has the highest priority.
5. Click **Map … strings**.
6. In the **Results** table, look at two columns:
   - **Prediction Type** reads **Curated** when the suggestion repeats a curator's earlier decision;
   - **Source** then names the resource the decision came from, instead of an ontology.
7. Click **Curated** in the **Prediction Type** column to see the provenance of the suggestion (see [ZOOMA-05](ZOOMA-05-review-and-choose-alternative.md)).

### With the API

List the resources (the entries with `"type": "DATABASE"`) and note their `name`:

```bash
curl -s 'https://www.ebi.ac.uk/spot/zooma/v3/api/sources'
```

Name the resources to use in `filter.required`, and those to prefer in `filter.preferred`:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "Exposure to tobacco smoke at home"},
          {"textToMap": "cooked broccoli"}
        ],
        "filter": {"required": ["ukbiobank", "atlas"], "preferred": ["atlas"]}
      }'
```

A curated suggestion has `"method": "curated"` in its `mappingProvenance`, and its `datasource` is the name of the resource. Leave `filter` out to use all resources.

## Example

| Text to Map | Term Label | Term ID | Confidence | Source | Prediction Type |
|---|---|---|---|---|---|
| Exposure to tobacco smoke at home | environmental tobacco smoke exposure measurement | `EFO:0008361` | 100% | ukbiobank | Curated |
| cooked broccoli | sulforaphane | `CHEBI:47807` | 100% | atlas | Curated |

Zooma can make these suggestions only because a curator made the same decision before: the first text is the wording of a UK Biobank data field (source `ukbiobank`), and the second was mapped by an Expression Atlas curator (source `atlas`). The second text does not share a single word with the label of its term.

If the two resources are excluded (in the API, by leaving them out of `filter.required`), the curated suggestions disappear and Zooma falls back on matching the text against ontology terms. With the ontologies Zooma starts with, the heading then reads **Results (0 out of 2 mapped)**:

| Text to Map | Term Label | Term ID | Confidence | Source | Prediction Type |
|---|---|---|---|---|---|
| Exposure to tobacco smoke at home | Secondhand Smoke Exposure in Household during Childhood | `NCIT_C156837` | 78.84% | ncit | Embedding |
| Exposure to tobacco smoke at home | environmental tobacco smoke exposure measurement | `EFO:0008361` | 78.37% | efo | Embedding |
| cooked broccoli | broccoli (cooked) | `FOODON:03311420` | 89.00% | foodon | Lexical |
| cooked broccoli | Brassica oleracea var. italica | `NCBITaxon:36774` | 47.47% | ncbitaxon | Lexical |

The EFO term for the first text is still found, but only by similarity of meaning and with a confidence that calls for review; the curated mapping is what made it certain. For the second text Zooma now proposes a food term rather than the compound the curator chose.

## Good to know

- A curated mapping was made for a purpose. *Cooked broccoli* was mapped to the compound *sulforaphane* because that was what mattered in the experiment being curated; in a dietary survey you would want a food term instead. Check that the term fits your use of the text.
- Curated mappings apply to the text as it was curated. A reworded or misspelt version of the same text is matched in other ways, usually with a lower confidence.
- Resources go by short names in the API and in the **Source** column, and by slightly different labels in section **2**: for example `atlas` is listed there as *ExpressionAtlas* and `ukbiobank` as *UKBiobank*.
- The choice of target ontologies still applies (see [ZOOMA-02](ZOOMA-02-choose-target-ontologies.md)). A curated mapping to a term in an ontology you have excluded is not suggested.

## See also

- [ZOOMA-05: Understand why Zooma suggested a term, choose a better one, and keep a record](ZOOMA-05-review-and-choose-alternative.md)
- [ZOOMA-01: Map a list of free-text values to ontology terms](ZOOMA-01-map-list-of-values.md)

*Checked against the live service on 5 October 2026. Suggestions change as curated mappings are added.*
