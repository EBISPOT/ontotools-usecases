# 33 OLS-01 (where-to-start)

- Captured: 2026-11-11T14:26:11.188Z
- DocBot message id: 13156
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-01-find-term-for-concept.md

## Question

Where to start if I have a concept in words, and I want its ontology term?

## Answer

To find an ontology term for a concept described in words, you should start by using [OLS](https://www.ebi.ac.uk/ols4).

1. Open [OLS](https://www.ebi.ac.uk/ols4) and type your word or phrase into the “Search OLS…” box.
2. Press Enter or click Search to view the results.
3. You can narrow your results using the panel on the left:

- Under **Type**, tick “Class” to focus on ontology terms.
- Under **Ontology**, select the specific ontology you wish to use (e.g., MONDO for diseases).
4. Review the result cards, which provide the term’s label, identifier, definition, and the ontology it belongs to.
5. Click the label of the best match to confirm the definition and synonyms before using the term.

If you do not know the specific wording used by ontologies, you can perform a semantic search by selecting an embedding model (such as `llama-embed-nemotron-8b_pca512`) from the “Search Model” list in [OLS](https://www.ebi.ac.uk/ols4) instead of the default lexical search.

Would you like to know how to map these terms to other vocabularies using [OxO](https://www.ebi.ac.uk/spot/oxo)?

## Links in answer

- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-01-find-term-for-concept.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md
