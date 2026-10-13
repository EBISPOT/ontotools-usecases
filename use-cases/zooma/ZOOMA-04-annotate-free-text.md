# ZOOMA-04: Find ontology terms in a passage of free text

**Question:** I have a sentence or paragraph — a sample description, a clinical note, part of a methods section. Which parts of it can be annotated with ontology terms, and with which terms?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) (the **Annotate Text** tab)

**You need:** the text, and the ontologies you want terms from.

**You get:** the phrases Zooma picked out of the text, and suggested terms for each phrase with a confidence.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/zooma> and click the **Annotate Text** tab under **1 Enter strings to map**.
2. Paste or type your text into the box.
3. Choose the ontologies to annotate with: open **3 Which ontologies to map to?**, select **Choose custom ontologies** and add the ontologies you want (see [ZOOMA-02](ZOOMA-02-choose-target-ontologies.md)). This step matters more here than anywhere else, because the ontologies you choose decide which phrases Zooma picks out.
4. Click the green **Annotate Text** button.
5. Read the text that Zooma shows above the results. The phrases it picked are shown as rounded labels, coloured by their best suggestion: green for a confidence of 90% or more, yellow for something to check, grey for a low score or no suggestion.
6. Read the **Results** table beneath it. It has one or more rows per phrase, with the same columns as when you map a list (see [ZOOMA-01](ZOOMA-01-map-list-of-values.md)).
7. Click a phrase in the text to highlight its rows in the table and scroll to them. Click it again to remove the highlight.
8. Click the **×** on a phrase to discard it, together with its rows — for example where Zooma picked out a word that is of no interest to you.
9. Click the download icon next to the **Results** heading to save the suggestions as `zooma_results.tsv`.

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/annotate-text-stream' \
  -H 'Content-Type: application/json' \
  -d '{
        "text": "Liver biopsy from a patient with type 2 diabetes mellitus and prior myocardial infarction.",
        "targetOntologies": ["mondo", "uberon", "efo"],
        "includeOtherOntologies": false
      }'
```

The response is a stream of lines, each a small JSON document with a `type`:

- `segments` — the phrases picked out, each with its `text` and its `start` and `end` position in your text;
- `result` — the suggestions for one phrase, in the same form as a `mappings` entry in [ZOOMA-01](ZOOMA-01-map-list-of-values.md);
- `ping` — a keep-alive that you can ignore;
- `done` — the end of the stream.

## Example

Text: *Liver biopsy from a patient with type 2 diabetes mellitus and prior myocardial infarction.*

With the custom ontologies Mondo, Uberon and EFO, Zooma picks out three phrases:

| Phrase | Suggested term | Confidence |
|---|---|---|
| type 2 diabetes mellitus | *type 2 diabetes mellitus* `MONDO:0005148` | 100% |
| myocardial infarction | *myocardial infarction* `MONDO:0005068` | 100% |
| biopsy | *biopsy site* `EFO:0000288` (curated); *biopsy* `EFO:0009120` | 100% each |

Above the table, the sentence is shown as: Liver **[biopsy ×]** from a patient with **[type 2 diabetes mellitus ×]** and prior **[myocardial infarction ×]**. — the three phrases as green labels.

With the broad preset that Zooma starts with, the same text is split differently — into *Liver biopsy*, *patient*, *type 2*, *myocardial* and *infarction* — and the two diseases are missed. Choosing ontologies that fit the text makes the difference.

## Good to know

- If you paste a long line (more than 30 words) into the **Map Strings** tab, Zooma switches to **Annotate Text** for you.
- A phrase with two green suggestions, like *biopsy* above, needs a decision from you (see [ZOOMA-05](ZOOMA-05-review-and-choose-alternative.md)).
- Not every word you care about will be picked out. Here *Liver* was not. Map such words separately on the **Map Strings** tab.
- Ignore the count in the **Results** heading in this mode. If one is shown (*n out of m mapped*), the *m* is left over from the last list you mapped on the **Map Strings** tab.
- OLS has a simpler text tagger that marks every stretch of text matching a term label, in any ontology, without ranking (see [OLS-06](../ols/OLS-06-tag-text.md)). Use OLS when you want to see everything that matches, and Zooma when you want one ranked suggestion per phrase.

## See also

- [OLS-06: Find the ontology terms mentioned in a text](../ols/OLS-06-tag-text.md)
- [ZOOMA-02: Choose the ontologies Zooma maps to](ZOOMA-02-choose-target-ontologies.md)

*Checked against the live service on 5 October 2026. Suggestions change as ontologies are updated.*
