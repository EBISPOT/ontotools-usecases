# 41 PAIR-03 (where-to-start)

- Captured: 2026-11-11T14:31:08.768Z
- DocBot message id: 13172
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md

## Question

Where to start if I have a mapping I am unsure of, and I want a reason to trust it or not?

## Answer

To determine if you can trust a mapping, you should start by examining its evidence and provenance within [OxO](https://www.ebi.ac.uk/spot/oxo). Follow these steps:

- **View Mapping Details:** In your [OxO](https://www.ebi.ac.uk/spot/oxo) results table, click the eye icon at the end of the row to open the Mapping Details page.
- **Check the Type:**

- If the mapping is **Asserted**, it was published by a project. Note who published it and how it was made under the Mapping Set section.
- If the mapping is an **SSSOM inference**, it was derived by [OxO](https://www.ebi.ac.uk/spot/oxo). Review the “Asserted Mappings” it rests on to identify the weakest link, such as mappings made by automatic label matching or those between terms with differing labels.
- **Compare Terms:** Use [OLS](https://www.ebi.ac.uk/ols4) to compare the two terms. Check their definitions, synonyms, and hierarchical positions to decide if they truly mean the same thing.
- **Evaluate Justification:** Look at the “Mapping justification” column. Be cautious of “LexicalMatching” (automatic label matching) or “MappingChaining,” as these often require closer scrutiny.
- **Assess Distance:** In inferred mappings, the “Distance” indicates how many ontologies an inference passes through; shorter derivations are generally safer.

Would you like to know how to filter your [OxO](https://www.ebi.ac.uk/spot/oxo) results to exclude mappings that do not meet your evidence requirements?

## Links in answer

- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-04-check-mapping-provenance.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md
