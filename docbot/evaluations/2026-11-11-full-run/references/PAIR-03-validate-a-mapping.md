# PAIR-03: Decide whether two mapped terms really mean the same thing

**Question:** OxO says two terms are an exact match. Before I merge data on the strength of that, do the two terms really mean the same thing?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo) for the mapping and its evidence; [OLS](https://www.ebi.ac.uk/ols4) for what each term means.

**You need:** a mapping in an OxO results table.

**You get:** a reasoned decision to accept the mapping, to treat it as a looser relationship, or to reject it.

## Steps

### 1. OxO — look at the evidence for the mapping

1. In the OxO results, find the row and read its **Predicate**, **Type**, **Mapping justification** and **Distance**.
2. Click the eye icon to open **Mapping Details** (see [OXO-04](../oxo/OXO-04-check-mapping-provenance.md)). For an asserted mapping, note who published it and how it was made. For an inferred mapping, read the **Asserted Mappings** it rests on and look for the weakest one: a mapping made by automatic label matching, or one between terms whose labels differ.

### 2. OLS — compare the two terms

3. Back in the results table, click the **OLS** link next to the subject, and then the one next to the object. Each opens the term's page in OLS in a new tab.
4. Compare the two pages:
   - **Definition** — do the two definitions describe the same thing, or does one describe a cause, a consequence, a part or a special case of the other?
   - **Tree** — are the two terms the same *kind* of thing? Follow each path upwards. A disease and a phenotype, or a substance and its role, can share a name without being interchangeable.
   - **Synonyms** — does each term list the other's label, or something close to it?
   - **Children** — expand each term in its tree. If one has children that the other lacks, one may be broader than the other.
   - **Class Information** — does either ontology itself cross-reference the other term (**database_cross_reference**)?

### 3. Decide

5. Choose one of three outcomes:
   - **accept** — same definition in substance, same kind of thing: treat the terms as equivalent;
   - **downgrade** — closely related but not the same (broader, narrower, or a different kind of thing): keep the link, but as a close, broad or narrow match, and do not merge records on it;
   - **reject** — the terms mean different things: do not use the mapping.
6. If you conclude that a published mapping is wrong, tell its publisher. The **Mapping Set** section of the details page identifies the source; [OXO-08](../oxo/OXO-08-find-source-of-incorrect-mapping.md) shows how to trace it and what to report.

### With the APIs

Fetch the mapping with its derivation, then each term:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/sssom/mappings/14b4c3c3-d1c3-3644-b907-f7307ab3e595'
```

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0005068'
```

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/doid/terms?obo_id=DOID:11847'
```

Compare `description` and `synonyms`, and follow `_links.parents` or `_links.hierarchicalAncestors` in each response to compare their places in the hierarchy.

## Example

Among the results for *myocardial infarction* (`MONDO:0005068`) are two inferred exact matches that deserve a second look.

**To `HP:0001658` (*Myocardial infarction*).** OxO's details show that the inference rests on a mapping made by automatic label matching ([OXO-04](../oxo/OXO-04-check-mapping-provenance.md)). In OLS:

| | `MONDO:0005068` | `HP:0001658` |
|---|---|---|
| Definition | Gross necrosis of the myocardium, as a result of interruption of the blood supply to the area, as in coronary thrombosis. | Necrosis of the myocardium caused by an obstruction of the blood supply to the heart and often associated with chest pain, shortness of breath, palpitations, and anxiety … |
| Path in the tree | disease → … → heart disorder → myocardial disorder | Phenotypic abnormality → Abnormality of the cardiovascular system → … → Acute coronary syndrome |

The definitions agree, but one term is a disease and the other a phenotype — a finding in a patient. *Decision: downgrade.* Use the link to find related records, but do not treat a diagnosis and an observed phenotype as the same statement.

**To `DOID:11847` (*coronary thrombosis*).** The labels already differ. OxO's details show the inference passes through a published mapping that equates *coronary thrombosis* with *acute myocardial infarction*. In OLS, Mondo defines coronary thrombosis (`MONDO:0006716`) as "Coagulation of blood in any of the coronary vessels. The presence of a blood clot (thrombus) often leads to myocardial infarction." — that is, a cause of infarction, not the infarction itself — and the Disease Ontology places `DOID:11847` under *thrombosis* and *coronary artery disease*. *Decision: reject.*

## Good to know

- "Exact match" in a mapping file is a claim made by its publisher, for the publisher's purposes. Whether it is exact enough for yours depends on what you will do with it: two terms can be interchangeable for retrieving literature and not for counting patients.
- Differing labels are the cheapest warning sign. Scan the **Subject** and **Object** labels of inferred rows before anything else.
- Short derivations are safer than long ones. In OxO, the **Max distance** filter keeps the short ones (see [OXO-05](../oxo/OXO-05-filter-by-evidence.md)).
- OxO shows a label only when its sources supply one. If a term has no label in OxO, or is from a vocabulary that is not in OLS, look it up at its home resource before you judge the mapping.

## See also

- [OXO-04: Check where a mapping comes from and how it was derived](../oxo/OXO-04-check-mapping-provenance.md)
- [OLS-03: See where a term sits in the hierarchy](../ols/OLS-03-explore-hierarchy.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026).*
