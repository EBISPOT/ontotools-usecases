# DocBot pilot evaluation — 28 October 2026

Five independent questions were submitted to the Ontology Tools DocBot. Four answers received thumbs up and one received thumbs down. All five ratings included comments, and the interface confirmed each with “Thank you for your feedback!”.

Reference: local checkout of EBISPOT/ontotools-usecases, branch `dev`, commit `773bf7c131b2426ee78fae9bb38073f408530dcd`. Relevant reference files had no tracked modifications. Remote freshness was not verified. Target: https://wwwdev.ebi.ac.uk/docbot/?selected=ontology_tools

Each question uses the use-case's own wording. These results measure a small baseline sample, not robustness to paraphrasing or overall accuracy. Tool workflows and API examples were compared with the repository; the underlying ontology services were not independently exercised.

| Use case | Subject | Rating | Finding |
|---|---|---|---|
| OLS-05 | Obsolete terms and replacements | 👍 | Correct workflow; suggested explicitly checking the replacement definition. |
| OXO-04 | Mapping provenance and inferred evidence | 👍 | Correctly distinguishes asserted/inferred mappings and explains how to inspect premises. |
| ZOOMA-05 | Review suggestions and preserve decisions | 👍 | Correctly explains provenance, alternatives, and the limitations of UI decisions and downloads. |
| PAIR-03 | Validate an exact mapping before merging | 👍 | Compares evidence and meaning; distinguishes accept, downgrade and reject. |
| TRIO-01 | Harmonise free text to ontology terms and codes | 👎 | Omits review of multiple high-confidence suggestions and evidence checks before accepting inferred codes. |

The TRIO-01 answer also omits explicitly recording broader parent-derived codes, leaving unresolved cases for manual coding, and joining the working table back to the original data. The thumbs down rests primarily on the two reliability omissions, since the question explicitly asks which results can be relied on.

Fresh browser tabs shared conversation history. After the first question, “New conversation” was used before each remaining question, and the greeting state was verified. No follow-up prompts were used. Ratings were submitted only after the complete answer had been captured. Submission screenshots record UI acknowledgement, not a separate audit of backend storage.

## Question, answer and feedback records

### 1. OLS-05 — thumbs up

**Question:** Is the term I am using still current? If it has been made obsolete, which term should I use instead?

**Reference:** [OLS-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/ols/OLS-05-check-obsolete-term.md)

**Answer** (rendered text transcribed from the saved accessibility snapshot; original structure is in the raw capture):

To determine if an ontology term is current or obsolete, you can use the Ontology Lookup Service (OLS).

Using the OLS Website

Open 

