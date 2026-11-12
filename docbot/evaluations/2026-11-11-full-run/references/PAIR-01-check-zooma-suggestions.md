# PAIR-01: Check Zooma's suggestions before you accept them

**Question:** Zooma has suggested a term for my value, but with a confidence below 90% — or it has suggested several. Is the suggestion right, and how do I check?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) to suggest terms; [OLS](https://www.ebi.ac.uk/ols4) to check what each suggested term means.

**You need:** a **Results** table in Zooma (see [ZOOMA-01](../zooma/ZOOMA-01-map-list-of-values.md)).

**You get:** for each doubtful suggestion, a decision — accept it, replace it or look elsewhere — based on the term's definition and its place in the ontology.

## Steps

### 1. Zooma — pick out the suggestions that need checking

1. In the **Results** table, look for the rows that are not green. Yellow rows have a confidence below 90%, or belong to a value with several high-confidence suggestions; grey rows have a low score.
2. For each such row, note the **Prediction Type**. An **Embedding** suggestion rests on similarity of meaning as judged by a language model, and deserves the closest look.

### 2. OLS — check what the suggested term means

3. Click the identifier in the **Term ID** column. The term opens in OLS in a new tab. (If OLS shows an error page instead — this happens for NCI Thesaurus terms, whose identifiers Zooma shows as `NCIT_C…` — paste the identifier into the OLS search box; see [OLS-02](../ols/OLS-02-look-up-identifier.md).)
4. Check four things on the term's page:
   - **Definition** — does it describe what your value means in your data?
   - **Synonyms** — is your wording, or something close to it, among them?
   - **Tree** — do the parent terms make sense? This is where you spot a term for the wrong kind of thing: an animal disease when your data are human, a measurement when you meant a disease, a symptom when you meant a diagnosis.
   - **Status** — a red box at the top saying **This class is deprecated** means the term is obsolete and should not be used (see [OLS-05](../ols/OLS-05-check-obsolete-term.md)).
5. If the term is close but too broad or too narrow, use the **Tree** to move to a child or a parent that fits better, and note its identifier.

### 3. Zooma — mark your decision, and write it down

6. Go back to the Zooma tab.
   - If the suggestion is right, click the **thumbs up** on its row.
   - If it is wrong, click the **thumbs down** to see Zooma's other candidates, and check any promising one in OLS in the same way before you select it and click **CONFIRM**.
   - If none of Zooma's candidates is right, look for a term yourself (see [PAIR-06](PAIR-06-find-term-when-zooma-cannot.md)).
7. Write each decision down outside Zooma — in the downloaded results file, or in a list of your own. The thumbs and the bin change only the table on the screen; they are not saved, and the downloaded file does not reflect them (see [ZOOMA-05](../zooma/ZOOMA-05-review-and-choose-alternative.md)).

### With the APIs

Take the `uri` of a candidate from Zooma's response and ask OLS for the term and its ancestors. OLS wants the IRI URL-encoded twice:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_1015393'
```

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_1015393/hierarchicalAncestors'
```

From the first response read `label`, `description`, `synonyms` and `is_obsolete`; the second lists the ancestors in `_embedded.terms`.

## Example

Three values mapped to Mondo (see [ZOOMA-02](../zooma/ZOOMA-02-choose-target-ontologies.md) for choosing the ontology):

| Text to Map | Zooma's suggestion | Confidence | Prediction Type |
|---|---|---|---|
| Alzheimers | *Alzheimer disease* `MONDO:0004975` | 84.61% | Embedding |
| broken leg | *fracture of pelvic limb tibia, non-human animal* `MONDO:1015393` | 75.14% | Embedding |
| sugar diabetes | *diabetes mellitus type 2 associated cataract* `MONDO:0005408` | 79.53% | Embedding |

All three are yellow, with similar scores. OLS tells them apart:

- **Alzheimers** — the definition and synonyms of `MONDO:0004975` fit. Accept.
- **broken leg** — in the **Tree**, `MONDO:1015393` sits under *bone fracture, non-human animal*, and further up under *non-human animal disease*. For human data this is the wrong term. Reject. Mondo's *bone fracture* (`MONDO:0005315`) is the nearest term for people; the Human Phenotype Ontology has the more specific *Fractured lower leg* (`HP:0041081`).
- **sugar diabetes** — the parent of `MONDO:0005408` is *cataract*: the term is an eye disease that is a complication of diabetes. Reject, and choose *diabetes mellitus* (`MONDO:0005015`) from Zooma's alternatives.

## Good to know

- A confidence score cannot tell a right suggestion from a wrong one that happens to be similar in wording or meaning. The three suggestions above scored between 75% and 85%; only one was right.
- Checking takes a minute per term. For a long list, check every row that is not green, and a sample of the green ones.
- Zooma's **Mapping Provenance** window (which is shown when you click on the value in the **Prediction Type** column of the 
mapping results table) shows what your text was matched against, which often explains a strange suggestion (see [ZOOMA-05](../zooma/ZOOMA-05-review-and-choose-alternative.md)).
- Keep a note of what you decided and why. It saves repeating the work when the same value turns up again.

## See also

- [ZOOMA-05: Understand why Zooma suggested a term, choose a better one, and keep a record](../zooma/ZOOMA-05-review-and-choose-alternative.md)
- [OLS-03: See where a term sits in the hierarchy](../ols/OLS-03-explore-hierarchy.md)
- [TRIO-01: Harmonise free-text values into ontology terms and codes](../three-tools/TRIO-01-harmonise-free-text-to-codes.md)

*Checked against the live services on 5 October 2026. Suggestions and confidences change as ontologies are updated.*
