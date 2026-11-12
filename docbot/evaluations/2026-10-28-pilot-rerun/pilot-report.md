# DocBot pilot rerun — 28 October 2026

The same five questions were rerun, each in a fresh conversation. Result: **4 thumbs up and 1 thumbs down**, matching the first pilot. Each new rating included a comment; all five submissions were acknowledged by the interface with “Thank you for your feedback!”.

Target: https://wwwdev.ebi.ac.uk/docbot/?selected=ontology_tools

Reference: local repository branch `dev`, commit `773bf7c131b2426ee78fae9bb38073f408530dcd`, unchanged from the first pilot. There were no tracked modifications. Remote freshness was not verified. The tool services and suggested API calls were not independently exercised. This evaluates alignment with the specified use cases.

| Use case | First pilot | Rerun | Finding |
|---|---|---|---|
| OLS-05 | 👍 | 👍 | Correct workflow again. The explicit reminder to verify the replacement definition remains absent; recorded as a minor improvement. |
| OXO-04 | 👍 | 👍 | Correctly distinguishes asserted and inferred mappings, identifies mapping sets, and explains inspecting the premises and weakest ingredient. |
| ZOOMA-05 | 👍 | 👍 | Correct provenance and separate-record guidance. This answer adds explicit alternative selection with CONFIRM and OLS checks. |
| PAIR-03 | 👍 | 👍 | Correct evidence and meaning checks, with accept/downgrade/reject outcomes and a warning not to merge on downgraded mappings. |
| TRIO-01 | 👎 | 👎 | Repeats both primary omissions: multiple high-confidence candidates need review, and inferred mappings need inspection of their asserted premises. Also describes Asserted only as selecting the most reliable mappings, which overstates what assertion status alone establishes. Uses an OLS URL different from the documented ols4 URL; whether it redirects was not tested. |

The answers vary in wording, but the five verdicts are unchanged. The repeated TRIO-01 failure concerns substantive reliability omissions, rather than style. The reference's website workflow explicitly requires review when there are several green suggestions (step 4), and checking inferred mappings against their premises (step 12). Missing broader-code labelling, manual-coding fallback, and rejoining results to the original dataset were also included in the feedback.

These are two small runs using the documents' own question wording. They do not establish overall accuracy, paraphrase robustness, or whether feedback caused any model change. UI acknowledgements confirm acceptance in the interface, not a separate backend audit. “New conversation” was used before every question and the greeting was checked. No follow-up prompts were used.

## Complete question, answer and feedback records

### 1. OLS-05 — thumbs up

**Captured:** 2026-10-28T13:33:50.346Z

**Question:** Is the term I am using still current? If it has been made obsolete, which term should I use instead?

**Reference:** [OLS-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-05-check-obsolete-term.md)

**Finding:** Correct workflow again. The explicit reminder to verify the replacement definition remains absent; recorded as a minor improvement.

**Answer** (rendered text from the saved accessibility snapshot; original structure is in the raw capture):

To determine if an ontology term is current or obsolete, you can use the 

