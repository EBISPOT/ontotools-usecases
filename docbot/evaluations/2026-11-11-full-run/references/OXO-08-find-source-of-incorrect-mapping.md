# OXO-08: Find where an incorrect mapping came from

**Question:** A mapping in OxO looks wrong to me. Which source published it — or, if OxO inferred it, which of the published mappings it rests on is wrong — and whom do I tell?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** the mapping, in an OxO results table (see [OXO-01](OXO-01-find-equivalent-terms.md)) or on its details page.

**You get:** the mapping set — or, inside an inference, the particular published mapping — that the error traces back to; where to report it; and a way to keep it out of your own results in the meantime.

## Background

OxO publishes nothing of its own except inferences. Every mapping it shows comes from one of three kinds of origin:

| Origin | How to recognise it | Whom to tell |
|---|---|---|
| a curated mapping set — a file published by a project such as Mondo, Biomappings or SeMRA | **Type** is **Asserted**; the **Mapping set** is the project's file | the project that publishes the set |
| an ontology's own cross-references, extracted from the ontology in OLS | **Type** is **Asserted**; the set is called *OLS extracted … mappings* and its **Provider** is the ontology's page in OLS | the ontology's maintainers, through the **Issue Tracker** button on the ontology's page in OLS |
| an inference by OxO, chaining published mappings | **Type** is **SSSOM inference**; the set is `https://www.ebi.ac.uk/oxo2/inferences` | the publisher of the premise that is wrong |

An inferred mapping is a logical consequence of the published mappings it rests on. OxO derives its inferences with a reasoning engine that is sound, complete and terminating, applying the SSSOM chaining rules, so the derivation itself does not introduce errors: when an inferred mapping is wrong, one of the asserted mappings it depends on is wrong. Finding that premise is the task.

## Steps

### On the website

1. Open the mapping's details page with the eye icon (**View mapping details**) at the end of its row. If the row says **n mappings** and **Multiple sets**, it stands for several sources that assert the same statement: click the **Expand** arrow at the start of the row first, and open the member you doubt — each member has its own eye icon. A wrong statement can have more than one publisher, so look at each member in turn.
2. Note the address of the details page. It contains the mapping's identifier, and it is what you will quote in a report.
3. **If the mapping is asserted:** under **Mapping Set**, click the set's identifier to open the set's page, and read its title, description and, where present, **Provider** and creators. Then:
   - a set called *OLS extracted … mappings* means the ontology itself asserts the cross-reference; its **Provider** links to the ontology in OLS. Open the ontology's page there and use its **Issue Tracker** button. (The term's own page in OLS shows the assertion under **Class Information → database_cross_reference**.)
   - a set with a title or a provider names its project directly;
   - a set with nothing but an identifier: the identifier is normally a web address — open it in a browser. `http://purl.obolibrary.org/obo/mondo/mappings/mondo.sssom.tsv`, for example, leads to the file of that name in Mondo's GitHub repository. If the address leads nowhere, ask OxO's maintainers where the set came from (step 6).
4. **If the mapping is inferred:** the error lies in one of its premises. Under **Inference Details**, the **Asserted Mappings** table lists the published mappings the inference rests on, and **Explanation of inferred mapping** draws how they were combined (the graph names the rule applied at each step; it tells you how the premises were put together, not which one is wrong). Find the premise that does not hold:
   - look for a premise whose two labels do not mean the same thing;
   - look at the **Mapping justification** column: `LexicalMatching` means the premise was made by matching labels automatically, and `MappingChaining` means the publishing project inferred it itself; these deserve the first suspicion, as does a stated confidence below 1;
   - if none stands out, compare the two terms of each premise in OLS in turn (see [PAIR-03](../two-tools/PAIR-03-validate-a-mapping.md)). The fault is usually an exact match asserted between terms that are only similar, or between different kinds of thing — a disease and a phenotype, say.

   The faulty premise's **Mapping set** names its source; go on with step 3 for that set.
5. Check whether the error is wider than one mapping. On the set's page, filter the **Subject** or **Object** column for the term concerned, or for the justification, to see whether the set contains other mappings of the same kind. A lexical set that mis-matched one label has often mis-matched others, and a report that lists several carries more weight.
6. Report it. Give the address of the details page (step 2); the subject and object with their labels; the predicate; 
the mapping set identifier; and why the mapping is wrong, quoting the two definitions. Send the report to the publisher 
found in step 3, for a faulty asserted mapping.
7. Meanwhile, keep the mapping out of your own results with the column filters (see [OXO-05](OXO-05-filter-by-evidence.md)): 
set **Type** to **Asserted only**, or exclude the justification or the mapping set concerned. The download honours the 
filters.

### With the API

The mapping, with its derivation if it is inferred:


```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/sssom/mappings/14b4c3c3-d1c3-3644-b907-f7307ab3e595'
```

`inference_type` says whether the mapping is asserted (ASSERTED) or inferred (SSSOM_INFERENCE), and `mapping_set_id` names its set. For an inference, 
`asserted_mappings` lists the premises with their `mapping_set_id`, `mapping_justification` and `mapping_id`, and `explanation` 
gives the whole derivation with the rule applied at each step.

