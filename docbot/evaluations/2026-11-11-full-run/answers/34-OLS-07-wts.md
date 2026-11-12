# 34 OLS-07 (where-to-start)

- Captured: 2026-11-11T14:27:35.842Z
- DocBot message id: 13158
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md

## Question

Where to start if I have a concept in mind, without knowing the correct words, and I want its ontology term?

## Answer

To find an ontology term for a concept when you do not know the correct terminology, you should use the [OLS](https://www.ebi.ac.uk/ols4) semantic search feature:

1. Open [OLS](https://www.ebi.ac.uk/ols4).
2. Type your phrase into the **Search OLS…** box.
3. Open the **Search Model** list under the search box and select an embedding model (e.g., `llama-embed-nemotron-8b_pca512`) instead of the default Lexical option.
4. Click **Search**. The results will be ranked by how similar their meaning is to your phrase, with a similarity score displayed next to each label.

Always read the definition of the term you select, as these results are computed from language-model embeddings and have not been curated.

Would you like to know how to filter these results by specific ontologies?

## Links in answer

- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md
