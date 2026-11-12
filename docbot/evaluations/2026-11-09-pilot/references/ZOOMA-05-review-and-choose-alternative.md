# ZOOMA-05: Understand why Zooma suggested a term, choose a better one, and keep a record

**Question:** Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma)

**You need:** a **Results** table in Zooma (see [ZOOMA-01](ZOOMA-01-map-list-of-values.md)).

**You get:** the reasoning behind each suggestion, the full list of alternatives, and a record of your decisions that outlasts the page.

## What the review controls do — and do not do

Each row of the **Results** table ends with three icons: a thumbs up (**Approve**), a thumbs down (**Select alternative mapping**) and a bin (**Remove row**). They help you work through the table, but they change only what is on the screen:

- they are not saved: reload the page and they are gone;
- they are not sent to Zooma, so they do not improve its future suggestions;
- the file you get from the download icon does not reflect them. It always contains the suggestions Zooma first returned — approved or not, replaced or not, removed or not — and a replacement that you picked from the list of alternatives is not in it at all. This is a known limitation, recorded as [zooma2 issue #52](https://github.com/EBISPOT/zooma2/issues/52).

So use the icons to keep track of where you are, and keep the record of your decisions yourself. The steps below show one way to do that.

## Steps

### On the website

1. Click the download icon next to the **Results** heading (**Download as TSV**) and open `zooma_results.tsv` in a spreadsheet. This is your working file: one row per suggestion, with the value (`textToMap`), the suggested term (`ontologyTermLabel`, `ontologyTermID`, `ontologyURI`), its confidence and its source. Add a column for your decision.
2. In the **Results** table on the website, find the rows that need a look — start with the ones that are not green.
3. Read the **Prediction Type** column. It tells you how the suggestion was found:
   - **Curated** — a curator at a data resource mapped this very text to this term before;
   - **Lexical** — the text matches the term's label or a synonym, wholly or in part;
   - **Embedding** — the text and the term are close in meaning according to a language model, though their wording differs;
   - **Replace obsolete** — the match was to an obsolete term, and Zooma substituted the term that replaces it.
4. Click the value in the **Prediction Type** column. The **Mapping Provenance** window lists the steps that led to the suggestion: for each step the **Method**, the **Match Type**, the **Input** text, the **Matched Text** (what your text was matched against), the **Target** term, the **Source** and, for embedding matches, the **Model**. For an embedding match, **Match Type** gives the similarity between your text and the matched text (for example *95% similar*); this is not the same number as the confidence in the table, which is lower.
5. Click the identifier in the **Term ID** column to open the term in OLS and read its definition and its place in the hierarchy (see [PAIR-01](../two-tools/PAIR-01-check-zooma-suggestions.md)).
6. Decide, mark the decision on the screen, and write it in your working file:

   | Your decision | On the screen | In your working file |
   |---|---|---|
   | the suggestion is right | click the **thumbs up**: the row turns green and the other suggestions for the same value are hidden (click again to undo) | mark the row as accepted; delete the value's other rows |
   | the suggestion is wrong, but one of Zooma's alternatives is right | click the **thumbs down**: after a few seconds the window **Select Mapping for "…"** lists every candidate Zooma can find, best first, with **Term Label**, **Confidence**, **Term ID**, **Source** and **Prediction Type**, the current suggestion selected; select the right one and click **CONFIRM**, and it replaces the row and is marked approved | copy the chosen term's label, identifier and IRI from the window into the value's row — the file does not contain the alternatives |
   | the suggestion is not needed | click the **bin**: the row disappears | delete the row |
   | nothing Zooma offers is right | — | mark the value as unresolved and find a term by hand (see [PAIR-06](../two-tools/PAIR-06-find-term-when-zooma-cannot.md)) |

7. When you have been through the table, your working file holds one row per value with the term you settled on and a decision against it. Keep it, with the date and the settings you used; it is the record, and the quickest way to map the same values next time.

### With the API

Every candidate in the response carries its reasoning in `mappingProvenance`: a list of steps, each with a `method` (`curated`, `lexical`, `semantic` or `cross_reference`), a `matchType`, the `input`, the `matchedText`, the `target` and the `source`.

To get the long list of alternatives rather than the short list of best suggestions, add `"returnAll": true` and `"deep": true`:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [{"textToMap": "sugar diabetes"}],
        "targetOntologies": ["mondo"],
        "includeOtherOntologies": false,
        "returnAll": true,
        "deep": true
      }'
```

This is slower than an ordinary request. With the API, recording decisions is up to your own code in any case: keep the candidate you choose, not the whole response.

## Example

Mapping `sugar diabetes` to Mondo gives one suggestion: *diabetes mellitus type 2 associated cataract* (`MONDO:0005408`), 79.53%, **Embedding** — a yellow row.

- **Mapping Provenance** shows a single step: method *Embedding*, matched text *diabetes mellitus type 2 associated cataract*. So the suggestion rests on similarity of meaning alone, and the term's label says it is an eye disease. It is not what was meant.
- **Thumbs down** opens a long list of alternatives, nearly all of them kinds of diabetes. Near the top are *type 2 diabetes mellitus* (`MONDO:0005148`), *diabetes mellitus* (`MONDO:0005015`) and *type 1 diabetes mellitus* (`MONDO:0005147`).
- "Sugar diabetes" does not say which type, so *diabetes mellitus* (`MONDO:0005015`) is the right choice — even though it is not the highest-scoring candidate. Select it and click **CONFIRM**. On the screen the row now reads *diabetes mellitus*, `MONDO:0005015`, in green.
- In the working file, the row for `sugar diabetes` still says `MONDO_0005408`, and will do so however often you download. Overwrite it with `MONDO_0005015`, *diabetes mellitus*, `http://purl.obolibrary.org/obo/MONDO_0005015`, and note *chosen from alternatives*.

## Good to know

- The limitation above may be lifted; check [zooma2 issue #52](https://github.com/EBISPOT/zooma2/issues/52) for its status. Until then, a download made after reviewing is no different from one made before.
- Because your choices are not fed back, Zooma will make the same suggestion for the same value next time. Your working file is what prevents the work being done twice.
- A **Curated** suggestion reflects a person's earlier decision about the same text, usually in the context of one data resource. It is strong evidence, but check that the context matches yours (see [ZOOMA-06](ZOOMA-06-reuse-curated-mappings.md)).
- A **Lexical** match on part of the text can land on a narrower or a different concept. Read the **Matched Text** to see what was matched.
- A high confidence on the wrong term is possible, and so is a modest confidence on the right one. The score orders the candidates; it does not replace your judgement.

## See also

- [PAIR-01: Check Zooma's suggestions before you accept them](../two-tools/PAIR-01-check-zooma-suggestions.md)
- [ZOOMA-01: Map a list of free-text values to ontology terms](ZOOMA-01-map-list-of-values.md)
- [ZOOMA-02: Choose the ontologies Zooma maps to](ZOOMA-02-choose-target-ontologies.md)

*Checked against the live service on 7 October 2026. Suggestions and confidences change as ontologies are updated.*