What OxO knows about a set:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/v2/mapping-sets/by-id?mappingSetId=https%3A%2F%2Fw3id.org%2Fbiopragmatics%2Fsemra%2Fdisease%2Fpriority.sssom.tsv.gz'
```

Every source that asserts the same statement:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["MONDO:0005015"], "objectPrefixes": ["DOID"], "page": 0, "size": 10, "groupBySpo": true}'
```

`group_members` in each result lists the members of the collapsed row, each with its `mapping_set_id`, `mapping_justification` and `mapping_id`.

## Example

**An asserted mapping.** Among the mappings of *hypertensive disorder* (`MONDO:0005044`) is `SKOS:exactMatch` to `ICD10CM:I15`, *Secondary hypertension* — one kind of hypertension, not the disorder in general, so not an exact match. The details page says **Asserted** and **Mapping Set ID: `http://purl.obolibrary.org/obo/mondo/mappings/mondo.sssom.tsv`**. The set's page shows no title or provider, but the identifier opens the file `mondo.sssom.tsv` in Mondo's GitHub repository: the source is Mondo. The term's page in OLS confirms it — under **Class Information → database_cross_reference**, Mondo lists `ICD10CM:I15` and marks it as equivalent — and the **Issue Tracker** button on Mondo's page in OLS leads to the place to report it.
Open: <https://www.ebi.ac.uk/spot/oxo/mapping/ceb33ea5-853b-33cf-a171-b2efcde5aa7f>

**An inferred mapping.** *myocardial infarction* (`MONDO:0005068`) `SKOS:exactMatch` *coronary thrombosis* (`DOID:11847`): a clot in a coronary artery is a cause of an infarction, not the same disease. The details page says **SSSOM inference** and lists three asserted mappings:

| Subject | Object | Justification | Mapping set |
|---|---|---|---|
| *myocardial infarction* `MONDO:0005068` | *acute myocardial infarction* `DOID:9408` | MappingInversion | SeMRA Disease Mappings Database - Priority Mappings |
| *coronary thrombosis* `MONDO:0006716` | *coronary thrombosis* `DOID:11847` | UnspecifiedMatching | `http://purl.obolibrary.org/obo/mondo/mappings/mondo.sssom.tsv` |
| *coronary thrombosis* `MONDO:0006716` | *acute myocardial infarction* `DOID:9408` | MappingChaining | SeMRA Disease Mappings Database - Priority Mappings |

The second premise is plainly right. The first equates an infarction with an acute infarction — close, and in any case not the problem. The third equates *coronary thrombosis* with *acute myocardial infarction*: that is the faulty premise, and its justification shows that the publishing project inferred it rather than curated it. The source is the SeMRA priority mapping set, whose title names its project. Report that premise there, quoting its own row rather than OxO's conclusion; in the meantime, **Type → Asserted only** keeps the conclusion out of your results.
Open: <https://www.ebi.ac.uk/spot/oxo/mapping/14b4c3c3-d1c3-3644-b907-f7307ab3e595>

**One statement, several publishers.** *diabetes mellitus* (`MONDO:0005015`) `SKOS:exactMatch` `DOID:9351` appears as one row marked **3 mappings** and **Multiple sets**. Expanded, it shows one mapping from Mondo's set and two from the SeMRA priority set. Had the statement been wrong, there would have been two publishers to tell — and since SeMRA compiles mappings from other projects, Mondo among them, the place to start would be the original publisher.
Open: <https://www.ebi.ac.uk/spot/oxo/search/MONDO:0005015?to=DOID>

## Good to know

- Because OxO's reasoning is logically sound and terminating, there is no need to re-check the derivation of an inferred mapping. 
An incorrect inference will only ever be because of an incorrect asserted mapping. An inferred exact match between
a disease and a phenotype, for instance, means that some source asserted an exact match across that boundary — in the case shown 
in [OXO-04](OXO-04-check-mapping-provenance.md), a lexical NCIt-to-HPO mapping — and that assertion is what to question.
- Aggregating sets, such as SeMRA's priority mappings, compile and re-derive mappings from many sources. A wrong mapping there may 
have an original publisher further upstream.
- Mapping identifiers are stable from one data release to the next, so the address of a details page remains a valid reference to the 
mapping for as long as the mapping exists.
- OxO reloads its sets with each data release (the date is shown on the home page). A correction made at the source reaches 
OxO at the next release.
- A report helps everyone: OxO serves the same sets to all its users, and so do the projects that publish them.

## See also

- [OXO-04: Check where a mapping comes from and how it was derived](OXO-04-check-mapping-provenance.md)
- [OXO-05: Keep only the mappings that meet your evidence requirements](OXO-05-filter-by-evidence.md)
- [OXO-07: See which mapping sets OxO holds and browse one](OXO-07-browse-mapping-sets.md)
- [PAIR-03: Decide whether two mapped terms really mean the same thing](../two-tools/PAIR-03-validate-a-mapping.md)

*Checked against the live service on 7 October 2026 (data release of 6 October 2026). Mappings and sets change with each data release.*
