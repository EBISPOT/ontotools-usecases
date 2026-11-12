# 42 OXO-08 (where-to-start)

- Captured: 2026-11-11T14:31:17.825Z
- DocBot message id: 13174
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md

## Question

Where to start if I have a mapping I believe is wrong, and I want to know who published it and where to report it?

## Answer

To identify the source of a mapping and determine where to report an error, you should start by opening the mapping’s details page in [OxO](https://www.ebi.ac.uk/spot/oxo).

1. **Locate the mapping:** Find the mapping in your results table. If the row indicates “Multiple sets,” click the expand arrow to view the individual members.
2. **Open details:** Click the eye icon (“View mapping details”) for the specific mapping you believe is incorrect.
3. **Identify the source:** Look at the “Mapping Set” section on the details page.

- **Asserted mappings:** The Mapping Set section identifies the project that published the set. You should report the error to that project.
- **Inferred mappings:** If the mapping is an [OxO](https://www.ebi.ac.uk/spot/oxo) inference, the error lies in one of the underlying asserted mappings. Use the “Asserted Mappings” table under “Inference Details” to identify the specific premise that is incorrect, then report it to the publisher of that premise.
4. **Report the error:** When reporting, provide the address of the details page, the subject and object with their labels, the predicate, the mapping set identifier, and a clear explanation of why the mapping is wrong (including the two definitions).

If the mapping is asserted, you can often find the reporting contact via the project’s website or, if the mapping is an ontology cross-reference, via the Issue Tracker button on the ontology’s page in [OLS](https://www.ebi.ac.uk/ols4).

Would you like to know how to filter out incorrect mappings from your results while you wait for a correction?

## Links in answer

- OxO -> https://www.ebi.ac.uk/spot/oxo
- OxO -> https://www.ebi.ac.uk/spot/oxo
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md
