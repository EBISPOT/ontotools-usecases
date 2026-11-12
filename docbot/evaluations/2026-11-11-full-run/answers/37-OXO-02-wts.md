# 37 OXO-02 (where-to-start)

- Captured: 2026-11-11T14:29:12.430Z
- DocBot message id: 13164
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-02-map-list-to-target.md

## Question

Where to start if I have many identifiers, and I want their equivalents in another vocabulary

## Answer

If you have a list of many identifiers and wish to find their equivalents in a target vocabulary, you should use [OxO](https://www.ebi.ac.uk/spot/oxo).

To map a list of identifiers to a target ontology:

- Open [OxO](https://www.ebi.ac.uk/spot/oxo) and select **Multiple terms**.
- Enter your identifiers (one per line) or upload a .txt, .csv, or .tsv file.
- In the **To ontologies** field, select your target vocabulary (e.g., ICD10CM).
- Leave the **From ontologies** field empty.
- You will receive a downloadable table of mappings. Through the [OxO](https://www.ebi.ac.uk/spot/oxo) API, you can also retrieve the list of inputs for which no equivalent was found.

If you are working with free-text values rather than identifiers, you should first use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map the text to a bridging ontology (such as MONDO) before using [OxO](https://www.ebi.ac.uk/spot/oxo) to translate those terms into your target vocabulary.

Would you like to know how to handle mappings that are not found by default in [OxO](https://www.ebi.ac.uk/spot/oxo)?

## Links in answer

- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-02-map-list-to-target.md