[OLS4](https://ebi.ac.uk/ols4)

.

Tick the  Include obsolete terms  checkbox under the search box.

Enter your term’s identifier and press Enter.

Select the result from the relevant ontology.

Check the top of the term’s page:

If there is no red box, the term is current.

If a red box states “This class is deprecated,” the term is obsolete. Look for the  Replaced by  field under “Class Information” to find the suggested replacement.

Using the OLS API

You can check the status of a term programmatically using the following command:

curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/[ontology_id]/terms?obo_id=[your_term_id]'

In the response, check the 

is_obsolete

 field:

If  is_obsolete  is  true , the term is deprecated.

The  term_replaced_by  field will contain the IRI of the replacement term, or  null  if no replacement is recorded.

If a term is obsolete but no replacement is provided by the ontology, you can use 

OxO

 to find mappings to current terms or 

Zooma

 to find a successor based on the term’s wording. Would you like to know more about using OxO or Zooma to find a replacement for an obsolete term?

**Feedback submitted:** Accurate against OLS-05: includes obsolete-term search, deprecated status, replacement field and missing-replacement fallback. Small improvement: explicitly tell users to check the replacement definition before switching.

**Submission:** Confirmed by Thank you for your feedback!

[Full accessibility capture](01-OLS-05-answer.ax.txt) · [Submission evidence](01-OLS-05-feedback.png)

### 2. OXO-04 — thumbs up

**Question:** Can I rely on this mapping? Who published it and on what basis — and if OxO inferred it, from which published mappings?

**Reference:** [OXO-04](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/oxo/OXO-04-check-mapping-provenance.md)

**Answer** (rendered text transcribed from the saved accessibility snapshot; original structure is in the raw capture):

Whether you can rely on a mapping depends on its origin and the evidence behind it. OxO publishes only inferences; every mapping it displays originates from either a curated mapping set (published by a project like Mondo or Biomappings) or an ontology’s own cross-references (extracted from OLS). To determine the reliability of a specific mapping:

Check the Type:  In the results table, look at the  Type  column. “Asserted” means the mapping was published by an external source. “SSSOM inference” means OxO derived it by chaining published mappings.

View Mapping Details:  Click the eye icon at the end of the row to open the Mapping Details page. This page provides:

Mapping:  The subject, predicate, and object.

Justification:  How the mapping was made (e.g., ManualMappingCuration or LexicalMatching) and the publisher’s confidence, if provided.

Mapping Set:  The collection the mapping belongs to, which identifies the publisher.

Evaluate Inferences:  For inferred mappings, the details page includes an  Inference Details  section:

Asserted Mappings:  Lists the specific published mappings the inference rests on.

Explanation:  Provides a graph showing the derivation path.

Assess Reliability:

An inferred mapping is only as reliable as the published mappings it rests on.

Judge the inference by its “weakest ingredient.” For example, an inference derived from manually curated exact matches is generally more trustworthy than one involving automatic lexical matching or terms with differing labels.

“Exact match” is a claim made by the publisher for their specific purposes; consider whether it meets your own requirements (e.g., data merging vs. literature retrieval).

If you believe a mapping is incorrect, you should contact the original publisher identified in the Mapping Set section. Would you like to know how to use the API to fetch the derivation of an inferred mapping?

**Feedback submitted:** Accurate against OXO-04 and OXO-08: distinguishes asserted/inferred mappings, identifies Mapping Details and source sets, explains asserted premises and derivation graph, and advises judging the weakest premise.

**Submission:** Confirmed by Thank you for your feedback!

[Full accessibility capture](02-OXO-04-answer.ax.txt) · [Submission evidence](02-OXO-04-feedback.png)

### 3. ZOOMA-05 — thumbs up

**Question:** Zooma suggested a term for my value. Why that term? If it is not right, what else could it have been — and how do I keep a record of what I decide?

**Reference:** [ZOOMA-05](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/zooma/ZOOMA-05-review-and-choose-alternative.md)

**Answer** (rendered text transcribed from the saved accessibility snapshot; original structure is in the raw capture):

Zooma suggests terms based on similarity of meaning (often via language models) or by reusing mappings previously curated by EMBL-EBI data resources. To understand why a specific term was suggested, click on the value in the 

Prediction Type

 column of the Results table to open the 

Mapping Provenance

 window, which displays what your text was matched against. If the suggestion is incorrect, you can find alternatives by clicking the 

thumbs down

 icon on the row. This opens the “Select Mapping” window, which lists all candidates Zooma can find, ranked by confidence. If none of these are correct, you may need to search for a term manually using OLS. To keep a record of your decisions:

Do not rely on the website icons:  The thumbs up, thumbs down, and bin icons only change the display on your screen. They are not saved, they are not sent to Zooma, and they are not reflected in the downloaded results file.

Maintain a working file:  Download your results as a TSV file and add a column to record your final decisions, including the term label, identifier, and IRI for any replacements you select. Keeping this file, along with the date and settings used, serves as your permanent record and allows you to map the same values more efficiently in the future.

Would you like to know more about how to use OLS to verify if a suggested term is appropriate for your data?

**Feedback submitted:** Accurate against ZOOMA-05: explains Prediction Type/Mapping Provenance, alternatives via thumbs down, OLS fallback, and crucially that on-screen decisions are not saved or reflected in TSV downloads. Correctly recommends a separate dated working file.

**Submission:** Confirmed by Thank you for your feedback!

[Full accessibility capture](03-ZOOMA-05-answer.ax.txt) · [Submission evidence](03-ZOOMA-05-feedback.png)

### 4. PAIR-03 — thumbs up

**Question:** OxO says two terms are an exact match. Before I merge data on the strength of that, do the two terms really mean the same thing?

**Reference:** [PAIR-03](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/two-tools/PAIR-03-validate-a-mapping.md)

**Answer** (rendered text transcribed from the saved accessibility snapshot; original structure is in the raw capture):

To verify if two terms identified as an exact match by OxO truly have the same meaning, you should evaluate the mapping evidence and compare the terms using OLS.

1. Evaluate the Mapping Evidence in OxO

Check the details:  In the OxO results table, click the eye icon to open the Mapping Details.

Review provenance:  For asserted mappings, identify who published the mapping and how it was created. For inferred mappings, examine the underlying asserted mappings and identify the weakest link (e.g., mappings derived from automatic label matching or those between terms with differing labels).

Consider the distance:  Shorter derivations are generally safer. You can use the Max distance filter to focus on shorter paths.

Warning signs:  Differing labels are a primary indicator to investigate further.

2. Compare Terms in OLS

Click the OLS link for both the subject and object terms to compare them side-by-side:

Definition:  Determine if the definitions describe the same substance or if one is a cause, consequence, part, or special case of the other.

Tree:  Follow the hierarchy upwards to ensure both terms represent the same kind of thing (e.g., a disease and a phenotype are not interchangeable).

Synonyms:  Check if each term lists the other’s label or a similar term.

Children:  Expand the trees; if one term has children that the other lacks, it may be broader.

Class Information:  Check if the ontology cross-references the other term (database_cross_reference).

3. Decide on an Outcome

Based on your comparison, choose one of the following:

Accept:  The terms have the same definition in substance and are the same kind of thing; treat them as equivalent.

Downgrade:  The terms are closely related but not identical (e.g., broader, narrower, or different kinds of things). Keep the link as a close, broad, or narrow match, but do not merge records.

Reject:  The terms mean different things; do not use the mapping.

Note that “exact match” is a claim made by the publisher for their specific purposes; whether it is sufficient for your needs depends on your specific use case (e.g., retrieving literature vs. counting patients). If a term is not in OLS, look it up at its home resource. Would you like to know how to report a mapping you believe is incorrect?

**Feedback submitted:** Accurate against PAIR-03: checks OxO premises/provenance and OLS definitions/hierarchy, distinguishes accept/downgrade/reject, and explicitly says not to merge on downgraded mappings. Correctly treats exact match as a context-dependent publisher claim.

**Submission:** Confirmed by Thank you for your feedback!

[Full accessibility capture](04-PAIR-03-answer.ax.txt) · [Submission evidence](04-PAIR-03-feedback.png)

### 5. TRIO-01 — thumbs down

**Question:** A column of my dataset holds diagnoses as people typed them. How do I turn that column into standard ontology terms and into codes of a coding system such as ICD-10-CM — and know which results I can rely on?

**Reference:** [TRIO-01](https://github.com/EBISPOT/ontotools-usecases/blob/773bf7c131b2426ee78fae9bb38073f408530dcd/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md)

**Answer** (rendered text transcribed from the saved accessibility snapshot; original structure is in the raw capture):

To map free-text diagnoses to standard ontology terms and ICD-10-CM codes, follow this three-stage process:

Propose Terms (Zooma):

Create a list of unique values from your column.

Use 

[Zooma](https://ebi.ac.uk/spot/zooma)

 to map these values to a bridging ontology (e.g., MONDO).

Evaluation:  Accept suggestions with a confidence of 90% or more. For suggestions below 90%, or those that are yellow/grey, mark them for review.

Review Terms (OLS):

For values in the review group, use 

[OLS](https://ebi.ac.uk/ols4)

 to check definitions, synonyms, and parent terms.

Accept or reject the suggestions based on this manual check. For rejected or unmapped values, search OLS manually to find the correct term.

Translate to Codes (OxO):

Use 

[OxO](https://ebi.ac.uk/spot/oxo)

 to translate your agreed-upon terms into ICD-10-CM codes.

Select “Multiple terms,” input your identifiers, and set the target to “ICD10CM.”

Evaluation:  Use the “Asserted only” filter initially. If a term lacks an asserted code, search without this filter to check for inferred mappings. If no mapping exists, check the term’s parent in OLS for a broader code.

Reliability and Best Practices:

Confidence Scores:  Every wrong term in the provided example had a confidence between 75% and 85%, as did some correct ones; therefore, review everything below 90%.

Verification:  OxO sources do not always include labels for every code; look up codes in the coding system itself before accepting them.

Documentation:  Record the date of your run, as ontologies and mappings change over time. Keep a working table that tracks the value, the term, the code, and the method used to obtain them (e.g., “accepted from Zooma” or “chosen by hand”).

Would you like to know how to use the API to automate this pipeline?

**Feedback submitted:** TRIO-01 reliability checks are missing: accept automatically only ONE green suggestion >=90%; several green suggestions still require review. Before accepting an inferred OxO code, open Mapping Details and inspect the asserted premises/derivation for equivalent meaning (step 12; OXO-04). Also explicitly mark parent-derived codes as broader, leave unresolved values for manual coding, and join the working table back to the original column. Source: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md

**Submission:** Confirmed by Thank you for your feedback!

[Full accessibility capture](05-TRIO-01-answer.ax.txt) · [Submission evidence](05-TRIO-01-feedback.png)
