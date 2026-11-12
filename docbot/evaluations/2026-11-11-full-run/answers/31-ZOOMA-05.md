# 31 ZOOMA-05 (full)

- Captured: 2026-11-11T14:25:53.062Z
- DocBot message id: 13152
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md

## Question

Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

## Answer

To understand why [Zooma](https://www.ebi.ac.uk/spot/zooma) suggested a specific term, click on the value in the “Prediction Type” column of the mapping results table to open the Mapping Provenance window. This window displays what your text was matched against, which often explains the reasoning behind a suggestion.

If the suggested term is incorrect, you can find alternatives by clicking the “thumbs down” icon on the row. This opens the “Select Mapping” window, which lists every candidate [Zooma](https://www.ebi.ac.uk/spot/zooma) found, ordered by confidence. You can review these candidates in [OLS](https://www.ebi.ac.uk/ols4) to check their definitions, synonyms, and hierarchy to determine if a better fit exists.

To keep a record of your decisions:

- **Do not rely on the website icons:** The thumbs up, thumbs down, and bin icons only change the display on your screen; they are not saved, are not sent to [Zooma](https://www.ebi.ac.uk/spot/zooma), and are not reflected in the downloaded results file.
- **Maintain a working file:** Download your results as a TSV file and add a column to record your decisions, the date, and the settings used. This file serves as your permanent record and allows you to quickly map the same values in the future.

Would you like to know more about using the [Zooma](https://www.ebi.ac.uk/spot/zooma) API to retrieve mapping provenance?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md
