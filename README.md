# ontotools-usecases
Here, we provide the different use cases realised by the ontology tools OLS, OxO, and Zooma. For each use case, we will describe it, state the tools necessary to realise it, and explain how the tool(s) can be used to do so.

## The tools

| Tool | What it does | Website | API |
|---|---|---|---|
| **OLS** — Ontology Lookup Service | Search, browse and look up the terms of more than 280 ontologies | <https://www.ebi.ac.uk/ols4> | `https://www.ebi.ac.uk/ols4/api` · [documentation](https://www.ebi.ac.uk/ols4/api-docs) |
| **OxO** | Find mappings between terms of different ontologies and coding systems | <https://www.ebi.ac.uk/spot/oxo> | `https://www.ebi.ac.uk/spot/oxo/api` · [documentation](https://www.ebi.ac.uk/spot/oxo/swagger-ui.html) |
| **Zooma** | Map free text to ontology terms | <https://www.ebi.ac.uk/spot/zooma> | `https://www.ebi.ac.uk/spot/zooma/v3/api` · [documentation](https://www.ebi.ac.uk/spot/zooma/docs) |

In short: **OLS** answers *what is this term?*, **Zooma** answers *which term fits this text?*, and **OxO** answers *what is this term called over there?*

## How a use case is written

Each use case is one file with the same parts:

- **Question** — what the user wants to know;
- **Tools** — the tool or tools that answer it;
- **Steps** — what to do, first on the website and then, where there is one, with the API;
- **Example** — the steps carried out on a real case, with the result;
- **Good to know** — limits, pitfalls and tips;
- **See also** — related use cases.

## Use cases

### OLS only

| ID | Question | Use case |
|---|---|---|
| OLS-01 | Which ontology term represents the concept I have in mind? | [Find the ontology term for a concept](use-cases/ols/OLS-01-find-term-for-concept.md) |
| OLS-02 | What does this identifier mean? | [Find out what an identifier means](use-cases/ols/OLS-02-look-up-identifier.md) |
| OLS-03 | What are the broader and narrower terms of this term? | [See where a term sits in the hierarchy](use-cases/ols/OLS-03-explore-hierarchy.md) |
| OLS-04 | Which ontologies cover my subject, and is this one suitable? | [Find an ontology for a domain and inspect it](use-cases/ols/OLS-04-find-and-inspect-ontology.md) |
| OLS-05 | Is this term still current, and if not, what replaces it? | [Check whether a term is obsolete and find its replacement](use-cases/ols/OLS-05-check-obsolete-term.md) |
| OLS-06 | Which ontology terms are mentioned in this text? | [Find the ontology terms mentioned in a text](use-cases/ols/OLS-06-tag-text.md) |
| OLS-07 | Which terms mean what I describe, in words I do not know? | [Find a term by meaning when you do not know the wording](use-cases/ols/OLS-07-semantic-search.md) |
| OLS-08 | How do I search within just one part of an ontology? | [Search only within one branch of an ontology](use-cases/ols/OLS-08-search-within-branch.md) |
| OLS-09 | How can my AI assistant look terms up instead of guessing? | [Let an AI assistant look up ontology terms](use-cases/ols/OLS-09-connect-ai-assistant.md) |

### OxO only

| ID | Question | Use case |
|---|---|---|
| OXO-01 | What is this term called in other ontologies and coding systems? | [Find equivalent terms in other ontologies](use-cases/oxo/OXO-01-find-equivalent-terms.md) |
| OXO-02 | What are the equivalents of my list of terms in one target, and which have none? | [Map a list of identifiers to one target ontology](use-cases/oxo/OXO-02-map-list-to-target.md) |
| OXO-03 | Which terms of one ontology correspond to terms of another? | [Get all the mappings between two ontologies](use-cases/oxo/OXO-03-all-mappings-between-ontologies.md) |
| OXO-04 | Who published this mapping, or how was it inferred? | [Check where a mapping comes from and how it was derived](use-cases/oxo/OXO-04-check-mapping-provenance.md) |
| OXO-05 | How do I keep only the mappings I am prepared to use? | [Keep only the mappings that meet your evidence requirements](use-cases/oxo/OXO-05-filter-by-evidence.md) |
| OXO-06 | Why did my search find nothing, and what is hidden? | [Find mappings when a search comes back empty](use-cases/oxo/OXO-06-search-returns-nothing.md) |
| OXO-07 | Where do OxO's mappings come from, and what is in a given set? | [See which mapping sets OxO holds and browse one](use-cases/oxo/OXO-07-browse-mapping-sets.md) |
| OXO-08 | This mapping is wrong — who published it, and whom do I tell? | [Find where an incorrect mapping came from](use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md) |

### Zooma only

| ID | Question | Use case |
|---|---|---|
| ZOOMA-01 | Which ontology term best matches each of my free-text values? | [Map a list of free-text values to ontology terms](use-cases/zooma/ZOOMA-01-map-list-of-values.md) |
| ZOOMA-02 | How do I get suggestions from the ontologies my project uses? | [Choose the ontologies Zooma maps to](use-cases/zooma/ZOOMA-02-choose-target-ontologies.md) |
| ZOOMA-03 | How do I get terms for a column of my spreadsheet? | [Annotate a column of a spreadsheet](use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md) |
| ZOOMA-04 | Which parts of this passage can be annotated, and with what? | [Find ontology terms in a passage of free text](use-cases/zooma/ZOOMA-04-annotate-free-text.md) |
| ZOOMA-05 | Why did Zooma suggest this term, and what else could it be? | [Understand why Zooma suggested a term, choose a better one, and keep a record](use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md) |
| ZOOMA-06 | Has a curator already mapped this text? | [Reuse mappings that curators have already made](use-cases/zooma/ZOOMA-06-reuse-curated-mappings.md) |

