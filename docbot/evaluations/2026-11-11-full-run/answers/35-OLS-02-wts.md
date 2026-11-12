# 35 OLS-02 (where-to-start)

- Captured: 2026-11-11T14:27:45.401Z
- DocBot message id: 13160
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-02-look-up-identifier.md

## Question

Where to start if I have an identifier, and I want to know what it means?

## Answer

To find out what an identifier means, you should use [OLS](https://www.ebi.ac.uk/ols4). You can provide the identifier in any of the following formats:

- A CURIE (e.g., MONDO:0005068)
- The underscore form (e.g., MONDO_0005068)
- The full IRI (e.g., [http://purl.obolibrary.org/obo/MONDO_0005068](http://purl.obolibrary.org/obo/MONDO_0005068))

To look it up on the website:

1. Open [OLS](https://www.ebi.ac.uk/ols4).
2. Paste the identifier into the “Search OLS…” box.
3. In the drop-down, look under “Jump to” and click the entry for the term. If the term is listed multiple times, choose the entry whose ontology badge matches the identifier’s prefix. Alternatively, press Enter and open the result that is not marked “IMPORTED.”
4. Review the term’s label, definition, synonyms, cross-references, and relations on the resulting page.

If you are using the API, you can search for the identifier using the following endpoint:

`curl -s 'https://www.ebi.ac.uk/ols4/api/terms?obo_id=YOUR_IDENTIFIER'`

Would you like to know how to handle cases where a search for an identifier returns no results?

## Links in answer

- OLS -> https://www.ebi.ac.uk/ols4
- http://purl.obolibrary.org/obo/MONDO_0005068 -> http://purl.obolibrary.org/obo/MONDO_0005068
- OLS -> https://www.ebi.ac.uk/ols4

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-02-look-up-identifier.md
