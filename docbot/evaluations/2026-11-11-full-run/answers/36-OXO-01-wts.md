# 36 OXO-01 (where-to-start)

- Captured: 2026-11-11T14:27:53.962Z
- DocBot message id: 13162
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-01-find-equivalent-terms.md

## Question

Where to start if I have an identifier, and I want its equivalent in another vocabulary?

## Answer

To find the equivalent of an identifier in another vocabulary, you should use [OxO](https://www.ebi.ac.uk/spot/oxo).

You can perform this mapping using the [OxO](https://www.ebi.ac.uk/spot/oxo) website or its API:

- **On the website:** Open [OxO](https://www.ebi.ac.uk/spot/oxo), enter your identifier into the “Which term do you want to map?” field, and select your desired target vocabularies in the “To ontologies” section.
- **With the API:** You can use a POST request to the `https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search` endpoint.

When reviewing the results, prefer rows marked as “Asserted” with the predicate `SKOS:exactMatch`. If a row is marked as an “SSSOM inference,” it is derived, and you should inspect it further before use. Note that prefixes in [OxO](https://www.ebi.ac.uk/spot/oxo) may differ from standard expectations (e.g., SNOMED CT is `SCTID` and ICD-10-CM is `ICD10CM`).

Would you like to know how to handle cases where [OxO](https://www.ebi.ac.uk/spot/oxo) returns no results for your identifier?

## Links in answer

- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-06-search-returns-nothing.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-01-find-equivalent-terms.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-02-find-term-and-translate.md
