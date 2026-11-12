# 30 ZOOMA-04 (full)

- Captured: 2026-11-11T14:24:24.855Z
- DocBot message id: 13150
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-04-annotate-free-text.md

## Question

I have a sentence or paragraph — a sample description, a clinical note, part of a methods section. Which parts of it can be annotated with ontology terms, and with which terms?

## Answer

To annotate parts of a sample description, clinical note, or methods section, you can use [Zooma](https://www.ebi.ac.uk/spot/zooma) or [OLS](https://www.ebi.ac.uk/ols4).

### Using [Zooma](https://www.ebi.ac.uk/spot/zooma)

The “Annotate Text” tab in [Zooma](https://www.ebi.ac.uk/spot/zooma) identifies phrases within your text and suggests ontology terms for them based on a confidence score.

1. Navigate to the **Annotate Text** tab.
2. Paste your text into the input box.
3. Select your desired ontologies under **Which ontologies to map to?**. This step is critical, as your selection determines which phrases [Zooma](https://www.ebi.ac.uk/spot/zooma) identifies.
4. Click **Annotate Text**.

### Using [OLS](https://www.ebi.ac.uk/ols4)

The “Tag Text” feature in [OLS](https://www.ebi.ac.uk/ols4) highlights stretches of text that match existing term labels or previously curated mappings.

1. Navigate to the **Tag Text** page.
2. Paste or type your text into the box.
3. [OLS](https://www.ebi.ac.uk/ols4) will automatically highlight matches. You can view the results in the **Matched Terms** list, which provides the Term IRI, Term Label, Ontology, and Match Type (LABEL or CURATION).

### Determining which terms to use

- **Refine by Ontology:** If you receive too many matches, use the Ontologies panel to restrict your search to specific ontologies.
- **Manual Mapping:** If a specific word is not picked up, you can map it separately using the **Map Strings** tab in [Zooma](https://www.ebi.ac.uk/spot/zooma).
- **Search by Meaning:** If a concept is worded differently than its label, [OLS](https://www.ebi.ac.uk/ols4) will not find it automatically. In such cases, use the search functionality in [OLS](https://www.ebi.ac.uk/ols4) to search by meaning (using an embedding model) or browse the hierarchy to find a broader term that fits.

Would you like to know how to handle cases where no suitable ontology term can be found?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-04-annotate-free-text.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-06-tag-text.md
