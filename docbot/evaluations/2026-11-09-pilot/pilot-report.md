# DocBot updated pilot — 9 November 2026

Result: **4 thumbs up, 1 thumbs down**. All five questions were asked verbatim in independent new conversations, and all ratings included comments. The interface acknowledged each submission.

Target: https://wwwdev.ebi.ac.uk/docbot/?selected=ontology_tools

Reference: local branch `dev`, commit `773bf7c131b2426ee78fae9bb38073f408530dcd`, unchanged from the October pilots; no tracked source modifications. Copies and checksums of the five reference documents are saved in this run. Remote freshness was not verified. The user reported a DocBot update; the deployment version was not independently exposed or verified.

| Use case | October pilot | October rerun | 9 November |
|---|---|---|---|
| OLS-05 | 👍 | 👍 | 👍 |
| OXO-04 | 👍 | 👍 | 👍 |
| ZOOMA-05 | 👍 | 👍 | 👍 |
| PAIR-03 | 👍 | 👍 | 👍 |
| TRIO-01 | 👎 | 👎 | 👎 |

These five tests check alignment with the repository. The underlying ontology services, API examples and link destinations were not independently exercised. A single new answer per question cannot establish overall accuracy or attribute a difference to the reported update. UI acknowledgements confirm receipt in the interface rather than an independent backend audit. No follow-up prompts were used.

## What changed since October

The first four use cases still pass. OLS-05 retains the minor omission of explicitly checking a replacement definition. OXO-04 now explicitly lists provenance fields. ZOOMA-05 retains its essential warning about unsaved decisions and downloads, though this answer gives less detail about recording replacement identifiers than the October rerun. PAIR-03 provides a shorter but sufficient comparison and decision workflow.

TRIO-01 is substantively better despite retaining a thumbs down:

- **Improved:** explicitly directs ambiguous suggestions to review, mentions inspecting inferred-mapping derivation paths, and includes assembly and rejoining to the original dataset. It also uses the documented OLS URL and no longer calls asserted mappings the most reliable.
- **Still problematic:** suggests a parent code without stating that it is broader than the original term or instructing users to label that loss of specificity. This omission was already raised in October and matters for interpreting the output.
- **Still too loose:** says inferred-code meaning can be checked in the coding system *or* through the derivation path. Looking up a target code establishes its meaning, but does not establish that the source term maps to it. The reference requires checking that the asserted mappings behind the inference link equivalent meanings.
- **Further improvements requested:** explicitly identify several high-confidence candidates as a review case, and retain unresolved values for manual coding. The new reference to ambiguity partly addresses the earlier multiple-candidate concern, so this was not treated as wholly unchanged.

The unchanged 4/5 tally therefore should not be read as no improvement. The primary grounds for the current thumbs down are the unqualified broader-code fallback and incomplete validation of inferred mappings. These are substantive reliability qualifications under the original rubric.

## Complete records

### 1. OLS-05 — thumbs up

**Question:** Is the term I am using still current? If it has been made obsolete, which term should I use instead?

**Reference:** [OLS-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-05-check-obsolete-term.md)

**Captured:** 2026-11-09T14:19:34.913Z

**Answer** (rendered text from the accessibility capture, with original structure retained in the raw file):

To determine if an ontology term is current or obsolete, you should use 

