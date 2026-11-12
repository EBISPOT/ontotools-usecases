# DocBot full run — 11 November 2026

Result: **40 thumbs up, 4 thumbs down** across all 44 questions of `docbot/Ontotools-docbot.tsv` (32 full use-case questions and 12 "Where to start" questions). Every question was asked verbatim in a new conversation, every answer completed, and every answer cited at least one use case as its source. **No ratings or comments were submitted to DocBot in this run**; the proposed rating and feedback text for each answer are in [`evaluation-log.json`](evaluation-log.json) and in the records below, ready to submit if wanted.

Target: https://wwwdev.ebi.ac.uk/docbot/?selected=ontology_tools

Reference: local branch `dev`, commit `773bf7c131b2426ee78fae9bb38073f408530dcd`, the same commit as the three earlier pilots; no tracked modifications to `use-cases/`, `README.md` or the TSV. Copies and SHA-256 checksums of the 32 use-case documents are in [`references/`](references/). Remote freshness and the deployed DocBot version were not verified.

Method: each question was typed into the chat box, the answer was captured from the page once the rating buttons appeared and the text had stopped changing, and **New conversation** was used before the next question. Captures are in [`answers/`](answers/) (one Markdown file per question, with message id, links and sources) and [`captures.json`](captures.json). Each answer was then compared with its use-case document and with the TSV's expected output. A thumbs up means the answer is accurate against the repository and gives the user the procedure or guidance the use case is about; a thumbs down means it contains a misleading statement or leaves out the core of the use case. The finer verdict is *pass* (accurate and sufficient), *partial* (accurate but with a notable omission) or *fail* (does not answer the use case). No follow-up prompts were used. The ontology services, API examples and link destinations were not independently exercised. Interface observations are in [`interface-notes.md`](interface-notes.md).

| | Thumbs up | Thumbs down | Pass | Partial | Fail |
|---|---|---|---|---|---|
| Full questions (32) | 28 | 4 | 24 | 7 | 1 |
| Where to start (12) | 12 | 0 | 11 | 1 | 0 |
| All (44) | 40 | 4 | 35 | 8 | 1 |

## Summary of all answers

| # | Use case | Variant | Rating | Verdict | Finding |
|---|---|---|---|---|---|
| 01 | OLS-01 | full | 👎 | fail | Answers the example, not the question: names myocardial infarction (MONDO:0005068) correctly but gives no procedure for finding a term for a concept. |
| 02 | OLS-02 | full | 👎 | partial | Correct label, definition and synonyms for the example identifier, but no lookup procedure for an identifier in general. |
| 03 | OLS-03 | full | 👍 | partial | Example facts (parent, 14 children, 20 descendants, example children) all match the use case; points to the Tree panel but gives little method and no API. |
| 04 | OLS-04 | full | 👍 | pass | Accurate: Ontologies page, category and text filters, where scope, version, size and licence are shown, and the two API calls with the right fields. |
| 05 | OLS-05 | full | 👍 | pass | Identical to the 9 November answer; accurate on Include obsolete terms, the deprecated box, term replaced by, API fields and the OxO/Zooma fallback. |
| 06 | OLS-06 | full | 👍 | partial | Correct tool (Tag Text), correct inputs and result columns, and a correct contrast with Zooma Annotate Text; omits the ontology filter, match-length controls, CSV download and API. |
| 07 | OLS-07 | full | 👍 | partial | Correct answer (Tinnitus HP:0000360) and correct embedding-search steps; omits the caveat that scores are uncurated and the definition must be checked. |
| 08 | OLS-08 | full | 👍 | pass | Accurate and complete: childrenOf on select/search, single URL-encoding, the exact example call, allChildrenOf, type=class, obsoletes=true, and that the website has no branch filter. |
| 09 | OLS-09 | full | 👍 | pass | Accurate: MCP address, Streamable HTTP, no authentication, Claude Code example, the twelve tools, example prompt, verification advice and the embedding-model tools. |
| 10 | OXO-01 | full | 👍 | pass | Accurate website and API procedure with the right target prefixes (MESH, ICD10CM, SCTID) and sound advice to prefer asserted exact matches. |
| 11 | OXO-02 | full | 👍 | pass | Accurate: Multiple terms mode, file upload, To ontologies, Asserted only filter, SSSOM download, Subject-column comparison, and the batch-map API with unmappedInputs. |
| 12 | OXO-03 | full | 👍 | pass | Accurate: empty term box, From/To, download as SSSOM, the exact API command for the file, and the folding explanation for row/line count differences. |
| 13 | OXO-04 | full | 👍 | pass | Identical to the 9 November answer; accurate on asserted vs inferred, Mapping Details sections, Inference Details, judging by the weakest premise and fitness for purpose. |
| 14 | OXO-05 | full | 👍 | pass | Accurate column filters (Type, Predicate, Mapping justification, Distance, Object), clear-filter behaviour, and the matching API fields. |
| 15 | OXO-06 | full | 👍 | pass | Accurate: what OxO hides by default, the three Also show options under More options, and the direction, label-matching and prefix checks. |
| 16 | OXO-07 | full | 👍 | pass | Accurate: the two kinds of mapping set plus OxO's inference set, the picker under More options, set pages, and the mapping-sets and mappingSetIds API calls. |
| 17 | OXO-08 | full | 👍 | pass | Accurate tracing of asserted and inferred mappings to their source, correct reporting routes (project, OLS Issue Tracker for extracted cross-references, premise publisher) and report contents. |
| 18 | TRIO-01 | full | 👎 | partial | Identical to the 9 November answer. The five-stage workflow is right, but the reliability safeguards the question asks for are still incomplete: broader parent codes are not flagged as broader, inferred mappings are validated too loosely, unresolved values are not left for manual coding, and choosing between several asserted codes is missing. |
| 19 | TRIO-02 | full | 👍 | pass | Accurate three-step order (OLS, then OxO with Obsolete terms ticked, then Zooma from the wording), with the final OLS check and the manual-decision fallback. |
| 20 | TRIO-03 | full | 👍 | pass | Accurate overall workflow, and gets the key OxO detail right: codes written as prefix:code and Max distance 1 for direct mappings into the common ontology. |
| 21 | PAIR-01 | full | 👍 | pass | Accurate review loop: Mapping Provenance, Term ID into OLS for definition, synonyms and hierarchy, thumbs-down alternatives checked the same way, and decisions recorded outside Zooma. |
| 22 | PAIR-02 | full | 👎 | partial | Answers the example only: the term and the three asserted codes match the use case exactly, but the OLS half of the workflow is absent and the OxO half is a bare pointer. |
| 23 | PAIR-03 | full | 👍 | pass | More complete than on 9 November: evidence columns and Mapping Details, five-point OLS comparison, accept/downgrade/reject with no merging on a downgrade, and the reporting route. |
| 24 | PAIR-04 | full | 👍 | pass | Accurate: top term (MONDO:0005015), Tree check, API descendants for large branches, OxO Multiple terms with Asserted only and download, and both fallbacks for terms without a code. |
| 25 | PAIR-05 | full | 👍 | pass | Accurate two-step workflow with the right details (custom bridging ontology, carry forward only accepted suggestions, underscore to colon, Asserted only) and a sensible parent-code fallback. |
| 26 | PAIR-06 | full | 👍 | pass | Accurate OLS search ladder (words, other words, meaning, browse), verification advice, and both no-term outcomes (broader term with original text kept; request via Issue Tracker). |
| 27 | ZOOMA-01 | full | 👍 | partial | Correct input procedure (Map Strings, one per line, Tab for the kind, Map N strings) but says little about reading the results and nothing about download or the limits of the confidence score. |
| 28 | ZOOMA-02 | full | 👍 | pass | Accurate: custom ontology list in order of preference, the API example, single answer with an ordered list, and the default state of Include results from other ontologies. |
| 29 | ZOOMA-03 | full | 👍 | pass | Accurate: export as CSV/TSV, Upload CSV, the preview settings, Term and Type columns, Import then Map, download and join on textToMap and propertyType, deduplicate first. |
| 30 | ZOOMA-04 | full | 👍 | pass | Accurate on both tools: Annotate Text with the ontology choice flagged as critical, OLS Tag Text with its result columns, and sensible advice for words not picked up. |
| 31 | ZOOMA-05 | full | 👍 | pass | Identical to the 9 November answer; accurate on Mapping Provenance, alternatives via thumbs down, OLS checks, and the warning that screen decisions are neither saved nor in the download. |
| 32 | ZOOMA-06 | full | 👍 | pass | Accurate: curated mappings and their Source, the Where to get mappings controls (exclude, include, reorder), the filter.required / filter.preferred API, and the excluded-ontology caveat. |
| 33 | OLS-01 | where-to-start | 👍 | pass | Full and accurate procedure: search box, Type = Class, Ontology filter, result cards, confirm definition and synonyms, semantic search as alternative. |
| 34 | OLS-07 | where-to-start | 👍 | pass | Accurate embedding-search steps with the uncurated-results caveat. |
| 35 | OLS-02 | where-to-start | 👍 | pass | Accurate: identifier forms, Jump to with matching ontology badge or the non-IMPORTED result, what to read on the page, API call. |
| 36 | OXO-01 | where-to-start | 👍 | pass | Correct tool and entry points, with the asserted-exact-match preference and the prefix note. |
| 37 | OXO-02 | where-to-start | 👍 | pass | Correct: Multiple terms mode, To ontologies, From empty, download, API reports unmapped inputs; sensible pointer to Zooma for free text. |
| 38 | PAIR-01 | where-to-start | 👍 | partial | Answers along the expected path (Zooma first, review doubtful suggestions in OLS, handle unmapped values) but omits recording decisions outside Zooma and the deprecated-status check; cites the Zooma use cases and TRIO-01 rather than PAIR-01. |
| 39 | TRIO-01 | where-to-start | 👍 | pass | Correct overview of the five stages, including why a bridging ontology is needed and the advice to run a sample first. |
| 40 | ZOOMA-04 | where-to-start | 👍 | pass | Correct choice between OLS Tag Text (every match, unranked) and Zooma Annotate Text (one ranked suggestion per phrase, ontology choice decides the phrases). |
| 41 | PAIR-03 | where-to-start | 👍 | pass | Accurate: Mapping Details, asserted vs inferred with the weakest-premise idea, OLS comparison, justification and Distance as warning signs. |
| 42 | OXO-08 | where-to-start | 👍 | pass | Accurate: Multiple sets expansion, Mapping Details, Mapping Set section, premise tracing for inferences, report contents, and the OLS Issue Tracker route. |
| 43 | TRIO-02 | where-to-start | 👍 | pass | Accurate three-step overview with the final OLS check. |
| 44 | TRIO-03 | where-to-start | 👍 | pass | Accurate overview of the five stages. |

## What the run shows

**1. When a question carries a worked example, DocBot tends to answer the example instead of the use case.** The three thumbs downs that are new in this run are all of this kind. For OLS-01 (*which term represents a concept, for example heart attack*) the whole answer is that heart attack is myocardial infarction, MONDO:0005068, "which you can find using OLS". For OLS-02 (*what does an identifier such as MONDO:0005068 mean*) the answer gives the correct label, definition and synonyms of that one identifier and never says how to look an identifier up. For PAIR-02 (*the term for heart attack and its codes in ICD-10-CM, MeSH and SNOMED CT*) the answer lists the three asserted codes from the use case's example table and omits both the OLS step and the OxO procedure. OLS-03 and OLS-07 show the same tendency in a milder form: the example's facts (parent, 14 children, 20 descendants; Tinnitus HP:0000360) are right and a short method follows, so they keep a thumbs up. In every case the facts match the repository, so these are not hallucinations; they are answers that a user with a different concept or identifier cannot act on. The contrast with the "Where to start" variants is sharp: asked *where to start if I have a concept in words* (33) or *an identifier* (35), DocBot gave the full procedure that the full questions 1 and 2 lacked.

**2. Procedural answers are accurate, and the omissions are mostly caveats from the use cases' *Good to know* sections.** None of the 44 answers contradicts the repository on a step, a field, a parameter or an identifier. What is missing, when something is missing, is the qualification that makes the procedure safe: that embedding-search scores are uncurated and the definition must be read (OLS-07, present in the where-to-start variant but not the full one); that a `hasDbXref` row only links two identifiers and is not an equivalence (OXO-06); that **Asserted only** depends on the direction of the search and **Max distance 1** is the filter to use from a coding system into an ontology (OXO-02, OXO-05; TRIO-03 does get Max distance 1 right); that Zooma's confidence is a ranking score, so non-green rows need checking and green ones spot-checking (ZOOMA-01); that a curated mapping was made for a purpose and must fit the user's context (ZOOMA-06); and the TRIO-01 safeguards listed below. These are the natural targets for feedback: each is one sentence in the source document.

**3. The five pilot questions behave as before.** OLS-05, OXO-04, ZOOMA-05 and TRIO-01 came back unchanged in substance from 9 November (identical apart from punctuation), so the TRIO-01 thumbs down stands on the same grounds: a parent term's code is used without saying it is broader than the term, an inferred mapping is accepted on the code's meaning alone rather than on its asserted premises, values that cannot be coded are not left for manual coding, and choosing between several asserted codes is not covered. PAIR-03 was the one answer that changed: it is now longer and more complete (evidence columns, five-point comparison, accept/downgrade/reject, reporting route) and keeps its thumbs up. That four answers out of five are word-for-word the same across two days suggests that DocBot's output for a fixed question is close to deterministic, or cached; the interface does not say which, and the answers were streamed afresh.

**4. Small slips, none of them factual errors.** PAIR-03 says two definitions should "describe the same substance" where the use case means "the same thing in substance"; OXO-08 ends by offering to explain Zooma filters in a question that has nothing to do with Zooma; OLS-02 cites PAIR-03 as a source; and the where-to-start question assigned to PAIR-01 (38) cites the Zooma use cases and TRIO-01 rather than PAIR-01, although its content follows the expected Zooma-then-OLS path. 43 of 44 answers cite their own use case among the sources.

**5. The "Where to start" questions all pass.** The twelve overview questions received short, correctly scoped answers that name the right tool first and sketch the path; the one *partial* (38) lacks the advice to record review decisions outside Zooma. Several of these answers are better entry points than the full-question answers for the same use case (OLS-01, OLS-02, OLS-07).

Answers arrived within 5 to 15 seconds of sending each question.

## The five pilot questions across the four runs

| Use case | 28 Oct | 28 Oct rerun | 9 Nov | 11 Nov | Answer since 9 Nov |
|---|---|---|---|---|---|
| OLS-05 | 👍 | 👍 | 👍 | 👍 | unchanged in substance |
| OXO-04 | 👍 | 👍 | 👍 | 👍 | unchanged in substance |
| TRIO-01 | 👎 | 👎 | 👎 | 👎 | unchanged in substance |
| PAIR-03 | 👍 | 👍 | 👍 | 👍 | rewritten and expanded |
| ZOOMA-05 | 👍 | 👍 | 👍 | 👍 | unchanged in substance |

## Suggested priorities for feedback

1. OLS-01, OLS-02 and PAIR-02: give the procedure, and use the example to illustrate it (thumbs down with the comments below).
2. TRIO-01: the four reliability safeguards still missing since October (thumbs down, comment unchanged in substance from 9 November).
3. The one-sentence caveats listed under point 2 above, for OLS-07, OXO-02, OXO-05, OXO-06, ZOOMA-01 and ZOOMA-06 (thumbs up with a comment).

## Limitations

