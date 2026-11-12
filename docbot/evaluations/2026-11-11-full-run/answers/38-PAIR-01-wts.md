# 38 PAIR-01 (where-to-start)

- Captured: 2026-11-11T14:29:21.491Z
- DocBot message id: 13166
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md

## Question

Where to start if I have many free-text values, and I want ontology terms?

## Answer

To map a list of free-text values to ontology terms, you should start by using [Zooma](https://www.ebi.ac.uk/spot/zooma).

For a large number of values, it is recommended to first remove duplicates so that each unique value is mapped only once, which is more efficient. You can then process these values using the following steps:

- **Prepare your data:** If your values are in a spreadsheet, save or export the file as a CSV or TSV. If you have a simple list, you can paste the values directly into the [Zooma](https://www.ebi.ac.uk/spot/zooma) website, one per line.
- **Configure mapping:** Open the [Zooma](https://www.ebi.ac.uk/spot/zooma) website and navigate to the mapping interface. It is recommended to select “Choose custom ontologies” under the “Which ontologies to map to?” section to ensure [Zooma](https://www.ebi.ac.uk/spot/zooma) performs better by focusing on specific, relevant ontologies rather than searching all available ones.
- **Review results:** Once [Zooma](https://www.ebi.ac.uk/spot/zooma) provides suggestions, you should review them. You can use [OLS](https://www.ebi.ac.uk/ols4) to check the definitions, synonyms, and parent terms of suggested candidates to verify their accuracy.
- **Handle unmapped values:** If [Zooma](https://www.ebi.ac.uk/spot/zooma) cannot find a suitable term, you can search [OLS](https://www.ebi.ac.uk/ols4) manually using technical names, synonyms, or by browsing the hierarchy of a broader term.

Would you like to know more about how to use [OLS](https://www.ebi.ac.uk/ols4) to verify these suggestions?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-01-map-list-of-values.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md
