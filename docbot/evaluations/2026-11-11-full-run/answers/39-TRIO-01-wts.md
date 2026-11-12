# 39 TRIO-01 (where-to-start)

- Captured: 2026-11-11T14:29:30.550Z
- DocBot message id: 13168
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

## Question

Where to start if I have many free-text values, and I want codes of a coding system?

## Answer

To map many free-text values to codes from a coding system, you should follow a multi-step process using [Zooma](https://www.ebi.ac.uk/spot/zooma), [OLS](https://www.ebi.ac.uk/ols4), and [OxO](https://www.ebi.ac.uk/spot/oxo).

1. **Prepare your data:** Create a list of the unique values from your column (removing duplicates).
2. **Map to an ontology:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map your free-text values to terms in a “bridging” ontology (such as MONDO for diseases). This is necessary because [Zooma](https://www.ebi.ac.uk/spot/zooma) cannot suggest codes for systems like ICD-10-CM directly.
3. **Review and refine:** Check the suggestions provided by [Zooma](https://www.ebi.ac.uk/spot/zooma). Use [OLS](https://www.ebi.ac.uk/ols4) to verify doubtful suggestions, replace incorrect ones, and resolve terms that lack a code.
4. **Translate to codes:** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate the agreed-upon ontology terms into your target coding system (e.g., ICD10CM).
5. **Assemble:** Create a table containing the original value, the ontology term, and the final code, then join this back to your original dataset.

It is recommended to run a sample of your values through the first stage to estimate the amount of manual review required.

Would you like to know more about how to use the [Zooma](https://www.ebi.ac.uk/spot/zooma) API for this process?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo
- Zooma -> https://www.ebi.ac.uk/spot/zooma

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md