### Two tools together

| ID | Question | Tools | Use case |
|---|---|---|---|
| PAIR-01 | Is the term Zooma suggested the right one? | Zooma + OLS | [Check Zooma's suggestions before you accept them](use-cases/two-tools/PAIR-01-check-zooma-suggestions.md) |
| PAIR-02 | What is the term for this concept, and its code elsewhere? | OLS + OxO | [Find a term and get its code in another vocabulary](use-cases/two-tools/PAIR-02-find-term-and-translate.md) |
| PAIR-03 | Do two terms that are mapped to each other really mean the same? | OxO + OLS | [Decide whether two mapped terms really mean the same thing](use-cases/two-tools/PAIR-03-validate-a-mapping.md) |
| PAIR-04 | Which codes belong to a whole subject area? | OLS + OxO | [Build a code list for a disease area](use-cases/two-tools/PAIR-04-code-list-for-branch.md) |
| PAIR-05 | How do I get from free text to identifiers of one particular vocabulary? | Zooma + OxO | [Convert free-text values into identifiers of a specific vocabulary](use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md) |
| PAIR-06 | What do I do with a value Zooma cannot map? | Zooma + OLS | [Find a term by hand when Zooma cannot map a value](use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md) |

### All three tools together

| ID | Question | Use case |
|---|---|---|
| TRIO-01 | How do I turn a free-text column into ontology terms and codes I can rely on? | [Harmonise free-text values into ontology terms and codes](use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md) |
| TRIO-02 | Which of my old annotations are obsolete, and what replaces them? | [Bring outdated annotations up to date](use-cases/three-tools/TRIO-02-update-outdated-annotations.md) |
| TRIO-03 | How do I analyse a free-text dataset and a coded dataset together? | [Combine two datasets that describe the same things differently](use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md) |

## Where to start

| I have … | I want … | Start with |
|---|---|---|
| a concept in words | its ontology term | [OLS-01](use-cases/ols/OLS-01-find-term-for-concept.md), or [OLS-07](use-cases/ols/OLS-07-semantic-search.md) if I do not know the wording |
| an identifier | to know what it means | [OLS-02](use-cases/ols/OLS-02-look-up-identifier.md) |
| an identifier | its equivalent in another vocabulary | [OXO-01](use-cases/oxo/OXO-01-find-equivalent-terms.md) |
| many identifiers | their equivalents in another vocabulary | [OXO-02](use-cases/oxo/OXO-02-map-list-to-target.md) |
| many free-text values | ontology terms | [ZOOMA-01](use-cases/zooma/ZOOMA-01-map-list-of-values.md), then [PAIR-01](use-cases/two-tools/PAIR-01-check-zooma-suggestions.md) |
| many free-text values | codes of a coding system | [TRIO-01](use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md) |
| a passage of text | the terms mentioned in it | [OLS-06](use-cases/ols/OLS-06-tag-text.md) or [ZOOMA-04](use-cases/zooma/ZOOMA-04-annotate-free-text.md) |
| a mapping I am unsure of | a reason to trust it or not | [OXO-04](use-cases/oxo/OXO-04-check-mapping-provenance.md), then [PAIR-03](use-cases/two-tools/PAIR-03-validate-a-mapping.md) |
| a mapping I believe is wrong | to know who published it and where to report it | [OXO-08](use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md) |
| old annotations | current ones | [TRIO-02](use-cases/three-tools/TRIO-02-update-outdated-annotations.md) |
| two datasets annotated differently | one combined dataset | [TRIO-03](use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md) |

## Conventions used in the instructions

- **Identifiers.** A term has a full identifier, its IRI (`http://purl.obolibrary.org/obo/MONDO_0005068`), and a short form called a CURIE (`MONDO:0005068`). The part before the colon is the prefix and usually names the ontology. Some tools and files write the short form with an underscore (`MONDO_0005068`).
- **Names of things on screen** are in bold, as in **Search**. Text to type, identifiers and anything belonging to an API are in `code`.
- **API examples** use [`curl`](https://curl.se/), which is available on most systems. All the APIs return JSON unless stated otherwise; pipe the output through a tool such as [`jq`](https://jqlang.org/) to make it easier to read. None of the examples needs an account or a key.
- **IRIs in OLS addresses.** Where the OLS API takes an IRI as part of the path, the IRI must be URL-encoded twice: `http://purl.obolibrary.org/obo/MONDO_0005068` becomes `http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068`. Where an IRI is given as a parameter (after the `?`), it is encoded once.
- **Results change.** The examples were run against the live services on 5 October 2026. Ontologies in OLS are reloaded regularly, OxO publishes new data releases, and Zooma's suggestions follow both, so the counts, scores and sometimes the results you see will differ from those shown here. The steps stay the same.

## Reporting problems

If an instruction no longer matches what a tool shows, or a use case is missing, please open an issue in this repository. Problems with the tools themselves belong in the tools' own issue trackers: [OLS](https://github.com/EBISPOT/ols4/issues), [OxO](https://github.com/EBISPOT/oxo2/issues), [Zooma](https://github.com/EBISPOT/zooma2/issues).
