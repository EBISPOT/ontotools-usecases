# 43 TRIO-02 (where-to-start)

- Captured: 2026-11-11T14:32:27.689Z
- DocBot message id: 13176
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-02-update-outdated-annotations.md

## Question

Where to start if I have old annotations, and I want current ones?

## Answer

To update outdated annotations, you should follow a three-step process, stopping at the first tool that provides a valid replacement for each term:

1. **[OLS](https://www.ebi.ac.uk/ols4):** Check if the term is obsolete and if the ontology explicitly names a replacement. Look up the term identifier with “Include obsolete terms” ticked. If the term page says “Replaced by,” you have found your successor.
2. **[OxO](https://www.ebi.ac.uk/spot/oxo):** If the ontology names no replacement, use [OxO](https://www.ebi.ac.uk/spot/oxo) to find a successor through mappings. Enter the identifier, tick “Obsolete terms” under “More options,” and search within your target ontologies.
3. **[Zooma](https://www.ebi.ac.uk/spot/zooma):** If the term remains unresolved, use [Zooma](https://www.ebi.ac.uk/spot/zooma) to find a successor based on the term’s wording. Use the original free-text value or the old term’s label (with any “obsolete” prefix removed) to map to your target ontologies.

After any of these steps, always verify the proposed replacement in [OLS](https://www.ebi.ac.uk/ols4) to ensure its definition fits your data. If a term remains unresolved after all three steps, it requires a manual decision.

Would you like to know how to use the API to automate these checks for multiple terms?

## Links in answer

- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-02-update-outdated-annotations.md