[OLS](https://ebi.ac.uk/ols4)

 tool.

Using the OLS Website

Open 

[OLS](https://ebi.ac.uk/ols4)

.

Tick the  Include obsolete terms  checkbox under the search box.

Enter your term’s identifier and press Enter.

Select the result from the relevant ontology.

Check the top of the term’s page:

If there is no red box, the term is current.

If a red box says “This class is deprecated,” the term is obsolete. You can find the replacement term (if recorded) under  Class Information  labeled as  term replaced by .

Using the OLS API

You can check the status of a term using the following command:

curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/[ontology_id]/terms?obo_id=[your_term_id]'

In the response, 

is_obsolete

 will be 

true

 if the term is deprecated, and 

term_replaced_by

 will provide the IRI of the replacement term (or 

null

 if none is recorded).

If no replacement is recorded

If the ontology does not provide a replacement, you can attempt to find one using:

[OxO](https://ebi.ac.uk/spot/oxo)

: To find a successor through mappings.

[Zooma](https://ebi.ac.uk/spot/zooma)

: To find a successor based on the term’s wording.

Would you like to know more about using OxO or Zooma to find a successor for an obsolete term?

**Comment submitted:** Rerun: accurate against OLS-05 on obsolete search, deprecated status, term replaced by, API fields and missing-replacement fallback. Minor improvement remains: explicitly check the replacement definition before switching.

**Submission status:** Confirmed by Thank you for your feedback!

[Full accessibility capture](01-OLS-05-answer.ax.txt) · [Submission evidence](01-OLS-05-feedback.png)

### 2. OXO-04 — thumbs up

**Captured:** 2026-10-28T13:34:37.969Z

**Question:** Can I rely on this mapping? Who published it and on what basis — and if OxO inferred it, from which published mappings?

**Reference:** [OXO-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-04-check-mapping-provenance.md)

**Finding:** Correctly distinguishes asserted and inferred mappings, identifies mapping sets, and explains inspecting the premises and weakest ingredient.

**Answer** (rendered text from the saved accessibility snapshot; original structure is in the raw capture):

Whether you can rely on a mapping depends on its origin and the evidence supporting it. OxO publishes no mappings of its own except for inferences; every mapping originates from either a curated set (published by a project like Mondo, Biomappings, or SeMRA) or an ontology’s own cross-references (extracted from 

[OLS](https://ebi.ac.uk/ols4/)

). To determine the reliability of a specific mapping:

Check the Type:  In the 

[OxO](https://ebi.ac.uk/spot/oxo)

 results table, the  Type  column indicates if a mapping is  Asserted  (published by a third party) or an  SSSOM inference  (derived by OxO).

View Mapping Details:  Click the eye icon at the end of any row to open the Mapping Details page. This page provides:

Mapping:  The statement (subject, predicate, object).

Mapping Set:  The collection the mapping belongs to, which identifies the publisher.

Justification:  How the mapping was made (e.g., ManualMappingCuration or LexicalMatching) and the publisher’s confidence, if provided.

Evaluate Inferences:  For inferred mappings, the details page includes an  Inference Details  section:

Asserted Mappings:  Lists the specific published mappings the inference rests on.

Explanation:  A graph showing the derivation path.

Reliability:  An inferred mapping is a logical consequence of the published mappings it rests on and is exactly as reliable as those premises. You can judge the inference by its “weakest ingredient”—for example, an inference passing through a mapping made by automatic label matching is less reliable than one based on manually curated exact matches.

“Exact match” claims are made by the publisher for their specific purposes; you should assess whether the mapping is suitable for your specific use case (e.g., retrieving literature versus counting patients). Would you like to know how to filter your search results to only show mappings that meet specific evidence requirements?

**Comment submitted:** Rerun: accurate against OXO-04. Correctly distinguishes asserted and inferred mappings, directs users to Mapping Details and source mapping sets, and explains inspecting asserted premises/derivation and judging the weakest premise.

**Submission status:** Confirmed by Thank you for your feedback!

[Full accessibility capture](02-OXO-04-answer.ax.txt) · [Submission evidence](02-OXO-04-feedback.png)

### 3. ZOOMA-05 — thumbs up

**Captured:** 2026-10-28T13:35:38.226Z

**Question:** Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

**Reference:** [ZOOMA-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md)

**Finding:** Correct provenance and separate-record guidance. This answer adds explicit alternative selection with CONFIRM and OLS checks.

**Answer** (rendered text from the saved accessibility snapshot; original structure is in the raw capture):

Zooma suggests terms based on its internal mapping logic, which includes curated mappings from EMBL-EBI data resources and similarity of meaning judged by a language model. To understand why a specific term was suggested:

Understand the suggestion:  Click on the value in the  Prediction Type  column of the results table to open the  Mapping Provenance  window. This shows what your text was matched against and the reasoning behind the suggestion.

Find alternatives:  If the suggestion is incorrect, click the  thumbs down  icon on the row. This opens the “Select Mapping” window, which lists all candidates Zooma found, including their Term Label, Confidence, Term ID, Source, and Prediction Type. You can select a better candidate from this list and click  CONFIRM .

Check terms:  Before accepting a suggestion or alternative, click the identifier in the  Term ID  column to open the term in 

[OLS](https://ebi.ac.uk/ols4)

. Check the definition, synonyms, hierarchy (Tree), and status to ensure it is appropriate for your data.

Keep a record:  Because the review controls (thumbs up/down and bin) in the Zooma interface are not saved and do not persist after a page reload or in the downloaded file, you must maintain your own record. Download the results as a TSV file and add a column to track your decisions, including the final term label, identifier, and IRI for each value.

Would you like to know more about how to use 

[OLS](https://ebi.ac.uk/ols4)

 to verify these terms?

**Comment submitted:** Rerun: accurate against ZOOMA-05. Covers Mapping Provenance, alternative selection with CONFIRM, checking meanings in OLS, and keeping a separate record because UI decisions are not saved or reflected in downloads.

**Submission status:** Confirmed by Thank you for your feedback!

[Full accessibility capture](03-ZOOMA-05-answer.ax.txt) · [Submission evidence](03-ZOOMA-05-feedback.png)

### 4. PAIR-03 — thumbs up

**Captured:** 2026-10-28T13:36:23.152Z

**Question:** OxO says two terms are an exact match. Before I merge data on the strength of that, do the two terms really mean the same thing?

**Reference:** [PAIR-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-03-validate-a-mapping.md)

**Finding:** Correct evidence and meaning checks, with accept/downgrade/reject outcomes and a warning not to merge on downgraded mappings.

**Answer** (rendered text from the saved accessibility snapshot; original structure is in the raw capture):

To verify if two terms identified as an exact match by 

[OxO](https://ebi.ac.uk/spot/oxo)

 truly have the same meaning, you should perform a comparative analysis using 

[OxO](https://ebi.ac.uk/spot/oxo)

 for mapping evidence and 

[OLS](https://ebi.ac.uk/ols4)

 for term definitions.

1. Evaluate the Mapping Evidence in OxO

Check the details:  In your 

[OxO](https://ebi.ac.uk/spot/oxo)

 results, examine the Predicate, Type, Mapping justification, and Distance.

Review provenance:  Click the eye icon to open Mapping Details. For asserted mappings, identify who published the mapping and how it was created. For inferred mappings, review the asserted mappings it relies on, looking for the weakest link (e.g., automatic label matching or mappings between terms with differing labels).

Consider the context:  Remember that an “exact match” is a claim made by a publisher for their specific purposes. Whether it is sufficient for your needs depends on your specific use case (e.g., retrieving literature vs. counting patients).

2. Compare Terms in OLS

Click the 

[OLS](https://ebi.ac.uk/ols4)

 link for both the subject and object terms to compare them side-by-side:

Definition:  Determine if the definitions describe the same substance or if one is a cause, consequence, part, or special case of the other.

Tree:  Follow the hierarchy upwards to ensure they are the same kind of thing.

Synonyms:  Check if each term lists the other’s label or a close variation.

Children:  Compare the children of each term; if one has children the other lacks, it may be broader.

Class Information:  Check if either ontology cross-references the other term.

3. Decide on an Outcome

Based on your comparison, choose one of the following:

Accept:  The terms have the same definition in substance and are the same kind of thing; treat them as equivalent.

Downgrade:  The terms are closely related but not identical (e.g., broader, narrower, or different kinds of things). Keep the link as a close, broad, or narrow match, but do not merge records.

Reject:  The terms mean different things; do not use the mapping.

If you conclude a published mapping is incorrect, you can identify the source in the Mapping Set section of the details page to report it. Would you like to know how to use the 

[OxO](https://ebi.ac.uk/spot/oxo)

 API to fetch mapping derivations programmatically?

**Comment submitted:** Rerun: accurate against PAIR-03. Covers mapping evidence and weakest premises, comparison of OLS definitions/hierarchy, and accept/downgrade/reject decisions. Explicitly prohibits merging records on downgraded mappings.

**Submission status:** Confirmed by Thank you for your feedback!

[Full accessibility capture](04-PAIR-03-answer.ax.txt) · [Submission evidence](04-PAIR-03-feedback.png)

### 5. TRIO-01 — thumbs down

**Captured:** 2026-10-28T13:37:07.844Z

**Question:** A column of my dataset holds diagnoses as people typed them. How do I turn that column into standard ontology terms and into codes of a coding system such as ICD-10-CM — and know which results I can rely on?

**Reference:** [TRIO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md)

**Finding:** Repeats both primary omissions: multiple high-confidence candidates need review, and inferred mappings need inspection of their asserted premises. Also describes Asserted only as selecting the most reliable mappings, which overstates what assertion status alone establishes. Uses an OLS URL different from the documented ols4 URL; whether it redirects was not tested.

**Answer** (rendered text from the saved accessibility snapshot; original structure is in the raw capture):

To map free-text diagnoses to standard ontology terms and ICD-10-CM codes, follow this three-stage process:

Propose Terms (Zooma):

Remove duplicates from your column so each unique diagnosis is listed only once.

Use 

[Zooma](https://ebi.ac.uk/spot/zooma)

 to map these values to a bridging ontology (e.g., MONDO).

Accept suggestions with a confidence of 90% or more.

Review and Refine (OLS):

For suggestions with a confidence below 90%, or those that are unmapped, use 

[OLS](https://ebi.ac.uk/spot/ols)

 to manually check definitions, synonyms, and parent terms.

Replace incorrect suggestions with appropriate terms found by searching 

[OLS](https://ebi.ac.uk/spot/ols)

.

Translate to Codes (OxO):

Use 

[OxO](https://ebi.ac.uk/spot/oxo)

 to translate your agreed-upon ontology terms into ICD-10-CM codes.

When using 

[OxO](https://ebi.ac.uk/spot/oxo)

, set the Type filter to “Asserted only” for the most reliable mappings.

If a term lacks an asserted code, you may check for inferred mappings or look up the parent term’s code in 

[OLS](https://ebi.ac.uk/spot/ols)

 and 

[OxO](https://ebi.ac.uk/spot/oxo)

.

Evaluating Reliability:

Confidence Scores:  Use the confidence score provided by 

[Zooma](https://ebi.ac.uk/spot/zooma)

 as a guide; review everything below 90%.

Manual Verification:  Always verify codes in the coding system itself, especially if 

[OxO](https://ebi.ac.uk/spot/oxo)

 does not provide a label for a code.

Documentation:  Record how each term and code was obtained (e.g., “accepted from Zooma,” “chosen by hand”) and note the date of the run, as mappings change over time.

Would you like to know how to use the API for this pipeline?

**Comment submitted:** Rerun: TRIO-01 still omits essential reliability checks. Automatically accept only ONE green suggestion >=90%; several high-confidence candidates need review. Inspect inferred OxO mappings in Mapping Details and check asserted premises before accepting a code. Asserted status alone does not guarantee reliability. Mark parent-derived codes as broader, leave unresolved values for manual coding, and join the working table back to the original dataset. Use the documented OLS URL https://www.ebi.ac.uk/ols4. Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Submission status:** Confirmed by Thank you for your feedback!

[Full accessibility capture](05-TRIO-01-answer.ax.txt) · [Submission evidence](05-TRIO-01-feedback.png)