[OLS](https://ebi.ac.uk/ols4)

.

Using the 

[OLS](https://ebi.ac.uk/ols4)

 website:

Open 

[OLS](https://ebi.ac.uk/ols4)

.

Tick the  Include obsolete terms  checkbox under the search box.

Enter the term identifier and press Enter.

Open the result from the relevant ontology.

Check the top of the term’s page:

If there is no red box, the term is current.

If a red box says “This class is deprecated,” the term is obsolete.

If obsolete, look under  Class Information  for “term replaced by” to find the suggested replacement. If no replacement is listed, the ontology may provide a “Reason” that suggests an alternative.

Using the 

[OLS](https://ebi.ac.uk/ols4)

 API:

You can check the status programmatically using the following command:

curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/[ontology_id]/terms?obo_id=[term_id]'

In the response, check the 

is_obsolete

 field:

If  true , the term is obsolete.

The  term_replaced_by  field will contain the IRI of the replacement, or  null  if none is recorded.

If the term is obsolete and no replacement is provided by the ontology, you can use 

[OxO](https://ebi.ac.uk/spot/oxo)

 to find mappings to current terms or 

[Zooma](https://ebi.ac.uk/spot/zooma)

 to find a successor based on the term’s wording. Would you like to know how to use 

[OxO](https://ebi.ac.uk/spot/oxo)

 to find a successor for an obsolete term?

**Comment submitted:** 9 November pilot: accurate against OLS-05 on including obsolete terms, deprecated status, term replaced by, API fields, and missing-replacement fallbacks. Minor improvement: explicitly check the replacement definition before switching.

**Status:** Confirmed by Thank you for your feedback!

[Raw answer](01-OLS-05-answer.ax.txt) · [Submission screenshot](01-OLS-05-feedback.png)

### 2. OXO-04 — thumbs up

**Question:** Can I rely on this mapping? Who published it and on what basis — and if OxO inferred it, from which published mappings?

**Reference:** [OXO-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-04-check-mapping-provenance.md)

**Captured:** 2026-11-09T14:20:16.355Z

**Answer** (rendered text from the accessibility capture, with original structure retained in the raw file):

Whether you can rely on a mapping depends on its origin and the evidence behind it. 

[OxO](https://ebi.ac.uk/spot/oxo)

 does not publish its own mappings except for inferences; every mapping it displays originates from either a curated mapping set or an ontology’s own cross-references. To determine the reliability of a specific mapping:

Check the Type:  In the results table, “Asserted” means the mapping was published by a third party. “SSSOM inference” means 

[OxO](https://ebi.ac.uk/spot/oxo)

 derived it by chaining published mappings.

View Mapping Details:  Click the eye icon at the end of the row to open the Mapping Details page. This page provides:

Provenance:  Information on authors, creators, and reviewers if recorded by the source.

Mapping Set:  The collection the mapping belongs to, which identifies the publisher you should contact if you believe the mapping is incorrect.

Justification:  How the mapping was made (e.g., ManualMappingCuration or LexicalMatching) and the publisher’s confidence level, if provided.

For Inferred Mappings:  The details page includes an “Inference Details” section. This lists the “Asserted Mappings” the inference rests on and provides an “Explanation” graph showing the derivation. An inferred mapping is only as reliable as the published mappings it depends on; you should judge the inference by its weakest ingredient (e.g., an inference passing through an automatic label match is less reliable than one based on manually curated exact matches).

“Exact match” is a claim made by the publisher for their specific purposes; you should evaluate whether it meets your own requirements, such as whether the terms are interchangeable for your specific use case (e.g., counting patients vs. retrieving literature). Would you like to know how to filter your search results to only include mappings that meet specific evidence requirements?

**Comment submitted:** 9 November pilot: accurate against OXO-04. Covers asserted/inferred status, Mapping Details, provenance, mapping sets, justification/confidence, asserted premises and the derivation graph. Correctly advises judging the weakest premise and suitability for the intended use.

**Status:** Confirmed by Thank you for your feedback!

[Raw answer](02-OXO-04-answer.ax.txt) · [Submission screenshot](02-OXO-04-feedback.png)

### 3. ZOOMA-05 — thumbs up

**Question:** Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

**Reference:** [ZOOMA-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md)

**Captured:** 2026-11-09T14:20:56.205Z

**Answer** (rendered text from the accessibility capture, with original structure retained in the raw file):

To understand why 

[Zooma](https://ebi.ac.uk/spot/zooma)

 suggested a specific term, click on the value in the “Prediction Type” column of the mapping results table to open the Mapping Provenance window. This window displays what your text was matched against, which often explains the reasoning behind a suggestion. If the suggested term is incorrect, you can find alternatives by clicking the “thumbs down” icon on the row. This opens the “Select Mapping” window, which lists every candidate 

[Zooma](https://ebi.ac.uk/spot/zooma)

 found, ordered by confidence. You can review these candidates in 

[OLS](https://ebi.ac.uk/ols4)

 to check their definitions, synonyms, and hierarchy to determine if a better fit exists. To keep a record of your decisions:

Do not rely on the website icons:  The thumbs up, thumbs down, and bin icons only change the display on your screen; they are not saved, are not sent to 

[Zooma](https://ebi.ac.uk/spot/zooma)

, and are not reflected in the downloaded results file.

Maintain a working file:  Download your results as a TSV file and add a column to record your decisions, the date, and the settings used. This file serves as your permanent record and allows you to quickly map the same values in the future.

Would you like to know more about using the 

[Zooma](https://ebi.ac.uk/spot/zooma)

 API to retrieve mapping provenance?

**Comment submitted:** 9 November pilot: accurate against ZOOMA-05. Explains Mapping Provenance, alternatives via thumbs down, OLS checks and the essential warning that UI decisions are neither saved nor reflected in downloads. Correctly recommends a dated working file. Small improvement: explicitly record replacement label, identifier and IRI in that file.

**Status:** Confirmed by Thank you for your feedback!

[Raw answer](03-ZOOMA-05-answer.ax.txt) · [Submission screenshot](03-ZOOMA-05-feedback.png)

### 4. PAIR-03 — thumbs up

**Question:** OxO says two terms are an exact match. Before I merge data on the strength of that, do the two terms really mean the same thing?

**Reference:** [PAIR-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-03-validate-a-mapping.md)

**Captured:** 2026-11-09T14:21:38.426Z

**Answer** (rendered text from the accessibility capture, with original structure retained in the raw file):

To verify if two terms identified as an exact match by 

[OxO](https://ebi.ac.uk/spot/oxo)

 truly have the same meaning, you should use 

[OLS](https://ebi.ac.uk/ols4)

 to compare the terms directly. Follow these steps:

Examine the 

[OxO](https://ebi.ac.uk/spot/oxo)

 evidence:  In the results table, click the eye icon to open Mapping Details. For asserted mappings, check who published the mapping and how it was made. For inferred mappings, identify the weakest link in the derivation chain.

Compare the terms in 

[OLS](https://ebi.ac.uk/ols4)

:  Click the 

[OLS](https://ebi.ac.uk/ols4)

 link for both the subject and object to open their respective pages. Compare them based on:

Definition:  Do they describe the same thing, or is one a cause, consequence, part, or special case of the other?

Tree:  Follow the paths upward to ensure they are the same kind of thing (e.g., a disease and a phenotype are not interchangeable).

Synonyms:  Does each term list the other’s label or a close variant?

Children:  Check if one term has children that the other lacks, which may indicate a difference in breadth.

Class Information:  Check if the ontology itself contains a  database_cross_reference  to the other term.

After your comparison, you can decide to:

Accept:  Treat the terms as equivalent if they have the same definition and are the same kind of thing.

Downgrade:  Keep the link as a close, broad, or narrow match if they are related but not identical; do not merge records in this case.

Reject:  Do not use the mapping if the terms mean different things.

Would you like to know how to report a mapping you have concluded is incorrect?

**Comment submitted:** 9 November pilot: accurate against PAIR-03. Directs users to inspect OxO evidence and compare OLS definitions, hierarchy, synonyms, children and cross-references. Correct accept/downgrade/reject outcomes, explicitly prohibiting merging on downgraded mappings.

**Status:** Confirmed by Thank you for your feedback!

[Raw answer](04-PAIR-03-answer.ax.txt) · [Submission screenshot](04-PAIR-03-feedback.png)

### 5. TRIO-01 — thumbs down

**Question:** A column of my dataset holds diagnoses as people typed them. How do I turn that column into standard ontology terms and into codes of a coding system such as ICD-10-CM — and know which results I can rely on?

**Reference:** [TRIO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md)

**Captured:** 2026-11-09T14:22:38.531Z

**Answer** (rendered text from the accessibility capture, with original structure retained in the raw file):

To map a column of free-text diagnoses to standard ontology terms and ICD-10-CM codes, follow this multi-stage process:

Prepare your data:  Remove duplicates from your column so that each unique diagnosis is listed only once.

Propose terms with 

[Zooma](https://ebi.ac.uk/spot/zooma)

:  Enter your unique values into 

[Zooma](https://ebi.ac.uk/spot/zooma)

, selecting a common ontology like MONDO as your target.

Review and refine with 

[OLS](https://ebi.ac.uk/ols4)

:

Accept suggestions with a confidence of 90% or higher.

For suggestions with lower confidence, or those that are ambiguous, use 

[OLS](https://ebi.ac.uk/ols4)

 to check definitions, synonyms, and parent terms. Replace incorrect terms by searching 

[OLS](https://ebi.ac.uk/ols4)

 or using 

[Zooma](https://ebi.ac.uk/spot/zooma)

’s alternatives.

Translate to codes with 

[OxO](https://ebi.ac.uk/spot/oxo)

:  Use 

[OxO](https://ebi.ac.uk/spot/oxo)

 to map your agreed-upon ontology terms to ICD-10-CM codes.

Filter by “Asserted only” for direct mappings.

If no asserted code exists, check for inferred mappings or look up the parent term’s code in 

[OLS](https://ebi.ac.uk/ols4)

 and 

[OxO](https://ebi.ac.uk/spot/oxo)

.

Assemble:  Create a table containing the original value, the chosen term, the code, and a record of how each was determined. Join this back to your original dataset.

Evaluating Reliability:

Confidence Scores:  Use 

[Zooma](https://ebi.ac.uk/spot/zooma)

 confidence scores to prioritize manual review; review everything below 90%.

Manual Verification:  For codes without labels or those derived from inferred mappings, verify the meaning directly in the coding system or by inspecting the derivation path in 

[OxO](https://ebi.ac.uk/spot/oxo)

.

Documentation:  Record the date of your run, as ontologies and mappings are updated over time.

Would you like to know more about using the 

[OxO](https://ebi.ac.uk/spot/oxo)

 API for batch mapping?

**Comment submitted:** 9 November pilot: improved over October: now mentions ambiguous suggestions, inspecting inferred derivation paths, and rejoining the results. Remaining TRIO-01 reliability gaps: when using a parent term code, explicitly state and record that it is BROADER than the original term (step 12), and leave unresolved values for manual coding. Checking a code meaning alone is not sufficient to validate an inferred mapping: inspect the asserted premises in Mapping Details and accept only if they link equivalent meanings. Clarify that several green/high-confidence suggestions still require review. Source: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Status:** Confirmed by Thank you for your feedback!

[Raw answer](05-TRIO-01-answer.ax.txt) · [Submission screenshot](05-TRIO-01-feedback.png)