- One answer per question. Two days apart, four of five repeated questions gave the same text, but a single sample still cannot establish robustness to paraphrasing or variation between sessions.
- Alignment with the repository is the only criterion. The OLS, OxO and Zooma services, the API calls quoted in the answers and the link targets were not exercised; identifiers and counts were checked against the use-case documents, not against the live services.
- No ratings or comments were sent to DocBot, so nothing in this run reaches the DocBot team until the proposed feedback is submitted.
- The reference commit is the one the earlier pilots used; the remote `dev` branch was not re-fetched, and the deployed DocBot version is not exposed by the interface.

## Complete records

Each record gives the question as typed, the reference document at the pinned commit, the answer as captured (headings flattened to bold), the assessment, and the feedback text proposed for the thumbs up or thumbs down button. Message ids are DocBot's own, from the page.

### 01. OLS-01 (full) — thumbs down, fail

**Question:** Which ontology term represents the concept I have in mind — for example heart attack — and what is its identifier?

**Reference:** [OLS-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-01-find-term-for-concept.md)

**Captured:** 2026-11-11T14:02:30Z · DocBot message id 13092 · [capture file](answers/01-OLS-01.md)

**Answer:**

> The ontology term that represents the concept of a heart attack is “myocardial infarction,” which has the identifier MONDO:0005068. You can find this term and its details using [OLS](https://www.ebi.ac.uk/ols4).

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-01-find-term-for-concept.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-02-look-up-identifier.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Answers the example, not the question: names myocardial infarction (MONDO:0005068) correctly but gives no procedure for finding a term for a concept.

*Correct:*
- myocardial infarction / MONDO:0005068 for heart attack
- points to OLS

*Gaps:*
- no search steps (Search OLS box, Enter)
- no narrowing by Type = Class and Ontology
- no advice to read definition and synonyms before using the term, nor to copy the identifier from the badge
- no API search endpoint
- nothing a user with a different concept can act on

*Errors:*
- none

**Proposed feedback (thumbs down, not submitted):** 11 November run, OLS-01: the example is right (myocardial infarction, MONDO:0005068) but the answer gives no method. The use case is how to find a term for any concept: type the phrase into Search OLS, narrow by Type = Class and by Ontology, read the result card (label, identifier badge, definition), open the term to confirm definition and synonyms; or use the API search endpoint with q, ontology and type=class. The 'Where to start' variant of this question got all of this right.

### 02. OLS-02 (full) — thumbs down, partial

**Question:** I have an ontology identifier such as MONDO:0005068 in my data — what does it mean?

**Reference:** [OLS-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-02-look-up-identifier.md)

**Captured:** 2026-11-11T14:06:12.528Z · DocBot message id 13094 · [capture file](answers/02-OLS-02.md)

**Answer:**

> The ontology identifier MONDO:0005068 refers to the term **myocardial infarction**.
>
> It is defined as: “Gross necrosis of the myocardium, as a result of interruption of the blood supply to the area, as in coronary thrombosis.” Common synonyms for this term include “heart attack” and “MI.”
>
> You can explore this term further using [OLS](https://www.ebi.ac.uk/ols4) to view its hierarchy, synonyms, and cross-references, or use [OxO](https://www.ebi.ac.uk/spot/oxo) to find equivalent terms in other ontologies and coding systems.

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-02-look-up-identifier.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Correct label, definition and synonyms for the example identifier, but no lookup procedure for an identifier in general.

*Correct:*
- label myocardial infarction
- definition quoted matches the use case
- synonyms heart attack, MI
- OLS for hierarchy/synonyms/cross-references; OxO for equivalents

*Gaps:*
- does not say to paste the identifier into Search OLS and pick the defining ontology (Jump to entry with matching badge, or the result not marked IMPORTED)
- no API call (terms?obo_id=...)
- no mention of the identifier forms accepted (CURIE, underscore, IRI)
- cites PAIR-03 as a source, which is unrelated

*Errors:*
- none

**Proposed feedback (thumbs down, not submitted):** 11 November run, OLS-02: the facts for MONDO:0005068 match the use case, but a user with a different identifier is not told how to look it up: paste it into Search OLS, open the Jump to entry whose ontology badge matches the prefix (or the result not marked IMPORTED), then read label, definition, synonyms, Class Information and Class Relations; API: /api/terms?obo_id=... and use the record with is_defining_ontology true. The 'Where to start' variant covered this correctly.

### 03. OLS-03 (full) — thumbs up, partial

**Question:** What are the broader and narrower terms of myocardial infarction — its parents, its children and everything beneath it?

**Reference:** [OLS-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-03-explore-hierarchy.md)

**Captured:** 2026-11-11T14:06:21.114Z · DocBot message id 13096 · [capture file](answers/03-OLS-03.md)

**Answer:**

> In the Mondo ontology, the term myocardial infarction (MONDO:0005068) has the following hierarchical structure:
>
> - **Parents (Broader terms):** The term has one parent, which is myocardial disorder (MONDO:0024643).
> - **Children (Directly beneath):** There are 14 direct children, including acute myocardial infarction (MONDO:0004781) and silent myocardial infarction (MONDO:0003678).
> - **Descendants (Everything beneath):** There are 20 descendants in total.
>
> You can explore this hierarchy further by viewing the Tree panel on the term’s page in [OLS](https://www.ebi.ac.uk/ols4).
>
> Would you like to know how to retrieve these hierarchical relationships using the [OLS](https://www.ebi.ac.uk/ols4) API?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-03-explore-hierarchy.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Example facts (parent, 14 children, 20 descendants, example children) all match the use case; points to the Tree panel but gives little method and no API.

*Correct:*
- one parent myocardial disorder MONDO:0024643
- 14 direct children incl. acute MI MONDO:0004781 and silent MI MONDO:0003678
- 20 descendants
- Tree panel on the term page

*Gaps:*
- no description of reading ancestors upward in the Tree, expanding children, Show counts, Show all siblings
- no Graph view or Class Relations
- no API endpoints (children, hierarchicalDescendants, hierarchicalAncestors) or pagination; offered only as a follow-up

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-03: counts and identifiers match the use case and the Tree panel is the right pointer. Please add how to use it (read upwards for ancestors, expand for children, Show counts), the Graph view for other relationships, and the API endpoints children, hierarchicalDescendants and hierarchicalAncestors with pagination, rather than leaving the API to a follow-up.

### 04. OLS-04 (full) — thumbs up, pass

**Question:** Which ontologies cover my subject area, and is a particular ontology suitable — what is its scope, which version is loaded, how big is it and under which licence is it published?

**Reference:** [OLS-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-04-find-and-inspect-ontology.md)

**Captured:** 2026-11-11T14:08:54.060Z · DocBot message id 13098 · [capture file](answers/04-OLS-04.md)

**Answer:**

> To find ontologies covering your subject area and determine their suitability, you can use [OLS](https://www.ebi.ac.uk/ols4).
>
> **Finding Ontologies**
>
> 1. Navigate to the [OLS](https://www.ebi.ac.uk/ols4) website and click **Ontologies** in the top menu.
> 2. You can filter the list by clicking category labels (e.g., health, phenotype) or by typing into the **Filter by Description**, **Filter by ID**, or **Filter by Ontology** fields.
>
> **Determining Suitability**
>
> Once you have identified an ontology, click its row to open its dedicated page to inspect the following details:
>
> - **Scope:** Read the **Description** provided at the top of the page.
> - **Version:** Check the **Version** field at the top of the page or the **Version IRI** listed under **Ontology Information**.
> - **Size:** View the **Classes**, **Properties**, and **Individuals** tabs, which display the count of each.
> - **License:** Check the **License** metadata listed under **Ontology Information**.
>
> Alternatively, you can retrieve this information via the [OLS](https://www.ebi.ac.uk/ols4) API:
>
> - To search for ontologies: `curl -s 'https://www.ebi.ac.uk/ols4/api/v2/ontologies?search=[your_subject]&size=20'`
> - To fetch specific details for an ontology: `curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/[ontology_id]'`
>
> - This returns `config.title`, `config.description`, `config.version`, `numberOfTerms`, `numberOfProperties`, `numberOfIndividuals`, and `updated` (the last load date).
>
> Would you like to know how to request an ontology that is not currently in [OLS](https://www.ebi.ac.uk/ols4)?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-04-find-and-inspect-ontology.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Accurate: Ontologies page, category and text filters, where scope, version, size and licence are shown, and the two API calls with the right fields.

*Correct:*
- Ontologies page and filters
- Description, Version / Version IRI, Classes/Properties/Individuals tabs, License under Ontology Information
- v2/ontologies?search and api/ontologies/{id} with config.* and numberOf* fields and updated

*Gaps:*
- Last loaded date on the page not mentioned
- Imports from / Exports to and the Homepage, Mailing List, Issue Tracker buttons not mentioned

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-04: accurate against the use case for finding ontologies and inspecting scope, version, size and licence on the website and via the API. Minor additions: the Last loaded date under Ontology Information, and Imports from / Exports to.

### 05. OLS-05 (full) — thumbs up, pass

**Question:** Is the term I am using still current? If it has been made obsolete, which term should I use instead?

**Reference:** [OLS-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-05-check-obsolete-term.md)

**Captured:** 2026-11-11T14:08:58.624Z · DocBot message id 13100 · [capture file](answers/05-OLS-05.md)

**Earlier runs:** 28 Oct 👍 · 28 Oct rerun 👍 · 9 Nov 👍 · answer unchanged in substance since 9 Nov

**Answer:**

> To determine if an ontology term is current or obsolete, you should use [OLS](https://www.ebi.ac.uk/ols4).
>
> **Using the [OLS](https://www.ebi.ac.uk/ols4) website:**
>
> 1. Open [OLS](https://www.ebi.ac.uk/ols4).
> 2. Tick the **Include obsolete terms** checkbox under the search box.
> 3. Enter the term identifier and press Enter.
> 4. Open the result from the relevant ontology.
> 5. Check the top of the term’s page:
>
> - If there is no red box, the term is current.
> - If a red box says “This class is deprecated,” the term is obsolete.
> 6. If obsolete, look under **Class Information** for “term replaced by” to find the suggested replacement. If no replacement is listed, the ontology may provide a “Reason” that suggests an alternative.
>
> **Using the [OLS](https://www.ebi.ac.uk/ols4) API:**
>
> You can check the status programmatically using the following command:
>
> `curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/[ontology_id]/terms?obo_id=[term_id]'`
>
> In the response, check the `is_obsolete` field:
>
> - If `true`, the term is obsolete.
> - The `term_replaced_by` field will contain the IRI of the replacement, or `null` if none is recorded.
>
> If the term is obsolete and no replacement is provided by the ontology, you can use [OxO](https://www.ebi.ac.uk/spot/oxo) to find mappings to current terms or [Zooma](https://www.ebi.ac.uk/spot/zooma) to find a successor based on the term’s wording.
>
> Would you like to know how to use [OxO](https://www.ebi.ac.uk/spot/oxo) to find a successor for an obsolete term?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-05-check-obsolete-term.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-02-update-outdated-annotations.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Identical to the 9 November answer; accurate on Include obsolete terms, the deprecated box, term replaced by, API fields and the OxO/Zooma fallback.

*Correct:*
- Include obsolete terms
- red deprecated box
- term replaced by under Class Information, Reason
- is_obsolete and term_replaced_by via API
- OxO/Zooma when no replacement is recorded

*Gaps:*
- does not say to check the replacement's definition before switching

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-05: accurate, unchanged from 9 November. Minor improvement: say to check the replacement's definition before switching to it.

### 06. OLS-06 (full) — thumbs up, partial

**Question:** Which ontology terms are mentioned in this piece of text — a sample description, an abstract, a protocol?

**Reference:** [OLS-06](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-06-tag-text.md)

**Captured:** 2026-11-11T14:09:07.219Z · DocBot message id 13102 · [capture file](answers/06-OLS-06.md)

**Answer:**

> To identify ontology terms mentioned in a piece of text, you can use the [OLS](https://www.ebi.ac.uk/ols4) Tag Text tool. This tool highlights stretches of text that match a term’s label or a previously curated mapping, providing the term’s IRI and ontology.
>
> To use this tool on the website:
>
> 1. Open [OLS](https://www.ebi.ac.uk/ols4) and select **Tag Text** from the top menu.
> 2. Paste or type your text into the provided box (or drag and drop a plain text file).
> 3. The tool will automatically tag the text, displaying the matched stretches and a list of matched terms including the Matched Text, Term IRI, Term Label, Ontology, and Match Type.
>
> If you prefer to use [Zooma](https://www.ebi.ac.uk/spot/zooma) for annotating free text, you can use the **Annotate Text** tab to receive ranked suggestions per phrase based on specific ontologies you select. Use [OLS](https://www.ebi.ac.uk/ols4) when you want to see every match, and [Zooma](https://www.ebi.ac.uk/spot/zooma) when you want one ranked suggestion per phrase.
>
> Would you like to know how to use the [OLS](https://www.ebi.ac.uk/ols4) API to perform this tagging programmatically?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-04-annotate-free-text.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-06-tag-text.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Correct tool (Tag Text), correct inputs and result columns, and a correct contrast with Zooma Annotate Text; omits the ontology filter, match-length controls, CSV download and API.

*Correct:*
- Tag Text page, paste/type/drag a file, tags automatically
- Matched Terms columns incl. Match Type
- OLS for every match vs Zooma for one ranked suggestion per phrase

*Gaps:*
- Ontologies panel to keep only chosen ontologies (the main way to get one answer per match)
- Min match length and Include substrings
- Download CSV
- tag_text API and its looser defaults

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-06: right tool and workflow. Please add the Ontologies panel (tick ontologies, reorder, exclude) since the example yields 30 matches across ontologies without it, the Min match length and Include substrings controls, Download CSV, and the v2/tag_text API with minLength and includeSubstrings set explicitly.

### 07. OLS-07 (full) — thumbs up, partial

**Question:** I can describe what I mean in everyday words — for example ringing in the ears — but I do not know what ontologies call it. Which terms mean the same thing?

**Reference:** [OLS-07](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-07-semantic-search.md)

**Captured:** 2026-11-11T14:10:51.300Z · DocBot message id 13104 · [capture file](answers/07-OLS-07.md)

**Answer:**

> The everyday term “ringing in the ears” corresponds to the ontology term **Tinnitus**, which has the identifier **HP:0000360**.
>
> You can find this term by using the embedding-based search feature in [OLS](https://www.ebi.ac.uk/ols4) by following these steps:
>
> - Navigate to [OLS](https://www.ebi.ac.uk/ols4).
> - Enter “ringing in the ears” into the search box.
> - Select an embedding model (e.g., llama-embed-nemotron-8b_pca512) from the Search Model list instead of the default Lexical option.
> - Click Search to view the ranked results.
>
> Would you like to know how to use the [OLS](https://www.ebi.ac.uk/ols4) API to perform this search programmatically?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Correct answer (Tinnitus HP:0000360) and correct embedding-search steps; omits the caveat that scores are uncurated and the definition must be checked.

*Correct:*
- Tinnitus HP:0000360
- Search Model -> embedding model llama-embed-nemotron-8b_pca512 instead of Lexical
- ranked results

*Gaps:*
- no caveat that similarity scores are not a judgement of correctness and the definition must be read
- no Filter by ontology, Similar Classes, or API (llm_models, llm_search)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-07: correct result and steps. Please add the use case's caveat that embedding results are uncurated and the definition must be checked before a term is used, plus Filter by ontology in the blue bar and the llm_search API. The 'Where to start' variant included the caveat.

### 08. OLS-08 (full) — thumbs up, pass

**Question:** How do I look for terms in just one part of an ontology — for example, offer only heart disorders when someone types "infarc" into a form field?

**Reference:** [OLS-08](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-08-search-within-branch.md)

**Captured:** 2026-11-11T14:10:59.862Z · DocBot message id 13106 · [capture file](answers/08-OLS-08.md)

**Answer:**

> To restrict your search to a specific branch of an ontology, you can use the `childrenOf` parameter in the [OLS](https://www.ebi.ac.uk/ols4) API. This parameter filters results to include only terms that are descendants of the specified term.
>
> To perform this search:
>
> 1. Find the IRI of the term at the top of the branch you wish to search (e.g., “heart disorder”, `http://purl.obolibrary.org/obo/MONDO_0005267`).
> 2. URL-encode the IRI (e.g., `:` becomes `%3A` and `/` becomes `%2F`).
> 3. Call the `select` endpoint (for search-as-you-type) or the `search` endpoint (for results pages) with the `childrenOf` parameter.
>
> For example, to search for “infarc” within the heart disorder branch of the Mondo ontology:
>
> `curl -s 'https://www.ebi.ac.uk/ols4/api/select?q=infarc&ontology=mondo&childrenOf=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0005267&rows=10'`
>
> **Good to know:**
>
> - `childrenOf` follows “is a” (subclass) links.
> - `allChildrenOf` can be used to follow other hierarchical relationships, such as “part of”.
> - You can add `type=class` to exclude properties and individuals, and `obsoletes=true` to include obsolete terms.
> - The website interface does not currently support branch filtering for searches; you can use the **Tree** panel on a term’s page to explore branches visually.
>
> Would you like to know how to find the IRI for the top-level term of a branch?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-08-search-within-branch.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Accurate and complete: childrenOf on select/search, single URL-encoding, the exact example call, allChildrenOf, type=class, obsoletes=true, and that the website has no branch filter.

*Correct:*
- childrenOf with branch IRI MONDO_0005267
- URL-encode once
- select for autocomplete, search for results pages
- example curl identical to the use case
- allChildrenOf for part-of
- type=class, obsoletes=true
- no branch filter on the website; use Tree

*Gaps:*
- store obo_id/iri rather than the label; response.docs fields

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-08: accurate against the use case, including the example call, the single URL-encoding, allChildrenOf and the website limitation. Minor addition: read response.docs and store the obo_id or IRI of the chosen suggestion, not the label.

### 09. OLS-09 (full) — thumbs up, pass

**Question:** How can my AI assistant, or an application built on a large language model, look terms up in OLS instead of guessing identifiers?

**Reference:** [OLS-09](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-09-connect-ai-assistant.md)

**Captured:** 2026-11-11T14:11:08.429Z · DocBot message id 13108 · [capture file](answers/09-OLS-09.md)

**Answer:**

> To enable an AI assistant or an application to look up terms in [OLS](https://www.ebi.ac.uk/ols4) using the Model Context Protocol (MCP), follow these steps:
>
> 1. **Configure the MCP Server**: In your assistant’s settings, add the remote MCP server using the following details:
>
> - **Address**: `https://www.ebi.ac.uk/ols4/api/mcp`
> - **Transport**: Streamable HTTP
> - **Authentication**: None
> - *Example for Claude Code*: `claude mcp add --transport http ols https://www.ebi.ac.uk/ols4/api/mcp`
> 2. **Verify Tools**: Ensure the assistant recognizes the available tools. There are currently twelve tools, including `searchClasses`, `fetch`, `getAncestors`, `getChildren`, `getDescendants`, `listOntologies`, and `searchClassesWithEmbeddingModel`.
> 3. **Execute Lookups**: Instruct the assistant to use [OLS](https://www.ebi.ac.uk/ols4) for specific queries. For example, you can ask: *“Use OLS to find the Mondo term for heart attack, then list its parent terms.”*
> 4. **Confirm Results**: Because an assistant can misread or misreport tool outputs, you should treat its answers as pointers and manually confirm important identifiers by opening them in [OLS](https://www.ebi.ac.uk/ols4).
>
> For semantic searches, the assistant should first call `listEmbeddingModels` and then use `searchClassesWithEmbeddingModel` with a model where `can_embed` is true.
>
> Would you like to know how to verify the server’s reachability using `curl`?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-09-connect-ai-assistant.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Accurate: MCP address, Streamable HTTP, no authentication, Claude Code example, the twelve tools, example prompt, verification advice and the embedding-model tools.

*Correct:*
- https://www.ebi.ac.uk/ols4/api/mcp, Streamable HTTP, none
- claude mcp add example
- twelve tools and names
- confirm identifiers in OLS
- listEmbeddingModels then searchClassesWithEmbeddingModel with can_embed

*Gaps:*
- MCP Server page in the OLS menu not mentioned

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-09: accurate against the use case on server address, transport, authentication, tools and verification. Minor addition: the MCP Server page in the OLS menu lists the address and tools.

### 10. OXO-01 (full) — thumbs up, pass

**Question:** I have a term in one ontology — for example myocardial infarction, MONDO:0005068. What is it called in other ontologies and coding systems such as MeSH, ICD-10-CM or SNOMED CT?

**Reference:** [OXO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-01-find-equivalent-terms.md)

**Captured:** 2026-11-11T14:12:33.980Z · DocBot message id 13110 · [capture file](answers/10-OXO-01.md)

**Answer:**

> To find equivalent terms for ‘myocardial infarction’ (MONDO:0005068) in other vocabularies like MeSH, ICD-10-CM, or SNOMED CT, you can use the [OxO](https://www.ebi.ac.uk/spot/oxo) tool.
>
> **Using the website**
>
> 1. Open [OxO](https://www.ebi.ac.uk/spot/oxo).
> 2. Paste the identifier `MONDO:0005068` into the field “Which term do you want to map?”.
> 3. In the “To ontologies” field, select the target vocabularies (e.g., `ICD10CM`, `MESH`, and `SCTID` for SNOMED CT).
> 4. Click **Search**.
> 5. Review the results table. For each target, prefer rows marked as **Asserted** with the predicate `SKOS:exactMatch`. You can copy the codes from the Object column or download the table.
>
> **Using the API**
>
> You can perform a batch search using a POST request to the [OxO](https://www.ebi.ac.uk/spot/oxo) API:
>
> ```
> curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
> -H 'Content-Type: application/json' \
> -d '{
>   "queries": ["MONDO:0005068"],
>   "objectPrefixes": ["MESH", "ICD10CM", "SCTID"],
>   "page": 0,
>   "size": 100,
>   "groupBySpo": true
> }'
> ```
>
> The results will be returned in `mappings.content`, where each entry includes the `subject_id`, `predicate_id`, `object_id`, and `inference_type` (e.g., `ASSERTED` or `SSSOM_INFERENCE`). Note that mappings should be carefully evaluated, as both asserted and inferred mappings may be incorrect.
>
> Would you like to know how to validate a specific mapping using [OxO](https://www.ebi.ac.uk/spot/oxo)?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-01-find-equivalent-terms.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-02-find-term-and-translate.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate website and API procedure with the right target prefixes (MESH, ICD10CM, SCTID) and sound advice to prefer asserted exact matches.

*Correct:*
- Which term do you want to map? field, To ontologies, Search
- prefixes ICD10CM, MESH, SCTID
- prefer Asserted + SKOS:exactMatch; copy or download
- POST mappings/search with queries, objectPrefixes, groupBySpo; fields incl. inference_type

*Gaps:*
- meaning of the other columns (Predicate kinds, Mapping justification, Distance, Mapping set) not explained
- eye icon to Mapping Details and OLS link not mentioned
- label matching must be complete, and labels can belong to several ontologies

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-01: accurate against the use case for website and API, including the target prefixes and preferring asserted exact matches. Additions worth making: what Predicate, Mapping justification, Distance and Mapping set tell the user, the eye icon for Mapping Details, and that a label must match completely (Partial match under More options).

### 11. OXO-02 (full) — thumbs up, pass

**Question:** I have a list of terms from one ontology. What are their equivalents in a specific target — for example, which ICD-10-CM codes correspond to my Mondo disease terms — and which of my terms have no equivalent there?

**Reference:** [OXO-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-02-map-list-to-target.md)

**Captured:** 2026-11-11T14:12:44.541Z · DocBot message id 13112 · [capture file](answers/11-OXO-02.md)

**Answer:**

> To map a list of terms from one ontology to a target, you can use [OxO](https://www.ebi.ac.uk/spot/oxo). You will need your list of identifiers (one per line) and the prefix of the target ontology (e.g., ICD10CM).
>
> **Using the Website**
>
> 1. Open [OxO](https://www.ebi.ac.uk/spot/oxo) and select **Multiple terms**.
> 2. Enter your terms in the box or upload a file (.txt, .csv, or .tsv).
> 3. In **To ontologies**, select your target (e.g., ICD10CM). Leave **From ontologies** empty.
> 4. Click **Search**.
> 5. Review the resulting table. You can filter for published mappings by clicking the filter icon in the **Type** column header and selecting **Asserted only**.
> 6. Click the download icon to save the results as an SSSOM file. To identify terms with no equivalent, compare the **Subject** column of the downloaded file against your original list.
>
> **Using the API**
>
> You can perform a batch mapping request using the following endpoint:
>
> `POST https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/batch-map`
>
> The JSON request body should include:
>
> - `terms`: A list of your identifiers.
> - `objectPrefixes`: The target prefix (e.g., `["ICD10CM"]`).
> - `inferenceType`: Use `["ASSERTED"]` to restrict results to asserted mappings; leave this out to include inferred mappings.
>
> The API response provides a `summary` of the mapping process and explicitly lists terms that could not be mapped in the `unmappedInputs` field.
>
> Would you like to know how to handle cases where a term has multiple potential codes?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-02-map-list-to-target.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: Multiple terms mode, file upload, To ontologies, Asserted only filter, SSSOM download, Subject-column comparison, and the batch-map API with unmappedInputs.

*Correct:*
- Multiple terms; paste or upload .txt/.csv/.tsv
- To ontologies target, From empty
- Type -> Asserted only
- download SSSOM; compare Subject column to find unmapped
- batch-map API: terms, objectPrefixes, inferenceType optional; summary and unmappedInputs

*Gaps:*
- direction caveat: from a coding system into an ontology, Asserted only leaves nothing and Max distance 1 should be used instead
- use identifiers rather than labels in a batch
- re-run without Asserted only for leftovers; format=sssom-tsv; 1,000-term limit

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-02: accurate against the use case, including unmappedInputs. Please add the direction caveat (mappings are stored in the published direction, so from ICD-10-CM into Mondo use Max distance 1 rather than Asserted only), and that batches should use identifiers, not labels.

### 12. OXO-03 (full) — thumbs up, pass

**Question:** Which terms in one ontology correspond to terms in another — for example, all mappings from the Human Disease Ontology (DOID) to the Experimental Factor Ontology (EFO) — and can I have them as a file?

**Reference:** [OXO-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-03-all-mappings-between-ontologies.md)

**Captured:** 2026-11-11T14:12:53.604Z · DocBot message id 13114 · [capture file](answers/12-OXO-03.md)

**Answer:**

> To find and download mappings between the Human Disease Ontology (DOID) and the Experimental Factor Ontology (EFO) using [OxO](https://www.ebi.ac.uk/spot/oxo), you can use either the website or the API.
>
> **Using the website**
>
> 1. Open [OxO](https://www.ebi.ac.uk/spot/oxo).
> 2. Leave the term box empty.
> 3. In the **From ontologies** list, select **DOID**.
> 4. In the **To ontologies** list, select **EFO**.
> 5. Click **Search**.
> 6. Once the results load, click the download icon next to the mapping count to save the results as an SSSOM file (oxo2-mappings.tsv).
>
> **Using the API**
>
> You can retrieve the mappings as a complete SSSOM file using the following command:
>
> `curl -s 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings?from=DOID&to=EFO&format=sssom-tsv' -o doid-efo.sssom.tsv`
>
> Note that the downloaded file is not folded, meaning it may contain more lines than the number of rows displayed in the web interface, as the interface folds identical mappings from different sources into a single row.
>
> Would you like to know how to filter these results for asserted mappings only?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-03-all-mappings-between-ontologies.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: empty term box, From/To, download as SSSOM, the exact API command for the file, and the folding explanation for row/line count differences.

*Correct:*
- empty term box, From DOID, To EFO, Search, download oxo2-mappings.tsv
- format=sssom-tsv API command identical to the use case
- table folds identical mappings; file is not folded

*Gaps:*
- direction matters and the swap button
- results include OxO inferences (mapping set oxo2/inferences)
- JSON paging and forSubject API not mentioned

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-03: accurate against the use case, including the folding explanation. Additions: direction matters (use the swap button for the reverse), and the result includes inferred mappings from the oxo2/inferences set.

### 13. OXO-04 (full) — thumbs up, pass

**Question:** Can I rely on this mapping? Who published it and on what basis — and if OxO inferred it, from which published mappings?

**Reference:** [OXO-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-04-check-mapping-provenance.md)

**Captured:** 2026-11-11T14:14:18.718Z · DocBot message id 13116 · [capture file](answers/13-OXO-04.md)

**Earlier runs:** 28 Oct 👍 · 28 Oct rerun 👍 · 9 Nov 👍 · answer unchanged in substance since 9 Nov

**Answer:**

> Whether you can rely on a mapping depends on its origin and the evidence behind it. [OxO](https://www.ebi.ac.uk/spot/oxo) does not publish its own mappings except for inferences; every mapping it displays originates from either a curated mapping set or an ontology’s own cross-references.
>
> To determine the reliability of a specific mapping:
>
> - **Check the Type:** In the results table, “Asserted” means the mapping was published by a third party. “SSSOM inference” means [OxO](https://www.ebi.ac.uk/spot/oxo) derived it by chaining published mappings.
> - **View Mapping Details:** Click the eye icon at the end of the row to open the Mapping Details page. This page provides:
>
> - **Provenance:** Information on authors, creators, and reviewers if recorded by the source.
> - **Mapping Set:** The collection the mapping belongs to, which identifies the publisher you should contact if you believe the mapping is incorrect.
> - **Justification:** How the mapping was made (e.g., ManualMappingCuration or LexicalMatching) and the publisher’s confidence level, if provided.
> - **For Inferred Mappings:** The details page includes an “Inference Details” section. This lists the “Asserted Mappings” the inference rests on and provides an “Explanation” graph showing the derivation. An inferred mapping is only as reliable as the published mappings it depends on; you should judge the inference by its weakest ingredient (e.g., an inference passing through an automatic label match is less reliable than one based on manually curated exact matches).
>
> “Exact match” is a claim made by the publisher for their specific purposes; you should evaluate whether it meets your own requirements, such as whether the terms are interchangeable for your specific use case (e.g., counting patients vs. retrieving literature).
>
> Would you like to know how to filter your search results to only include mappings that meet specific evidence requirements?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-04-check-mapping-provenance.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Identical to the 9 November answer; accurate on asserted vs inferred, Mapping Details sections, Inference Details, judging by the weakest premise and fitness for purpose.

*Correct:*
- Asserted vs SSSOM inference
- eye icon -> Mapping Details: Provenance, Mapping Set, Justification and confidence
- Inference Details: Asserted Mappings and Explanation graph
- weakest-ingredient judgement
- exact match is the publisher's claim

*Gaps:*
- Distance column as a quick indicator
- API by mapping_id with asserted_mappings and explanation

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-04: accurate, unchanged from 9 November. Minor additions: Distance as a quick indicator of how many ontologies an inference passes through, and the sssom/mappings/{mapping_id} API with asserted_mappings and explanation.

### 14. OXO-05 (full) — thumbs up, pass

**Question:** OxO returns many mappings for my term. How do I keep only the ones I am prepared to use — for example only published ones, only exact matches, or only those a curator made by hand?

**Reference:** [OXO-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-05-filter-by-evidence.md)

**Captured:** 2026-11-11T14:14:27.807Z · DocBot message id 13118 · [capture file](answers/14-OXO-05.md)

**Answer:**

> To filter [OxO](https://www.ebi.ac.uk/spot/oxo) mappings on the website, run your search and use the filter icons in the column headers. Filters can be combined, and a row must pass all of them to be displayed.
>
> - **Published mappings only:** Click the filter icon in the **Type** column header and choose **Asserted only**.
> - **Specific match types (e.g., exactMatch):** Click the filter icon in the **Predicate** header and type the desired match type (e.g., `exactMatch`) into the ID box, or select a value from the provided list.
> - **Manually curated mappings:** Click the filter icon in the **Mapping justification** header and select **ManualMappingCuration** (or type part of the name).
>
> You can also filter by **Distance** (e.g., choosing 1 to keep only asserted mappings and inferences within two ontologies) or by **Object** (to target a specific ontology prefix). A coloured dot on a filter icon indicates that the column is filtered, and you can use the **Clear** button next to the Search button to reset all filters.
>
> If you are using the [OxO](https://www.ebi.ac.uk/spot/oxo) API, these filters are applied as fields in your search request:
>
> - **Published mappings:** Use `"inferenceType": ["ASSERTED"]`.
> - **Predicate:** Use `"columnFilters": [{"id": "predicate_id", "value": "SKOS:exactMatch", "match": "EXACT"}]`.
> - **Justification:** Use `"columnFilters": [{"id": "mapping_justification", "value": "ManualMappingCuration"}]`.
>
> Would you like to know how to save these filtered results as a file?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-05-filter-by-evidence.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate column filters (Type, Predicate, Mapping justification, Distance, Object), clear-filter behaviour, and the matching API fields.

*Correct:*
- Type -> Asserted only
- Predicate filter with exactMatch
- Mapping justification -> ManualMappingCuration
- Max distance 1 meaning
- Object prefix filter; coloured dot; Clear
- API inferenceType and columnFilters for predicate_id and mapping_justification

*Gaps:*
- More options -> Where should mappings come from? (Ontologies / Curated sets / Both) and Choose specific mapping sets; API mappingSetCategory and mappingSetIds
- direction caveat for Asserted only
- download honours the filters (left to a follow-up)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-05: accurate against the use case for the column filters and the API fields. Please add the source-kind choice under More options (Ontologies / Curated sets / Both, or specific mapping sets) and the caveat that Asserted only depends on direction.

### 15. OXO-06 (full) — thumbs up, pass

**Question:** I searched OxO for a term that I know exists, and got nothing (or less than I expected). Are there really no mappings — or are they hidden?

**Reference:** [OXO-06](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-06-search-returns-nothing.md)

**Captured:** 2026-11-11T14:14:36.870Z · DocBot message id 13120 · [capture file](answers/15-OXO-06.md)

**Answer:**

> By default, [OxO](https://www.ebi.ac.uk/spot/oxo) only displays mappings that make a definite claim about the relationship between two terms (such as exact, close, broad, or narrow matches). It hides “loose” links and mappings involving obsolete terms.
>
> You may be getting no results or fewer than expected because [OxO](https://www.ebi.ac.uk/spot/oxo) excludes the following by default:
>
> - **Cross-references (oboInOwl:hasDbXref):** Links between identifiers that do not specify the relationship type.
> - **Subclass links (rdfs:subClassOf):** Links indicating one term is a kind of another, rather than equivalent.
> - **Obsolete terms:** Any mapping involving a term marked as obsolete.
>
> To view these hidden mappings, click **More options** under the Search button on the [OxO](https://www.ebi.ac.uk/spot/oxo) website and tick the boxes for **Cross-reference (oboInOwl:hasDbXref)**, **Subclass (rdfs:subClassOf)**, and **Obsolete terms**.
>
> Additionally, ensure your search parameters are correct:
>
> - **Label matching:** If you searched by label, [OxO](https://www.ebi.ac.uk/spot/oxo) requires a complete match (ignoring case). Under **More options → Label matching**, you can switch to **Partial match** or search by identifier instead.
> - **Direction:** If you restricted your search using **From ontologies** or **To ontologies**, try clearing these fields or swapping them using the ⇄ icon.
> - **Identifier prefixes:** Ensure the prefix of your term is recognized by [OxO](https://www.ebi.ac.uk/spot/oxo) by typing it into the **From ontologies** field to see if it is offered as a suggestion.
>
> Would you like to know how to retrieve these mappings using the [OxO](https://www.ebi.ac.uk/spot/oxo) API?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-06-search-returns-nothing.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-01-find-equivalent-terms.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: what OxO hides by default, the three Also show options under More options, and the direction, label-matching and prefix checks.

*Correct:*
- hides hasDbXref, subClassOf and obsolete terms by default
- More options -> tick Cross-reference, Subclass, Obsolete terms
- Label matching -> Partial match, or search by identifier
- clear or swap From/To
- check the prefix is known

*Gaps:*
- caveat that a hasDbXref row only links identifiers and may not be an equivalence
- API includeWeakPredicates / includeObsolete (left to a follow-up)
- suggestion list follows the same settings

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-06: accurate against the use case. Please add the caveat that a row with OBOINOWL:hasDbXref only says the source linked the two identifiers, not that they are equivalent, and the API fields includeWeakPredicates and includeObsolete.

### 16. OXO-07 (full) — thumbs up, pass

**Question:** Where do OxO's mappings come from? Which mapping sets does it hold, what is in a particular set, and how do I search within just that set?

**Reference:** [OXO-07](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-07-browse-mapping-sets.md)

**Captured:** 2026-11-11T14:16:06.369Z · DocBot message id 13122 · [capture file](answers/16-OXO-07.md)

**Answer:**

> [OxO](https://www.ebi.ac.uk/spot/oxo) loads its mappings from published collections called mapping sets, which are provided in the SSSOM format. These sets originate from two primary sources:
>
> - **Ontologies:** Cross-references that an ontology publishes about its own terms, extracted from ontologies in [OLS](https://www.ebi.ac.uk/ols4).
> - **Curated sets:** Mapping files published independently, such as Biomappings or MGI mouse–human phenotype mappings.
>
> Additionally, [OxO](https://www.ebi.ac.uk/spot/oxo) generates its own set of inferred mappings.
>
> **Mapping Sets and Content**
>
> [OxO](https://www.ebi.ac.uk/spot/oxo) holds hundreds of mapping sets, categorized as either “ONTOLOGY” or “CURATED.” You can view the full list, including descriptions and contents, through the following methods:
>
> - **On the website:** Open [OxO](https://www.ebi.ac.uk/spot/oxo), click **More options**, and select **Choose specific mapping sets…**. You can browse the tables for curated sets and ontologies, or filter by column headings. Clicking a set’s name in a results table will open its dedicated page, which displays its title, description, provider, and a table of all contained mappings.
> - **Via the API:** You can list all mapping sets using `GET https://www.ebi.ac.uk/spot/oxo/api/v2/mapping-sets` or fetch a specific set’s description using `GET https://www.ebi.ac.uk/spot/oxo/api/v2/mapping-sets/by-id?mappingSetId={URL-encoded-ID}`.
>
> **Searching Within a Set**
>
> - **On the website:** In the “Choose specific mapping sets” picker, select the desired set(s) by clicking the row. Once selected, perform your search; the results will be restricted to mappings belonging only to those sets.
> - **Via the API:** Use a `POST` request to `https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search` and include the `mappingSetIds` parameter in your JSON body to limit the search to specific sets.
>
> Would you like to know how to check the provenance or derivation of a specific mapping within these sets?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-07-browse-mapping-sets.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: the two kinds of mapping set plus OxO's inference set, the picker under More options, set pages, and the mapping-sets and mappingSetIds API calls.

*Correct:*
- ontology cross-references from OLS and curated sets (Biomappings, MGI); inferences as a further set
- ONTOLOGY / CURATED categories
- Choose specific mapping sets picker; set page via the Mapping set column
- GET mapping-sets, by-id?mappingSetId=, search with mappingSetIds

*Gaps:*
- Data Content box and data-content API
- downloading a set's mappings from its page

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-07: accurate against the use case for sources, the picker, set pages and the API. Minor additions: the Data Content box on the home page and the download icon on a set's page.

### 17. OXO-08 (full) — thumbs up, pass

**Question:** A mapping in OxO looks wrong to me. Which source published it — or, if OxO inferred it, which of the published mappings it rests on is wrong — and whom do I tell?

**Reference:** [OXO-08](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md)

**Captured:** 2026-11-11T14:16:15.932Z · DocBot message id 13124 · [capture file](answers/17-OXO-08.md)

**Answer:**

> To identify the source of a mapping in [OxO](https://www.ebi.ac.uk/spot/oxo), follow these steps:
>
> 1. **Locate the mapping:** Find the row in your [OxO](https://www.ebi.ac.uk/spot/oxo) results table and click the eye icon to open the Mapping Details page.
> 2. **Check the Type:**
>
> - **Asserted:** The mapping was published by an external project. The “Mapping Set” section on the details page will identify the source, provider, or creator.
> - **SSSOM inference:** The mapping was derived by [OxO](https://www.ebi.ac.uk/spot/oxo). Under “Inference Details,” the “Asserted Mappings” table lists the published mappings the inference rests on.
> 3. **Identify the error:**
>
> - For **asserted mappings**, the error lies within the identified mapping set.
> - For **inferred mappings**, the error lies in one of the underlying asserted premises. You can investigate these by comparing the terms in [OLS](https://www.ebi.ac.uk/ols4) or checking the “Mapping justification” column for automated methods like “LexicalMatching,” which are more prone to errors.
> 4. **Report the error:**
>
> - **Asserted mappings:** Contact the project that publishes the mapping set. If the set is “OLS extracted… mappings,” use the Issue Tracker button on the ontology’s page in [OLS](https://www.ebi.ac.uk/ols4). If the set is a web address, open it in a browser to find the repository or contact information.
> - **Inferred mappings:** Report the error to the publisher of the specific premise (the underlying asserted mapping) that is incorrect.
>
> When reporting, provide the address of the [OxO](https://www.ebi.ac.uk/spot/oxo) details page, the subject and object with their labels, the predicate, the mapping set identifier, and a clear explanation of why the mapping is wrong. In the meantime, you can use column filters in [OxO](https://www.ebi.ac.uk/spot/oxo) to exclude the problematic mapping or set from your results.
>
> Would you like to know how to use [Zooma](https://www.ebi.ac.uk/spot/zooma) or [OxO](https://www.ebi.ac.uk/spot/oxo) filters to manage these mappings?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-04-check-mapping-provenance.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate tracing of asserted and inferred mappings to their source, correct reporting routes (project, OLS Issue Tracker for extracted cross-references, premise publisher) and report contents.

*Correct:*
- eye icon -> Mapping Details; Asserted vs SSSOM inference
- Mapping Set section identifies the publisher
- Inference Details -> Asserted Mappings; error lies in a premise; LexicalMatching suspicious
- OLS extracted ... mappings -> Issue Tracker in OLS; web-address identifiers opened in a browser
- what to include in a report; filter the mapping out meanwhile

*Gaps:*
- rows marked Multiple sets must be expanded to reach each publisher
- check whether the set has other mappings of the same kind
- MappingChaining and confidence below 1 as further suspects
- closing offer mentions Zooma, which plays no part here

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-08: accurate against the use case on tracing and reporting. Additions: expand rows marked Multiple sets to reach each publisher, check the set for other mappings of the same kind before reporting, and treat MappingChaining or a confidence below 1 as suspects too. The closing offer to use Zooma is out of place here.

### 18. TRIO-01 (full) — thumbs down, partial

**Question:** A column of my dataset holds diagnoses as people typed them. How do I turn that column into standard ontology terms and into codes of a coding system such as ICD-10-CM — and know which results I can rely on?

**Reference:** [TRIO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md)

**Captured:** 2026-11-11T14:16:27.495Z · DocBot message id 13126 · [capture file](answers/18-TRIO-01.md)

**Earlier runs:** 28 Oct 👎 · 28 Oct rerun 👎 · 9 Nov 👎 · answer unchanged in substance since 9 Nov

**Answer:**

> To map a column of free-text diagnoses to standard ontology terms and ICD-10-CM codes, follow this multi-stage process:
>
> 1. **Prepare your data:** Remove duplicates from your column so that each unique diagnosis is listed only once.
> 2. **Propose terms with [Zooma](https://www.ebi.ac.uk/spot/zooma):** Enter your unique values into [Zooma](https://www.ebi.ac.uk/spot/zooma), selecting a common ontology like MONDO as your target.
> 3. **Review and refine with [OLS](https://www.ebi.ac.uk/ols4):**
>
> - Accept suggestions with a confidence of 90% or higher.
> - For suggestions with lower confidence, or those that are ambiguous, use [OLS](https://www.ebi.ac.uk/ols4) to check definitions, synonyms, and parent terms. Replace incorrect terms by searching [OLS](https://www.ebi.ac.uk/ols4) or using [Zooma](https://www.ebi.ac.uk/spot/zooma)’s alternatives.
> 4. **Translate to codes with [OxO](https://www.ebi.ac.uk/spot/oxo):** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to map your agreed-upon ontology terms to ICD-10-CM codes.
>
> - Filter by “Asserted only” for direct mappings.
> - If no asserted code exists, check for inferred mappings or look up the parent term’s code in [OLS](https://www.ebi.ac.uk/ols4) and [OxO](https://www.ebi.ac.uk/spot/oxo).
> 5. **Assemble:** Create a table containing the original value, the chosen term, the code, and a record of how each was determined. Join this back to your original dataset.
>
> **Evaluating Reliability:**
>
> - **Confidence Scores:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) confidence scores to prioritize manual review; review everything below 90%.
> - **Manual Verification:** For codes without labels or those derived from inferred mappings, verify the meaning directly in the coding system or by inspecting the derivation path in [OxO](https://www.ebi.ac.uk/spot/oxo).
> - **Documentation:** Record the date of your run, as ontologies and mappings are updated over time.
>
> Would you like to know more about using the [OxO](https://www.ebi.ac.uk/spot/oxo) API for batch mapping?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-02-map-list-to-target.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Identical to the 9 November answer. The five-stage workflow is right, but the reliability safeguards the question asks for are still incomplete: broader parent codes are not flagged as broader, inferred mappings are validated too loosely, unresolved values are not left for manual coding, and choosing between several asserted codes is missing.

*Correct:*
- deduplicate values first
- Zooma with MONDO as target
- accept at 90%+, review lower or ambiguous suggestions in OLS; alternatives via thumbs down or OLS search
- OxO Multiple terms to ICD10CM with Asserted only
- inferred mappings or parent code as fallback
- assemble a table with provenance and rejoin to the dataset
- review everything below 90%; look up codes without labels; record the date

*Gaps:*
- a parent's code is broader than the term and must be marked as such (step 12)
- validation of an inferred mapping: accept only if the published mappings behind it link terms with the same meaning; checking the code's meaning alone is not sufficient
- values that cannot be coded should be left for manual coding
- where a term has several asserted codes, choose the one at the same level of generality (step 11)
- several green suggestions for one value also need review; 'Did not map' group not named
- run a sample first to estimate the review effort

*Errors:*
- none

**Proposed feedback (thumbs down, not submitted):** 11 November run, TRIO-01: unchanged from 9 November, so the same reliability gaps remain. When a parent term's code is used, say and record that it is broader than the original term; for inferred mappings, accept only when the asserted premises in Mapping Details link equivalent meanings (checking the code's meaning alone is not enough); leave values with no code for manual coding; and say how to choose between several asserted codes. Source: use case TRIO-01 steps 11 and 12.

### 19. TRIO-02 (full) — thumbs up, pass

**Question:** My data were annotated with ontology terms some years ago. Which of those terms have since been made obsolete, and what should each be replaced with?

**Reference:** [TRIO-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-02-update-outdated-annotations.md)

**Captured:** 2026-11-11T14:18:15.628Z · DocBot message id 13128 · [capture file](answers/19-TRIO-02.md)

**Answer:**

> To determine which of your ontology terms are obsolete and find their replacements, you should follow a three-step process, stopping at the first tool that provides an answer for each term:
>
> 1. **[OLS](https://www.ebi.ac.uk/ols4):** Check if the term is obsolete and if the ontology explicitly records a replacement. Search for your term identifier in [OLS](https://www.ebi.ac.uk/ols4) with the “Include obsolete terms” option enabled. If the term is obsolete, the page will indicate if a “Replaced by” value is provided.
> 2. **[OxO](https://www.ebi.ac.uk/spot/oxo):** If [OLS](https://www.ebi.ac.uk/ols4) does not name a replacement, use [OxO](https://www.ebi.ac.uk/spot/oxo) to find a successor through mappings. Ensure you tick “Obsolete terms” under “More options” to include them in your search. Prefer results with an exact match, a small distance, and a label that matches your original term.
> 3. **[Zooma](https://www.ebi.ac.uk/spot/zooma):** If no mappings are found, use [Zooma](https://www.ebi.ac.uk/spot/zooma) to find a current term that matches the wording of your original annotation. Use the original free-text value if available, or the old term’s label (with any “obsolete” prefix removed).
>
> For any replacement found, you must verify it in [OLS](https://www.ebi.ac.uk/ols4) to ensure the definition fits the context of your data. If a term remains unresolved after these steps, it requires a manual decision based on your data’s context.
>
> Would you like to know more about using the [OLS](https://www.ebi.ac.uk/ols4) API to automate these checks?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-05-check-obsolete-term.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-06-search-returns-nothing.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-02-update-outdated-annotations.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate three-step order (OLS, then OxO with Obsolete terms ticked, then Zooma from the wording), with the final OLS check and the manual-decision fallback.

*Correct:*
- stop at the first tool that answers
- OLS with Include obsolete terms; Replaced by
- OxO with Obsolete terms under More options; prefer exact match, small distance, matching label
- Zooma with the original free text or the old label minus the obsolete prefix
- verify replacement in OLS; unresolved terms need a manual decision

*Gaps:*
- record old -> new with how it was found, keep the table with the date
- Reason field may suggest an alternative
- replacement is not always one for one (split or merged terms)
- API calls (left to a follow-up)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, TRIO-02: accurate against the use case. Additions: keep a dated old -> new table noting how each replacement was found, read the Reason field when no replacement is named, and warn that an obsolete term may have been split or merged rather than replaced one for one.

### 20. TRIO-03 (full) — thumbs up, pass

**Question:** I want to analyse two datasets together. One records diagnoses as free text, the other as codes from several coding systems. How do I bring both to a common set of terms, so that I can match records and group them?

**Reference:** [TRIO-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md)

**Captured:** 2026-11-11T14:18:31.189Z · DocBot message id 13130 · [capture file](answers/20-TRIO-03.md)

**Answer:**

> To map two datasets with different diagnosis formats to a common set of terms, you can use [Zooma](https://www.ebi.ac.uk/spot/zooma), [OxO](https://www.ebi.ac.uk/spot/oxo), and [OLS](https://www.ebi.ac.uk/ols4) by following these steps:
>
> - **Choose a common ontology:** Use [OLS](https://www.ebi.ac.uk/ols4) to select an ontology (e.g., Mondo) that covers the subject matter and is well-connected to your coding systems.
> - **Map free-text to the ontology:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map the unique values from your free-text dataset to terms in your chosen ontology. Accept suggestions or verify them using [OLS](https://www.ebi.ac.uk/ols4).
> - **Translate codes to the ontology:** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate your coded dataset values into the same ontology. Paste your codes (formatted as prefix:code) into [OxO](https://www.ebi.ac.uk/spot/oxo), select your common ontology, and set the “Max distance” to 1 to ensure direct mappings.
> - **Group the terms:** Use [OLS](https://www.ebi.ac.uk/ols4) to identify the broader groups (ancestors) for each term. Choose a level in the hierarchy that effectively separates the groups you need.
> - **Combine:** Add the resulting term and group to every record in both datasets. Records sharing the same term represent the same entity, while those sharing the same group belong together at a broader level.
>
> Would you like to see the API request format for mapping free-text to Mondo?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate overall workflow, and gets the key OxO detail right: codes written as prefix:code and Max distance 1 for direct mappings into the common ontology.

*Correct:*
- choose a common ontology in OLS (Mondo)
- Zooma for unique free-text values, verified in OLS
- OxO with codes as prefix:code, target the common ontology, Max distance 1
- group by OLS ancestors at a chosen level
- add term and group to every record

*Gaps:*
- why not Asserted only in this direction (published direction is ontology -> code)
- codes with several or no rows: compare in OLS or raise Max distance
- keep the original value or code beside the new term; terms can have several parents
- record date, ontology version and OxO data release
- API calls (left to a follow-up)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, TRIO-03: accurate against the use case, including Max distance 1 for the code-to-ontology step. Additions: say explicitly not to use Asserted only in that direction and why, what to do when a code gets several rows or none, and to keep the original codes beside the new terms.

### 21. PAIR-01 (full) — thumbs up, pass

**Question:** Zooma has suggested a term for my value, but with a confidence below 90% — or it has suggested several. Is the suggestion right, and how do I check?

**Reference:** [PAIR-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md)

**Captured:** 2026-11-11T14:18:39.749Z · DocBot message id 13132 · [capture file](answers/21-PAIR-01.md)

**Answer:**

> To verify a [Zooma](https://www.ebi.ac.uk/spot/zooma) suggestion that has a confidence score below 90% or when multiple suggestions are provided, you should perform the following steps:
>
> - **Review the Prediction Type:** In the Results table, click on the value in the “Prediction Type” column to open the Mapping Provenance window. This explains how the suggestion was found (e.g., Curated, Lexical, Embedding, or Replace obsolete) and what your text was matched against.
> - **Check the term in [OLS](https://www.ebi.ac.uk/ols4):** Click the Term ID in the Results table to open the term in [OLS](https://www.ebi.ac.uk/ols4). Review the term’s definition, synonyms, and its position within the ontology hierarchy to ensure it is contextually appropriate.
> - **Evaluate alternatives:** If the initial suggestion is incorrect, click the thumbs down icon on the row to view all candidates [Zooma](https://www.ebi.ac.uk/spot/zooma) has found. Check any promising alternatives in [OLS](https://www.ebi.ac.uk/ols4) using the same review process before selecting one and clicking CONFIRM.
> - **Maintain a record:** Since the review icons on the website are not saved and do not update the downloaded results file, you must manually record your final decisions (e.g., “accepted,” “replaced,” or “chosen by hand”) in your own working file (such as the downloaded `zooma_results.tsv`).
>
> Would you like to know how to use the [OLS](https://www.ebi.ac.uk/ols4) API to programmatically check term ancestors?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate review loop: Mapping Provenance, Term ID into OLS for definition, synonyms and hierarchy, thumbs-down alternatives checked the same way, and decisions recorded outside Zooma.

*Correct:*
- Prediction Type -> Mapping Provenance and its meaning
- Term ID -> OLS: definition, synonyms, hierarchy
- thumbs down -> candidates, check in OLS, CONFIRM
- icons not saved; record decisions in a working file

*Gaps:*
- use row colours to pick the rows to check; Embedding suggestions deserve the closest look
- check the deprecated status box in OLS
- move to a parent or child in the Tree when the term is too broad or narrow
- if no candidate fits, find a term by hand (PAIR-06)
- spot-check green rows too

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-01: accurate against the use case. Additions: pick rows by colour (yellow below 90% or several high-confidence suggestions, grey low), look hardest at Embedding suggestions, check the deprecated box in OLS, move up or down the Tree when a term is too broad or narrow, and fall back to a manual search when no candidate fits.

### 22. PAIR-02 (full) — thumbs down, partial

**Question:** I know the concept in words — say heart attack. What is the ontology term for it, and what are the corresponding codes in other vocabularies, such as ICD-10-CM, MeSH and SNOMED CT?

**Reference:** [PAIR-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-02-find-term-and-translate.md)

**Captured:** 2026-11-11T14:20:14.761Z · DocBot message id 13134 · [capture file](answers/22-PAIR-02.md)

**Answer:**

> The ontology term for “heart attack” is **myocardial infarction**, which has the identifier **MONDO:0005068**.
>
> To find the corresponding codes in other vocabularies, you can use [OxO](https://www.ebi.ac.uk/spot/oxo) to map this identifier. The asserted mappings for this term include:
>
> - **MeSH**: MESH:D009203
> - **ICD-10-CM**: ICD10CM:I21 (Acute myocardial infarction)
> - **SNOMED CT**: SCTID:22298006
>
> These mappings are based on the `SKOS:exactMatch` predicate. Please note that mappings should be carefully evaluated, as both asserted and inferred mappings may be incorrect.
>
> Would you like to know how to perform this mapping using the [OxO](https://www.ebi.ac.uk/spot/oxo) API?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-02-find-term-and-translate.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Answers the example only: the term and the three asserted codes match the use case exactly, but the OLS half of the workflow is absent and the OxO half is a bare pointer.

*Correct:*
- myocardial infarction MONDO:0005068
- MESH:D009203, ICD10CM:I21, SCTID:22298006 as asserted SKOS:exactMatch
- mappings may be wrong and need evaluating

*Gaps:*
- no OLS step: search the concept, tick MONDO, confirm the definition, copy the identifier
- no OxO procedure: paste the identifier, choose To ontologies (ICD10CM, MESH, SCTID), prefer Asserted exact matches, inspect inferences with the eye icon
- prefix note (SCTID, ICD10CM) and that ICD-10-CM codes are not in OLS
- nothing a user with a different concept can act on

*Errors:*
- none

**Proposed feedback (thumbs down, not submitted):** 11 November run, PAIR-02: the example result is right (MONDO:0005068; MESH:D009203, ICD10CM:I21, SCTID:22298006) but the method is missing. The use case is a two-tool procedure: search OLS for the concept, tick MONDO, confirm the definition and copy the identifier; then in OxO paste it, choose ICD10CM, MESH and SCTID under To ontologies, prefer Asserted exact matches and open inferences before using them. Please give the steps, not only the example's answer.

### 23. PAIR-03 (full) — thumbs up, pass

**Question:** OxO says two terms are an exact match. Before I merge data on the strength of that, do the two terms really mean the same thing?

**Reference:** [PAIR-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-03-validate-a-mapping.md)

**Captured:** 2026-11-11T14:20:23.825Z · DocBot message id 13136 · [capture file](answers/23-PAIR-03.md)

**Earlier runs:** 28 Oct 👍 · 28 Oct rerun 👍 · 9 Nov 👍 · answer rewritten since 9 Nov

**Answer:**

> To verify if two terms identified as an exact match by [OxO](https://www.ebi.ac.uk/spot/oxo) truly have the same meaning, you should evaluate the mapping evidence and compare the terms using [OLS](https://www.ebi.ac.uk/ols4).
>
> **Evaluate the Mapping Evidence**
>
> In the [OxO](https://www.ebi.ac.uk/spot/oxo) results table, examine the specific row for the mapping:
>
> - **Check the metadata:** Review the Predicate, Type, Mapping justification, and Distance.
> - **Inspect details:** Click the eye icon to open Mapping Details. For asserted mappings, check who published it and how it was made. For inferred mappings, identify the weakest link in the derivation chain (e.g., automatic label matching).
> - **Consider the context:** Remember that “exact match” is a claim made by the publisher for their specific purposes. Whether it is sufficient for your needs depends on your use case (e.g., retrieving literature vs. counting patients).
>
> **Compare the Terms in [OLS](https://www.ebi.ac.uk/ols4)**
>
> Click the [OLS](https://www.ebi.ac.uk/ols4) link for both the subject and object to compare them side-by-side:
>
> - **Definitions:** Determine if they describe the same substance or if one is a cause, consequence, part, or special case of the other.
> - **Hierarchy (Tree):** Follow the paths upward to ensure they are the same kind of thing.
> - **Synonyms:** Check if each term lists the other’s label or a similar term.
> - **Children:** Expand the trees; if one term has children that the other lacks, it may be broader.
> - **Class Information:** Check if the ontology includes a `database_cross_reference` to the other term.
>
> **Decide on the Outcome**
>
> Based on your comparison, choose one of the following:
>
> - **Accept:** The terms have the same definition and are the same kind of thing; treat them as equivalent.
> - **Downgrade:** The terms are closely related but not identical (e.g., broader/narrower); keep the link but do not merge records.
> - **Reject:** The terms mean different things; do not use the mapping.
>
> If you conclude a published mapping is incorrect, you can identify the source in the Mapping Set section of the details page to report it.
>
> Would you like to know how to use the [OxO](https://www.ebi.ac.uk/spot/oxo) API to fetch these mappings for automated comparison?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** More complete than on 9 November: evidence columns and Mapping Details, five-point OLS comparison, accept/downgrade/reject with no merging on a downgrade, and the reporting route.

*Correct:*
- Predicate, Type, Mapping justification, Distance; eye icon; weakest link of an inference
- exact match is the publisher's claim; depends on use
- definitions, Tree, synonyms, children, database_cross_reference
- accept / downgrade (do not merge) / reject
- Mapping Set identifies the publisher to report to

*Gaps:*
- differing labels as the cheapest warning sign; Max distance to prefer short derivations; terms without a label in OxO

*Errors:*
- wording slip: 'describe the same substance' where the use case means 'the same thing in substance'

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-03: accurate and fuller than on 9 November, covering evidence, comparison, decision and reporting. One wording slip: 'describe the same substance' should read 'describe the same thing'. Optional additions: differing labels as a first warning sign and the Max distance filter.

### 24. PAIR-04 (full) — thumbs up, pass

**Question:** I need every code that belongs to a subject area — for example, to select all records about diabetes. Which terms does an ontology place under diabetes mellitus, and which codes in my coding system (say ICD-10-CM) correspond to them?

**Reference:** [PAIR-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-04-code-list-for-branch.md)

**Captured:** 2026-11-11T14:20:32.884Z · DocBot message id 13138 · [capture file](answers/24-PAIR-04.md)

**Answer:**

> To retrieve all ontology terms under a specific subject area like ‘diabetes mellitus’ and map them to a coding system such as ICD-10-CM, you can use [OLS](https://www.ebi.ac.uk/ols4) and [OxO](https://www.ebi.ac.uk/spot/oxo) by following these steps:
>
> 1. **List the branch in [OLS](https://www.ebi.ac.uk/ols4):**
>
> - Find the term that defines your area (e.g., diabetes mellitus, MONDO:0005015).
> - Use the Tree panel to confirm the branch covers the desired terms.
> - For a large number of terms, use the [OLS](https://www.ebi.ac.uk/ols4) API to request the descendants of the term.
> 2. **Translate the branch using [OxO](https://www.ebi.ac.uk/spot/oxo):**
>
> - Open [OxO](https://www.ebi.ac.uk/spot/oxo) and select “Multiple terms.”
> - Paste the identifiers (the top term and all its descendants), one per line.
> - In “To ontologies,” select the target coding system (e.g., ICD10CM).
> - Click the filter icon in the “Type” column header and select “Asserted only” to keep published mappings.
> - Download the result as an SSSOM file.
>
> If a term has no asserted code, you can search [OxO](https://www.ebi.ac.uk/spot/oxo) again without the “Asserted only” filter to check for inferred mappings, or look up the term’s parent in [OLS](https://www.ebi.ac.uk/ols4) to see if the parent has a broader code available.
>
> Would you like to know more about using the [OxO](https://www.ebi.ac.uk/spot/oxo) API for batch mapping?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-04-code-list-for-branch.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: top term (MONDO:0005015), Tree check, API descendants for large branches, OxO Multiple terms with Asserted only and download, and both fallbacks for terms without a code.

*Correct:*
- diabetes mellitus MONDO:0005015; confirm branch in the Tree
- API for descendants of a large branch
- OxO Multiple terms, To ontologies ICD10CM, Asserted only, SSSOM download
- no code: inferred mappings, or parent's broader code

*Gaps:*
- how to find the terms without a code (Subject column, or unmappedInputs via batch-map)
- hierarchicalDescendants endpoint and the 500/1,000 limits
- expect many unmapped terms; the choice of top term decides the list (codes outside E08-E13)
- record date and ontology version

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-04: accurate against the use case. Additions: say how to list the terms without a code (compare the Subject column, or read unmappedInputs from the batch-map API), name the hierarchicalDescendants endpoint, and warn that the choice of top term decides the list, e.g. gestational and neonatal diabetes map outside the E08-E13 block.

### 25. PAIR-05 (full) — thumbs up, pass

**Question:** My values are free text, but the system I am loading them into wants identifiers from one particular vocabulary — MeSH headings for literature searching, say, or ICD-10-CM codes. How do I get from the text to those identifiers?

**Reference:** [PAIR-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md)

**Captured:** 2026-11-11T14:22:20.859Z · DocBot message id 13140 · [capture file](answers/25-PAIR-05.md)

**Answer:**

> To map free-text values to identifiers from a specific vocabulary, you can use a two-step process involving [Zooma](https://www.ebi.ac.uk/spot/zooma) and [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> **Step 1: Map text to a bridging ontology**
>
> Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to convert your free-text values into ontology terms.
>
> - Enter your values into [Zooma](https://www.ebi.ac.uk/spot/zooma).
> - Select a “bridging” ontology that is well-mapped to other vocabularies (e.g., MONDO for diseases).
> - Review the suggestions and carry forward only those you are satisfied with.
> - Ensure the term identifiers are formatted with a colon (e.g., change `MONDO_0005068` to `MONDO:0005068`).
>
> **Step 2: Translate terms to the target vocabulary**
>
> Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate the ontology terms into your target vocabulary (e.g., MESH or ICD10CM).
>
> - Open [OxO](https://www.ebi.ac.uk/spot/oxo) and select “Multiple terms.”
> - Paste your list of ontology identifiers.
> - In “To ontologies,” select your target vocabulary.
> - Click “Search” and set the Type filter to “Asserted only.”
> - Download the results to obtain the target identifiers.
>
> If a term has no mapping in [OxO](https://www.ebi.ac.uk/spot/oxo), you can use [OLS](https://www.ebi.ac.uk/ols4) to browse the ontology hierarchy, find a broader parent term, and check if that parent has a mapping in [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> Would you like to know how to perform these steps using the APIs?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate two-step workflow with the right details (custom bridging ontology, carry forward only accepted suggestions, underscore to colon, Asserted only) and a sensible parent-code fallback.

*Correct:*
- Zooma to a bridging ontology such as MONDO
- carry forward only satisfactory suggestions
- MONDO_0005068 -> MONDO:0005068
- OxO Multiple terms, To ontologies, Asserted only, download
- OLS parent as fallback

*Gaps:*
- why two steps: ICD-10-CM is not in OLS and mapping straight to MeSH performs worse
- join the two files on the term identifier (textToMap -> ontologyTermID; subject_id -> object_id)
- list the values that fell out at either step and handle them by hand
- inferred mappings judged one by one; one term may have several or no target identifiers

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-05: accurate against the use case. Additions: explain why two steps are needed (ICD-10-CM is not in OLS; Zooma straight to MeSH does worse), describe joining Zooma's file to OxO's on the term identifier, and say to list the values lost at either step for manual handling.

### 26. PAIR-06 (full) — thumbs up, pass

**Question:** Zooma found nothing for one of my values, or nothing that fits. How do I find the right term myself — and what do I do if there isn't one?

**Reference:** [PAIR-06](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md)

**Captured:** 2026-11-11T14:22:29.927Z · DocBot message id 13142 · [capture file](answers/26-PAIR-06.md)

**Answer:**

> If [Zooma](https://www.ebi.ac.uk/spot/zooma) cannot map a value, you should look for a term manually using [OLS](https://www.ebi.ac.uk/ols4) by following these steps:
>
> - **Search with the value’s words:** Type the value into the “Search OLS…” box and press Enter. Ensure you tick the relevant ontologies under the “Ontology” filter on the left.
> - **Search with other words:** Try using technical names instead of everyday language, full names instead of abbreviations, or singular forms instead of plurals.
> - **Search by meaning:** Set the “Search Model” to an embedding model to find terms that share the same meaning even if they do not share the same words.
> - **Browse the hierarchy:** Find a broader term that applies (e.g., an organ or disease group), open it, and expand the “Tree” panel to look through its children for a match.
>
> When you find a candidate, verify it by checking its definition and parent terms before using its identifier.
>
> **If no suitable term exists:**
>
> - **Use a broader term:** If the nearest available term is broader than your value, use that broader term and keep your original text alongside it to ensure no information is lost.
> - **Request a new term:** If nothing fits, open the ontology’s page in [OLS](https://www.ebi.ac.uk/ols4) and use its “Issue Tracker” button (if provided) to contact the maintainers. Describe the concept, provide a definition, and suggest where the term should be placed in the hierarchy.
>
> Would you like to know how to use the [OLS](https://www.ebi.ac.uk/ols4) API to perform these searches programmatically?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate OLS search ladder (words, other words, meaning, browse), verification advice, and both no-term outcomes (broader term with original text kept; request via Issue Tracker).

*Correct:*
- search with the value's words, tick ontologies
- technical names, full names, singular
- Search Model -> embedding model
- browse a broader term's Tree
- verify definition and parents
- use a broader term and keep the original text
- Issue Tracker request with concept, definition and placement

*Gaps:*
- first look through Zooma's longer candidate list via thumbs down
- how to collect the leftover values (Did not map, grey, rejected)
- expand abbreviations and fix misspellings, then retry Zooma
- some values should not be mapped ('not recorded', 'other')
- keep the value -> term decisions

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-06: accurate against the use case. Additions: start with Zooma's thumbs-down candidate list before searching by hand, expand abbreviations and correct misspellings and retry Zooma, and note that values like 'not recorded' should not be forced onto a term.

### 27. ZOOMA-01 (full) — thumbs up, partial

**Question:** I have a list of free-text values — sample attributes, column values, questionnaire answers. Which ontology term best matches each of them?

**Reference:** [ZOOMA-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-01-map-list-of-values.md)

**Captured:** 2026-11-11T14:22:38.992Z · DocBot message id 13144 · [capture file](answers/27-ZOOMA-01.md)

**Answer:**

> To find the best matching ontology terms for your list of free-text values, you can use [Zooma](https://www.ebi.ac.uk/spot/zooma).
>
> Follow these steps:
>
> 1. Open [Zooma](https://www.ebi.ac.uk/spot/zooma).
> 2. Under “1 Enter strings to map,” ensure you are on the “Map Strings” tab and paste your values into the box, one per line.
> 3. Optionally, provide the “kind” of thing each value describes (e.g., “disease” or “organism part”) by pressing the Tab key after the value and typing the category. This helps [Zooma](https://www.ebi.ac.uk/spot/zooma) rank suggestions more accurately.
> 4. Click the green button (e.g., “Map X strings”) to receive suggested terms, their confidence scores, and the provenance of the suggestions.
>
> If you are unsure which ontologies to target, you can browse them first in [OLS](https://www.ebi.ac.uk/ols4). If [Zooma](https://www.ebi.ac.uk/spot/zooma) does not provide a suitable term, you can search for one manually in [OLS](https://www.ebi.ac.uk/ols4) using technical names, synonyms, or by browsing the hierarchy.
>
> Would you like to know how to use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate these ontology terms into specific coding systems?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-01-map-list-of-values.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Correct input procedure (Map Strings, one per line, Tab for the kind, Map N strings) but says little about reading the results and nothing about download or the limits of the confidence score.

*Correct:*
- Map Strings tab, one value per line
- Tab then the kind as context
- green Map N strings button
- suggestions with confidence and provenance
- OLS to choose ontologies or to search by hand

*Gaps:*
- Results columns (Term ID opens OLS, Source, Prediction Type)
- row colours and Did not map
- Download as TSV (zooma_results.tsv)
- confidence is a ranking score: check non-green rows and spot-check green ones
- choosing target ontologies improves results
- API call

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-01: input steps are right. Please add how to read the Results table (Term ID opens OLS, Source, Prediction Type, row colours, Did not map), the TSV download, and the caveat that the confidence is a ranking score, so non-green rows need checking and green ones spot-checking.

### 28. ZOOMA-02 (full) — thumbs up, pass

**Question:** My project annotates with particular ontologies. How do I make Zooma suggest terms from those ontologies only — or prefer them over others?

**Reference:** [ZOOMA-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md)

**Captured:** 2026-11-11T14:24:07.733Z · DocBot message id 13146 · [capture file](answers/28-ZOOMA-02.md)

**Answer:**

> To configure [Zooma](https://www.ebi.ac.uk/spot/zooma) to suggest or prefer terms from specific ontologies, you can define a custom list of ontologies in order of preference. The first ontology in your list that contains a good match will be prioritized.
>
> **On the website**
>
> 1. Open [Zooma](https://www.ebi.ac.uk/spot/zooma) and enter your values.
> 2. Click the heading **3 Which ontologies to map to?** to open the section.
> 3. Open the list at the top of the section and select **Choose custom ontologies**.
> 4. Build your list by adding the ontologies you want to use, ensuring they are ordered by your preference (not alphabetically).
>
> **Using the API**
>
> You can specify your preferred ontologies using the `targetOntologies` parameter in your JSON request. For example:
>
> ```
> {
>   "properties": [{"textToMap": "heart attack"}],
>   "targetOntologies": ["mondo", "hp"],
>   "includeOtherOntologies": false
> }
> ```
>
> When you provide an ordered list, [Zooma](https://www.ebi.ac.uk/spot/zooma) will provide a single answer based on your priority. If you do not provide a list, [Zooma](https://www.ebi.ac.uk/spot/zooma) may return multiple suggestions from different ontologies when equally good matches exist. Note that when you build a custom list, `includeOtherOntologies` is unticked by default.
>
> Would you like to know how to use [OLS](https://www.ebi.ac.uk/ols4) to browse ontologies before adding them to your [Zooma](https://www.ebi.ac.uk/spot/zooma) configuration?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate: custom ontology list in order of preference, the API example, single answer with an ordered list, and the default state of Include results from other ontologies.

*Correct:*
- section 3, Choose custom ontologies, order by preference
- targetOntologies and includeOtherOntologies example
- ordered list gives one answer; none gives several
- includeOtherOntologies unticked by default for a custom list

*Gaps:*
- presets and All ontologies (not recommended)
- Include results from other ontologies tick box on the website
- ontology-presets API

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-02: accurate against the use case. Minor additions: the presets and the Include results from other ontologies tick box on the website.

### 29. ZOOMA-03 (full) — thumbs up, pass

**Question:** My values are in a column of a spreadsheet, perhaps with a second column saying what kind of thing each value is. How do I get ontology terms for that column without retyping it?

**Reference:** [ZOOMA-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md)

**Captured:** 2026-11-11T14:24:15.794Z · DocBot message id 13148 · [capture file](answers/29-ZOOMA-03.md)

**Answer:**

> To map values from a spreadsheet column to ontology terms using [Zooma](https://www.ebi.ac.uk/spot/zooma), follow these steps:
>
> 1. **Prepare your file:** Save or export your spreadsheet as a CSV, TSV, or plain text file.
> 2. **Upload:** Open [Zooma](https://www.ebi.ac.uk/spot/zooma) and click **Upload CSV** to select your file.
> 3. **Configure layout:** In the CSV Import Preview window, verify the delimiter and quote character settings. Ensure **First row is header** is ticked if your file includes column names.
> 4. **Map columns:**
>
> - Set the **Term column** to the column containing the values you wish to map.
> - Set the **Type column** to the column that describes the kind of thing each value is (e.g., “disease” or “organism part”). If you do not have a type column, set this to **None**.
> 5. **Import and Map:** Click the **Import** button. Once the values appear in the Map Strings box, click the **Map** button to process them.
> 6. **Download:** Review the results and click the download icon next to the Results heading to save the output as a `zooma_results.tsv` file.
> 7. **Join:** You can join the downloaded file back to your original spreadsheet by matching the `textToMap` and `propertyType` columns to the original values and types.
>
> For large datasets, it is recommended to remove duplicates from your column before uploading to save time, as you can join the results back to the full column later.

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate: export as CSV/TSV, Upload CSV, the preview settings, Term and Type columns, Import then Map, download and join on textToMap and propertyType, deduplicate first.

*Correct:*
- save as CSV/TSV/TXT; Upload CSV
- Delimiter, Quote character, First row is header
- Term column, Type column or None
- Import, then Map
- zooma_results.tsv; join on textToMap and propertyType
- remove duplicates first

*Gaps:*
- Zooma pre-selects the first two columns as Term and Type, so check both
- imported values are added to the existing box: Clear first
- several suggestions per value: decide which to keep before joining

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-03: accurate against the use case. Additions: warn that Zooma pre-selects the first column as Term and the second as Type, and that imported values are added to what is already in the box.

### 30. ZOOMA-04 (full) — thumbs up, pass

**Question:** I have a sentence or paragraph — a sample description, a clinical note, part of a methods section. Which parts of it can be annotated with ontology terms, and with which terms?

**Reference:** [ZOOMA-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-04-annotate-free-text.md)

**Captured:** 2026-11-11T14:24:24.855Z · DocBot message id 13150 · [capture file](answers/30-ZOOMA-04.md)

**Answer:**

> To annotate parts of a sample description, clinical note, or methods section, you can use [Zooma](https://www.ebi.ac.uk/spot/zooma) or [OLS](https://www.ebi.ac.uk/ols4).
>
> **Using [Zooma](https://www.ebi.ac.uk/spot/zooma)**
>
> The “Annotate Text” tab in [Zooma](https://www.ebi.ac.uk/spot/zooma) identifies phrases within your text and suggests ontology terms for them based on a confidence score.
>
> 1. Navigate to the **Annotate Text** tab.
> 2. Paste your text into the input box.
> 3. Select your desired ontologies under **Which ontologies to map to?**. This step is critical, as your selection determines which phrases [Zooma](https://www.ebi.ac.uk/spot/zooma) identifies.
> 4. Click **Annotate Text**.
>
> **Using [OLS](https://www.ebi.ac.uk/ols4)**
>
> The “Tag Text” feature in [OLS](https://www.ebi.ac.uk/ols4) highlights stretches of text that match existing term labels or previously curated mappings.
>
> 1. Navigate to the **Tag Text** page.
> 2. Paste or type your text into the box.
> 3. [OLS](https://www.ebi.ac.uk/ols4) will automatically highlight matches. You can view the results in the **Matched Terms** list, which provides the Term IRI, Term Label, Ontology, and Match Type (LABEL or CURATION).
>
> **Determining which terms to use**
>
> - **Refine by Ontology:** If you receive too many matches, use the Ontologies panel to restrict your search to specific ontologies.
> - **Manual Mapping:** If a specific word is not picked up, you can map it separately using the **Map Strings** tab in [Zooma](https://www.ebi.ac.uk/spot/zooma).
> - **Search by Meaning:** If a concept is worded differently than its label, [OLS](https://www.ebi.ac.uk/ols4) will not find it automatically. In such cases, use the search functionality in [OLS](https://www.ebi.ac.uk/ols4) to search by meaning (using an embedding model) or browse the hierarchy to find a broader term that fits.
>
> Would you like to know how to handle cases where no suitable ontology term can be found?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-06-find-term-when-zooma-cannot.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-04-annotate-free-text.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-06-tag-text.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate on both tools: Annotate Text with the ontology choice flagged as critical, OLS Tag Text with its result columns, and sensible advice for words not picked up.

*Correct:*
- Annotate Text tab; paste; choose ontologies (critical); Annotate Text button
- OLS Tag Text and Matched Terms columns
- map missed words separately on Map Strings
- restrict by ontology; search by meaning in OLS

*Gaps:*
- reading the annotated text (coloured phrase labels), clicking a phrase, discarding with x
- download zooma_results.tsv
- a phrase with two green suggestions needs a decision
- annotate-text-stream API

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-04: accurate against the use case. Additions: how the annotated text is shown (coloured phrase labels, click to highlight, x to discard), the download, and that a phrase with two green suggestions needs a decision.

### 31. ZOOMA-05 (full) — thumbs up, pass

**Question:** Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

**Reference:** [ZOOMA-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md)

**Captured:** 2026-11-11T14:25:53.062Z · DocBot message id 13152 · [capture file](answers/31-ZOOMA-05.md)

**Earlier runs:** 28 Oct 👍 · 28 Oct rerun 👍 · 9 Nov 👍 · answer unchanged in substance since 9 Nov

**Answer:**

> To understand why [Zooma](https://www.ebi.ac.uk/spot/zooma) suggested a specific term, click on the value in the “Prediction Type” column of the mapping results table to open the Mapping Provenance window. This window displays what your text was matched against, which often explains the reasoning behind a suggestion.
>
> If the suggested term is incorrect, you can find alternatives by clicking the “thumbs down” icon on the row. This opens the “Select Mapping” window, which lists every candidate [Zooma](https://www.ebi.ac.uk/spot/zooma) found, ordered by confidence. You can review these candidates in [OLS](https://www.ebi.ac.uk/ols4) to check their definitions, synonyms, and hierarchy to determine if a better fit exists.
>
> To keep a record of your decisions:
>
> - **Do not rely on the website icons:** The thumbs up, thumbs down, and bin icons only change the display on your screen; they are not saved, are not sent to [Zooma](https://www.ebi.ac.uk/spot/zooma), and are not reflected in the downloaded results file.
> - **Maintain a working file:** Download your results as a TSV file and add a column to record your decisions, the date, and the settings used. This file serves as your permanent record and allows you to quickly map the same values in the future.
>
> Would you like to know more about using the [Zooma](https://www.ebi.ac.uk/spot/zooma) API to retrieve mapping provenance?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Identical to the 9 November answer; accurate on Mapping Provenance, alternatives via thumbs down, OLS checks, and the warning that screen decisions are neither saved nor in the download.

*Correct:*
- Prediction Type -> Mapping Provenance
- thumbs down -> Select Mapping, candidates by confidence
- check candidates in OLS
- icons change only the screen; not saved, not sent, not in the download
- working file with decisions, date and settings

*Gaps:*
- record the replacement's label, identifier and IRI in the file since the download never contains alternatives
- meaning of the Prediction Type values
- API returnAll and deep

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-05: accurate, unchanged from 9 November. Small improvement: say to write the chosen alternative's label, identifier and IRI into the working file, because the download never contains it.

### 32. ZOOMA-06 (full) — thumbs up, pass

**Question:** Has a curator at one of the EMBL-EBI data resources already mapped this text to an ontology term? And how do I control which resources' curated mappings Zooma draws on?

**Reference:** [ZOOMA-06](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-06-reuse-curated-mappings.md)

**Captured:** 2026-11-11T14:26:02.123Z · DocBot message id 13154 · [capture file](answers/32-ZOOMA-06.md)

**Answer:**

> Yes, [Zooma](https://www.ebi.ac.uk/spot/zooma) draws on mappings previously made by curators at EMBL-EBI data resources. When your input text matches a previously curated mapping, [Zooma](https://www.ebi.ac.uk/spot/zooma) suggests the same term with high confidence and identifies the source resource in the “Source” column of the results.
>
> You can control which resources are used as follows:
>
> - **On the website:**
>
> - Open the “Where to get mappings?” section.
> - Click the × on a label to exclude a resource.
> - Click an excluded resource to include it again.
> - Drag the labels to reorder them; the resource in the first position has the highest priority.
> - **With the API:**
>
> - Use the `filter` parameter in your POST request to the `https://www.ebi.ac.uk/spot/zooma/v3/api/services/map` endpoint.
> - Specify resources to use in `filter.required` and resources to prefer in `filter.preferred`.
> - If you leave the `filter` parameter out, [Zooma](https://www.ebi.ac.uk/spot/zooma) will use all available resources.
>
> Note that [Zooma](https://www.ebi.ac.uk/spot/zooma) will not suggest a curated mapping if the target ontology has been excluded.
>
> Would you like to know how to view the provenance of a specific curated suggestion?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-06-reuse-curated-mappings.md

**Links in the answer:** Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate: curated mappings and their Source, the Where to get mappings controls (exclude, include, reorder), the filter.required / filter.preferred API, and the excluded-ontology caveat.

*Correct:*
- curated mappings suggested with high confidence; Source names the resource
- section 2 controls: x, click to include, drag to reorder
- filter.required and filter.preferred on services/map; omit filter for all
- curated mapping not suggested if its ontology is excluded

*Gaps:*
- Prediction Type reads Curated
- a curated mapping was made for a purpose: check it fits your use of the text
- Select all / Select none; sources API

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-06: accurate against the use case. Additions: Prediction Type reads Curated for such rows, and a curated mapping reflects the purpose of the resource that made it (cooked broccoli -> sulforaphane), so check that it fits your own use.

### 33. OLS-01 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have a concept in words, and I want its ontology term?

**Reference:** [OLS-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-01-find-term-for-concept.md)

**Captured:** 2026-11-11T14:26:11.188Z · DocBot message id 13156 · [capture file](answers/33-OLS-01-wts.md)

**Answer:**

> To find an ontology term for a concept described in words, you should start by using [OLS](https://www.ebi.ac.uk/ols4).
>
> 1. Open [OLS](https://www.ebi.ac.uk/ols4) and type your word or phrase into the “Search OLS…” box.
> 2. Press Enter or click Search to view the results.
> 3. You can narrow your results using the panel on the left:
>
> - Under **Type**, tick “Class” to focus on ontology terms.
> - Under **Ontology**, select the specific ontology you wish to use (e.g., MONDO for diseases).
> 4. Review the result cards, which provide the term’s label, identifier, definition, and the ontology it belongs to.
> 5. Click the label of the best match to confirm the definition and synonyms before using the term.
>
> If you do not know the specific wording used by ontologies, you can perform a semantic search by selecting an embedding model (such as `llama-embed-nemotron-8b_pca512`) from the “Search Model” list in [OLS](https://www.ebi.ac.uk/ols4) instead of the default lexical search.
>
> Would you like to know how to map these terms to other vocabularies using [OxO](https://www.ebi.ac.uk/spot/oxo)?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-01-find-term-for-concept.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Full and accurate procedure: search box, Type = Class, Ontology filter, result cards, confirm definition and synonyms, semantic search as alternative.

*Correct:*
- Search OLS box, Enter
- Type Class, Ontology e.g. MONDO
- result cards: label, identifier, definition, ontology
- confirm definition and synonyms
- embedding model for unknown wording

*Gaps:*
- no API call (acceptable for a where-to-start answer)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-01 (where to start): accurate and complete for the website; this is the method the full OLS-01 question should also receive.

### 34. OLS-07 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have a concept in mind, without knowing the correct words, and I want its ontology term?

**Reference:** [OLS-07](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-07-semantic-search.md)

**Captured:** 2026-11-11T14:27:35.842Z · DocBot message id 13158 · [capture file](answers/34-OLS-07-wts.md)

**Answer:**

> To find an ontology term for a concept when you do not know the correct terminology, you should use the [OLS](https://www.ebi.ac.uk/ols4) semantic search feature:
>
> 1. Open [OLS](https://www.ebi.ac.uk/ols4).
> 2. Type your phrase into the **Search OLS…** box.
> 3. Open the **Search Model** list under the search box and select an embedding model (e.g., `llama-embed-nemotron-8b_pca512`) instead of the default Lexical option.
> 4. Click **Search**. The results will be ranked by how similar their meaning is to your phrase, with a similarity score displayed next to each label.
>
> Always read the definition of the term you select, as these results are computed from language-model embeddings and have not been curated.
>
> Would you like to know how to filter these results by specific ontologies?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-07-semantic-search.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4

**Assessment:** Accurate embedding-search steps with the uncurated-results caveat.

*Correct:*
- Search Model -> embedding model
- similarity score shown
- always read the definition; results not curated

*Gaps:*
- Filter by ontology and Similar Classes not mentioned

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-07 (where to start): accurate, including the caveat that results are uncurated.

### 35. OLS-02 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have an identifier, and I want to know what it means?

**Reference:** [OLS-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-02-look-up-identifier.md)

**Captured:** 2026-11-11T14:27:45.401Z · DocBot message id 13160 · [capture file](answers/35-OLS-02-wts.md)

**Answer:**

> To find out what an identifier means, you should use [OLS](https://www.ebi.ac.uk/ols4). You can provide the identifier in any of the following formats:
>
> - A CURIE (e.g., MONDO:0005068)
> - The underscore form (e.g., MONDO_0005068)
> - The full IRI (e.g., [http://purl.obolibrary.org/obo/MONDO_0005068](http://purl.obolibrary.org/obo/MONDO_0005068))
>
> To look it up on the website:
>
> 1. Open [OLS](https://www.ebi.ac.uk/ols4).
> 2. Paste the identifier into the “Search OLS…” box.
> 3. In the drop-down, look under “Jump to” and click the entry for the term. If the term is listed multiple times, choose the entry whose ontology badge matches the identifier’s prefix. Alternatively, press Enter and open the result that is not marked “IMPORTED.”
> 4. Review the term’s label, definition, synonyms, cross-references, and relations on the resulting page.
>
> If you are using the API, you can search for the identifier using the following endpoint:
>
> `curl -s 'https://www.ebi.ac.uk/ols4/api/terms?obo_id=YOUR_IDENTIFIER'`
>
> Would you like to know how to handle cases where a search for an identifier returns no results?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-02-look-up-identifier.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, http://purl.obolibrary.org/obo/MONDO_0005068 -> http://purl.obolibrary.org/obo/MONDO_0005068

**Assessment:** Accurate: identifier forms, Jump to with matching ontology badge or the non-IMPORTED result, what to read on the page, API call.

*Correct:*
- CURIE / underscore / IRI forms
- Jump to, matching badge, not IMPORTED
- label, definition, synonyms, cross-references, relations
- api/terms?obo_id=

*Gaps:*
- use the record with is_defining_ontology true when several ontologies return the term

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OLS-02 (where to start): accurate against the use case. Minor addition for the API: pick the record with is_defining_ontology true.

### 36. OXO-01 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have an identifier, and I want its equivalent in another vocabulary?

**Reference:** [OXO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-01-find-equivalent-terms.md)

**Captured:** 2026-11-11T14:27:53.962Z · DocBot message id 13162 · [capture file](answers/36-OXO-01-wts.md)

**Answer:**

> To find the equivalent of an identifier in another vocabulary, you should use [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> You can perform this mapping using the [OxO](https://www.ebi.ac.uk/spot/oxo) website or its API:
>
> - **On the website:** Open [OxO](https://www.ebi.ac.uk/spot/oxo), enter your identifier into the “Which term do you want to map?” field, and select your desired target vocabularies in the “To ontologies” section.
> - **With the API:** You can use a POST request to the `https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search` endpoint.
>
> When reviewing the results, prefer rows marked as “Asserted” with the predicate `SKOS:exactMatch`. If a row is marked as an “SSSOM inference,” it is derived, and you should inspect it further before use. Note that prefixes in [OxO](https://www.ebi.ac.uk/spot/oxo) may differ from standard expectations (e.g., SNOMED CT is `SCTID` and ICD-10-CM is `ICD10CM`).
>
> Would you like to know how to handle cases where [OxO](https://www.ebi.ac.uk/spot/oxo) returns no results for your identifier?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-06-search-returns-nothing.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-01-find-equivalent-terms.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-02-find-term-and-translate.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Correct tool and entry points, with the asserted-exact-match preference and the prefix note.

*Correct:*
- OxO term field and To ontologies
- POST mappings/search
- prefer Asserted + exactMatch; inspect inferences
- SCTID and ICD10CM prefixes

*Gaps:*
- none

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-01 (where to start): accurate and appropriately brief.

### 37. OXO-02 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have many identifiers, and I want their equivalents in another vocabulary

**Reference:** [OXO-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-02-map-list-to-target.md)

**Captured:** 2026-11-11T14:29:12.430Z · DocBot message id 13164 · [capture file](answers/37-OXO-02-wts.md)

**Answer:**

> If you have a list of many identifiers and wish to find their equivalents in a target vocabulary, you should use [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> To map a list of identifiers to a target ontology:
>
> - Open [OxO](https://www.ebi.ac.uk/spot/oxo) and select **Multiple terms**.
> - Enter your identifiers (one per line) or upload a .txt, .csv, or .tsv file.
> - In the **To ontologies** field, select your target vocabulary (e.g., ICD10CM).
> - Leave the **From ontologies** field empty.
> - You will receive a downloadable table of mappings. Through the [OxO](https://www.ebi.ac.uk/spot/oxo) API, you can also retrieve the list of inputs for which no equivalent was found.
>
> If you are working with free-text values rather than identifiers, you should first use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map the text to a bridging ontology (such as MONDO) before using [OxO](https://www.ebi.ac.uk/spot/oxo) to translate those terms into your target vocabulary.
>
> Would you like to know how to handle mappings that are not found by default in [OxO](https://www.ebi.ac.uk/spot/oxo)?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-02-map-list-to-target.md

**Links in the answer:** OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Correct: Multiple terms mode, To ontologies, From empty, download, API reports unmapped inputs; sensible pointer to Zooma for free text.

*Correct:*
- Multiple terms; one per line or file
- To ontologies, From empty
- downloadable table; API lists unmapped inputs
- Zooma first if the values are free text

*Gaps:*
- Asserted only filter not mentioned

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-02 (where to start): accurate. Minor addition: the Type -> Asserted only filter.

### 38. PAIR-01 (where-to-start) — thumbs up, partial

**Question:** Where to start if I have many free-text values, and I want ontology terms?

**Reference:** [PAIR-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-01-check-zooma-suggestions.md)

**Captured:** 2026-11-11T14:29:21.491Z · DocBot message id 13166 · [capture file](answers/38-PAIR-01-wts.md)

**Answer:**

> To map a list of free-text values to ontology terms, you should start by using [Zooma](https://www.ebi.ac.uk/spot/zooma).
>
> For a large number of values, it is recommended to first remove duplicates so that each unique value is mapped only once, which is more efficient. You can then process these values using the following steps:
>
> - **Prepare your data:** If your values are in a spreadsheet, save or export the file as a CSV or TSV. If you have a simple list, you can paste the values directly into the [Zooma](https://www.ebi.ac.uk/spot/zooma) website, one per line.
> - **Configure mapping:** Open the [Zooma](https://www.ebi.ac.uk/spot/zooma) website and navigate to the mapping interface. It is recommended to select “Choose custom ontologies” under the “Which ontologies to map to?” section to ensure [Zooma](https://www.ebi.ac.uk/spot/zooma) performs better by focusing on specific, relevant ontologies rather than searching all available ones.
> - **Review results:** Once [Zooma](https://www.ebi.ac.uk/spot/zooma) provides suggestions, you should review them. You can use [OLS](https://www.ebi.ac.uk/ols4) to check the definitions, synonyms, and parent terms of suggested candidates to verify their accuracy.
> - **Handle unmapped values:** If [Zooma](https://www.ebi.ac.uk/spot/zooma) cannot find a suitable term, you can search [OLS](https://www.ebi.ac.uk/ols4) manually using technical names, synonyms, or by browsing the hierarchy of a broader term.
>
> Would you like to know more about how to use [OLS](https://www.ebi.ac.uk/ols4) to verify these suggestions?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-01-map-list-of-values.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Answers along the expected path (Zooma first, review doubtful suggestions in OLS, handle unmapped values) but omits recording decisions outside Zooma and the deprecated-status check; cites the Zooma use cases and TRIO-01 rather than PAIR-01.

*Correct:*
- Zooma for the list; deduplicate first
- CSV/TSV upload or paste; Choose custom ontologies
- review suggestions in OLS: definitions, synonyms, parents
- unmapped values: search OLS by hand

*Gaps:*
- record decisions outside Zooma (icons are not saved)
- check the deprecated status box
- accept / replace per suggestion; thumbs-down alternatives
- sources cite ZOOMA-01/02/03 and TRIO-01, not PAIR-01

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-01 (where to start): the Zooma-then-OLS path matches the expected answer. Additions: say to record decisions outside Zooma because the review icons are not saved, and to check the deprecated box when reviewing a term in OLS.

### 39. TRIO-01 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have many free-text values, and I want codes of a coding system?

**Reference:** [TRIO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md)

**Captured:** 2026-11-11T14:29:30.550Z · DocBot message id 13168 · [capture file](answers/39-TRIO-01-wts.md)

**Answer:**

> To map many free-text values to codes from a coding system, you should follow a multi-step process using [Zooma](https://www.ebi.ac.uk/spot/zooma), [OLS](https://www.ebi.ac.uk/ols4), and [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> 1. **Prepare your data:** Create a list of the unique values from your column (removing duplicates).
> 2. **Map to an ontology:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map your free-text values to terms in a “bridging” ontology (such as MONDO for diseases). This is necessary because [Zooma](https://www.ebi.ac.uk/spot/zooma) cannot suggest codes for systems like ICD-10-CM directly.
> 3. **Review and refine:** Check the suggestions provided by [Zooma](https://www.ebi.ac.uk/spot/zooma). Use [OLS](https://www.ebi.ac.uk/ols4) to verify doubtful suggestions, replace incorrect ones, and resolve terms that lack a code.
> 4. **Translate to codes:** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate the agreed-upon ontology terms into your target coding system (e.g., ICD10CM).
> 5. **Assemble:** Create a table containing the original value, the ontology term, and the final code, then join this back to your original dataset.
>
> It is recommended to run a sample of your values through the first stage to estimate the amount of manual review required.
>
> Would you like to know more about how to use the [Zooma](https://www.ebi.ac.uk/spot/zooma) API for this process?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-05-free-text-to-vocabulary-codes.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Correct overview of the five stages, including why a bridging ontology is needed and the advice to run a sample first.

*Correct:*
- unique values first
- Zooma to a bridging ontology because it cannot suggest ICD-10-CM codes directly
- OLS review
- OxO translation
- assemble and join
- sample first to estimate review effort

*Gaps:*
- Asserted only filter and the inferred/parent fallbacks (acceptable at this level)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, TRIO-01 (where to start): accurate overview.

### 40. ZOOMA-04 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have a passage of text, and I want the terms mentioned in it?

**Reference:** [ZOOMA-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-04-annotate-free-text.md)

**Captured:** 2026-11-11T14:30:59.710Z · DocBot message id 13170 · [capture file](answers/40-ZOOMA-04-wts.md)

**Answer:**

> To extract ontology terms from a passage of text, you can use either [OLS](https://www.ebi.ac.uk/ols4) or [Zooma](https://www.ebi.ac.uk/spot/zooma), depending on your specific needs:
>
> - **Use [OLS](https://www.ebi.ac.uk/ols4) (Tag Text page):** Choose this tool if you want to identify every stretch of text that matches a term label or a previously curated mapping. It does not rank results and will highlight all matches found in any ontology.
> - **Use [Zooma](https://www.ebi.ac.uk/spot/zooma) (Annotate Text tab):** Choose this tool if you want one ranked suggestion per phrase. This tool requires you to specify the ontologies you wish to map to, which determines the phrases the tool selects for annotation.
>
> Would you like to know more about how to choose specific ontologies for your annotation?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-04-annotate-free-text.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/ols/OLS-06-tag-text.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Correct choice between OLS Tag Text (every match, unranked) and Zooma Annotate Text (one ranked suggestion per phrase, ontology choice decides the phrases).

*Correct:*
- OLS Tag Text for every label match
- Zooma Annotate Text for ranked suggestions; ontologies must be chosen

*Gaps:*
- first steps on either tool not given (acceptable at this level)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, ZOOMA-04 (where to start): accurate choice between the two tools.

### 41. PAIR-03 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have a mapping I am unsure of, and I want a reason to trust it or not?

**Reference:** [PAIR-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-03-validate-a-mapping.md)

**Captured:** 2026-11-11T14:31:08.768Z · DocBot message id 13172 · [capture file](answers/41-PAIR-03-wts.md)

**Answer:**

> To determine if you can trust a mapping, you should start by examining its evidence and provenance within [OxO](https://www.ebi.ac.uk/spot/oxo). Follow these steps:
>
> - **View Mapping Details:** In your [OxO](https://www.ebi.ac.uk/spot/oxo) results table, click the eye icon at the end of the row to open the Mapping Details page.
> - **Check the Type:**
>
> - If the mapping is **Asserted**, it was published by a project. Note who published it and how it was made under the Mapping Set section.
> - If the mapping is an **SSSOM inference**, it was derived by [OxO](https://www.ebi.ac.uk/spot/oxo). Review the “Asserted Mappings” it rests on to identify the weakest link, such as mappings made by automatic label matching or those between terms with differing labels.
> - **Compare Terms:** Use [OLS](https://www.ebi.ac.uk/ols4) to compare the two terms. Check their definitions, synonyms, and hierarchical positions to decide if they truly mean the same thing.
> - **Evaluate Justification:** Look at the “Mapping justification” column. Be cautious of “LexicalMatching” (automatic label matching) or “MappingChaining,” as these often require closer scrutiny.
> - **Assess Distance:** In inferred mappings, the “Distance” indicates how many ontologies an inference passes through; shorter derivations are generally safer.
>
> Would you like to know how to filter your [OxO](https://www.ebi.ac.uk/spot/oxo) results to exclude mappings that do not meet your evidence requirements?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-04-check-mapping-provenance.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/two-tools/PAIR-03-validate-a-mapping.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: Mapping Details, asserted vs inferred with the weakest-premise idea, OLS comparison, justification and Distance as warning signs.

*Correct:*
- eye icon -> Mapping Details
- Asserted: who and how; inference: Asserted Mappings, weakest link
- compare definitions, synonyms, hierarchy in OLS
- LexicalMatching and MappingChaining deserve scrutiny; Distance

*Gaps:*
- the accept / downgrade / reject decision (acceptable at this level)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, PAIR-03 (where to start): accurate against the use case.

### 42. OXO-08 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have a mapping I believe is wrong, and I want to know who published it and where to report it?

**Reference:** [OXO-08](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md)

**Captured:** 2026-11-11T14:31:17.825Z · DocBot message id 13174 · [capture file](answers/42-OXO-08-wts.md)

**Answer:**

> To identify the source of a mapping and determine where to report an error, you should start by opening the mapping’s details page in [OxO](https://www.ebi.ac.uk/spot/oxo).
>
> 1. **Locate the mapping:** Find the mapping in your results table. If the row indicates “Multiple sets,” click the expand arrow to view the individual members.
> 2. **Open details:** Click the eye icon (“View mapping details”) for the specific mapping you believe is incorrect.
> 3. **Identify the source:** Look at the “Mapping Set” section on the details page.
>
> - **Asserted mappings:** The Mapping Set section identifies the project that published the set. You should report the error to that project.
> - **Inferred mappings:** If the mapping is an [OxO](https://www.ebi.ac.uk/spot/oxo) inference, the error lies in one of the underlying asserted mappings. Use the “Asserted Mappings” table under “Inference Details” to identify the specific premise that is incorrect, then report it to the publisher of that premise.
> 4. **Report the error:** When reporting, provide the address of the details page, the subject and object with their labels, the predicate, the mapping set identifier, and a clear explanation of why the mapping is wrong (including the two definitions).
>
> If the mapping is asserted, you can often find the reporting contact via the project’s website or, if the mapping is an ontology cross-reference, via the Issue Tracker button on the ontology’s page in [OLS](https://www.ebi.ac.uk/ols4).
>
> Would you like to know how to filter out incorrect mappings from your results while you wait for a correction?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/oxo/OXO-08-find-source-of-incorrect-mapping.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo

**Assessment:** Accurate: Multiple sets expansion, Mapping Details, Mapping Set section, premise tracing for inferences, report contents, and the OLS Issue Tracker route.

*Correct:*
- expand Multiple sets rows
- eye icon -> details
- Mapping Set identifies publisher
- Asserted Mappings under Inference Details -> faulty premise -> its publisher
- report contents incl. the two definitions
- Issue Tracker in OLS for ontology cross-references

*Gaps:*
- how to spot the faulty premise (labels, LexicalMatching, MappingChaining)

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, OXO-08 (where to start): accurate against the use case.

### 43. TRIO-02 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have old annotations, and I want current ones?

**Reference:** [TRIO-02](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-02-update-outdated-annotations.md)

**Captured:** 2026-11-11T14:32:27.689Z · DocBot message id 13176 · [capture file](answers/43-TRIO-02-wts.md)

**Answer:**

> To update outdated annotations, you should follow a three-step process, stopping at the first tool that provides a valid replacement for each term:
>
> 1. **[OLS](https://www.ebi.ac.uk/ols4):** Check if the term is obsolete and if the ontology explicitly names a replacement. Look up the term identifier with “Include obsolete terms” ticked. If the term page says “Replaced by,” you have found your successor.
> 2. **[OxO](https://www.ebi.ac.uk/spot/oxo):** If the ontology names no replacement, use [OxO](https://www.ebi.ac.uk/spot/oxo) to find a successor through mappings. Enter the identifier, tick “Obsolete terms” under “More options,” and search within your target ontologies.
> 3. **[Zooma](https://www.ebi.ac.uk/spot/zooma):** If the term remains unresolved, use [Zooma](https://www.ebi.ac.uk/spot/zooma) to find a successor based on the term’s wording. Use the original free-text value or the old term’s label (with any “obsolete” prefix removed) to map to your target ontologies.
>
> After any of these steps, always verify the proposed replacement in [OLS](https://www.ebi.ac.uk/ols4) to ensure its definition fits your data. If a term remains unresolved after all three steps, it requires a manual decision.
>
> Would you like to know how to use the API to automate these checks for multiple terms?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-02-update-outdated-annotations.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate three-step overview with the final OLS check.

*Correct:*
- OLS with Include obsolete terms, Replaced by
- OxO with Obsolete terms ticked
- Zooma from the wording
- verify in OLS; manual decision otherwise

*Gaps:*
- none

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, TRIO-02 (where to start): accurate.

### 44. TRIO-03 (where-to-start) — thumbs up, pass

**Question:** Where to start if I have two datasets annotated differently, and I want one combined dataset?

**Reference:** [TRIO-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md)

**Captured:** 2026-11-11T14:32:37.256Z · DocBot message id 13178 · [capture file](answers/44-TRIO-03-wts.md)

**Answer:**

> To combine two datasets that describe the same things differently, you should first bring both datasets to a common set of terms using a shared ontology. You can achieve this by following these steps:
>
> - **Choose a common ontology:** Use [OLS](https://www.ebi.ac.uk/ols4) to browse and select an ontology (such as Mondo) that covers the subject matter of both datasets and is well-connected to the coding systems you are using.
> - **Process the free-text dataset:** Use [Zooma](https://www.ebi.ac.uk/spot/zooma) to map the unique free-text values to terms from your chosen ontology. You should check any uncertain suggestions in [OLS](https://www.ebi.ac.uk/ols4) before accepting them.
> - **Process the coded dataset:** Use [OxO](https://www.ebi.ac.uk/spot/oxo) to translate your existing codes into terms from the same common ontology.
> - **Group the terms:** Once both datasets are mapped to the same ontology, use [OLS](https://www.ebi.ac.uk/ols4) to identify the hierarchy and broader groups for your terms. This allows you to group records at a level that separates the categories you care about.
> - **Combine:** Add the common term and the broader group to every record in both datasets. Records sharing the same term represent the same entity, while records sharing the same group belong together at a broader level.
>
> Would you like to know more about using the [Zooma](https://www.ebi.ac.uk/spot/zooma) or [OxO](https://www.ebi.ac.uk/spot/oxo) APIs for this process?

**Sources shown:**
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-03-combine-differently-annotated-datasets.md

**Links in the answer:** OLS -> https://www.ebi.ac.uk/ols4, OxO -> https://www.ebi.ac.uk/spot/oxo, Zooma -> https://www.ebi.ac.uk/spot/zooma

**Assessment:** Accurate overview of the five stages.

*Correct:*
- common ontology via OLS
- Zooma for free text, checked in OLS
- OxO for codes
- group via OLS hierarchy
- combine

*Gaps:*
- Max distance 1 when translating codes into the ontology

*Errors:*
- none

**Proposed feedback (thumbs up, not submitted):** 11 November run, TRIO-03 (where to start): accurate overview. Worth adding even here: set Max distance to 1 when translating codes into the ontology.
