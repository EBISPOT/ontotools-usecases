# 44 TRIO-03 (where-to-start)

- Captured: 2026-11-11T14:32:37.256Z
- DocBot message id: 13178
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md

## Question

Where to start if I have two datasets annotated differently, and I want one combined dataset?

## Answer

To combine two datasets that describe the same things differently, you should first bring both datasets to a common set of terms using a shared ontology. You can achieve this by following these steps:

- **Choose a common ontology:** Use [OLS](https://www.ebi.ac.uk/ols4) to browse and select an ontology (such as Mondo) that covers the subject matter of both datasets and is well-connected to the coding systems you are using.
- **Process the free-text dataset:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map the unique free-text values to terms from your chosen ontology. You should check any uncertain suggestions in [OLS](https://www.ebi.ac.uk/ols4) before accepting them.
- **Process the coded dataset:** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate your existing codes into terms from the same common ontology.
- **Group the terms:** Once both datasets are mapped to the same ontology, use [OLS](https://www.ebi.ac.uk/ols4) to identify the hierarchy and broader groups for your terms. This allows you to group records at a level that separates the categories you care about.
- **Combine:** Add the common term and the broader group to every record in both datasets. Records sharing the same term represent the same entity, while records sharing the same group belong together at a broader level.

Would you like to know more about using the [Zooma](https://www.ebi.ac.uk/spot/zooma) or [OxO](https://www.ebi.ac.uk/spot/oxo) APIs for this process?

## Links in answer

- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OxO -> https://www.ebi.ac.uk/spot/oxo

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md
