# PAIR-02: Find a term and get its code in another vocabulary

**Question:** I know the concept in words — say *heart attack*. What is the ontology term for it, and what are the corresponding codes in other vocabularies, such as ICD-10-CM, MeSH and SNOMED CT?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4) to find the term; [OxO](https://www.ebi.ac.uk/spot/oxo) to translate it.

**You need:** a word or phrase for the concept, and the vocabularies you want codes from.

**You get:** one ontology term, and its equivalents in the other vocabularies with the evidence for each.

## Steps

### 1. OLS — find the term

1. Open <https://www.ebi.ac.uk/ols4>, type the concept into **Search OLS...** (for example `heart attack`) and press **Enter**.
2. Under **Ontology** on the left, tick an ontology that covers the subject and is well connected to other vocabularies — for diseases, **MONDO**.
3. Open the best result and confirm from its **Definition** that it is the concept you mean.
4. Copy the term's identifier with the **Copy** button next to it at the top of the page (here `MONDO:0005068`).

### 2. OxO — map the term to term in another vocabulary

5. Open <https://www.ebi.ac.uk/spot/oxo> and paste the identifier into **Which term do you want to map?**.
6. In **To ontologies**, choose the vocabularies you want codes from, for example `ICD10CM`, `MESH` and `SCTID` (SNOMED CT).
7. Click **Search**.
8. Read the rows. For each target vocabulary, prefer a row that is **Asserted** with the predicate `SKOS:exactMatch`. Rows marked **SSSOM inference** are derived; open one with the eye icon to see what it rests on before you use it (see [OXO-04](../oxo/OXO-04-check-mapping-provenance.md)).
9. Copy the codes you need from the **Object** column, or click the download icon to save the table.

### With the APIs
Find the term in OLS:
```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/search?q=heart%20attack&ontology=mondo&type=class&rows=3'
```

Take the `obo_id` of the result you want from `response.docs`, and give it to OxO:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["MONDO:0005068"], "objectPrefixes": ["ICD10CM", "MESH", "SCTID"], "page": 0, "size": 100, "groupBySpo": true}'
```

## Example

OLS: `heart attack`, restricted to Mondo, gives *myocardial infarction*, `MONDO:0005068`.

OxO: `MONDO:0005068` to `ICD10CM`, `MESH` and `SCTID` gives seven rows, three of them asserted:

| Vocabulary | Code | Predicate | Type |
|---|---|---|---|
| MeSH | `MESH:D009203` | `SKOS:exactMatch` | Asserted |
| ICD-10-CM | `ICD10CM:I21` (Acute myocardial infarction) | `SKOS:exactMatch` | Asserted |
| SNOMED CT | `SCTID:22298006` | `SKOS:exactMatch` | Asserted |

Both asserted and inferred mappings may be incorrect due to faulty asserted mappings.  Hence, mappings need to be carefully 
evaluated.

Open the example: <https://www.ebi.ac.uk/spot/oxo/search/MONDO:0005068?to=ICD10CM&to=MESH&to=SCTID>

## Good to know

- The term's page in OLS already lists cross-references under **Class Information** (**database_cross_reference**). These are mappings
that are based on `oboInOwl:hasDbXref` which are known to be poorly defined. OxO adds what they lack: the kind of match, where each 
mapping came from, mappings published by other sources, and inferred mappings. 
- Which ontology you start from matters. Start from one whose maintainers publish mappings to many vocabularies; for diseases, 
Mondo is a good choice.
- Prefixes in OxO are not always what you would guess: SNOMED CT is `SCTID`, and ICD-10-CM is `ICD10CM`. The **To ontologies** 
list shows the prefixes that are available.
- Several coding systems that OxO can map *to* are not in OLS (ICD-10-CM is one), so you cannot look their codes up there. 
Check the meaning of such a code at its home resource.
- If you have many concepts rather than one, see [PAIR-05](PAIR-05-free-text-to-vocabulary-codes.md).

## See also

- [OLS-01: Find the ontology term for a concept](../ols/OLS-01-find-term-for-concept.md)
- [OXO-01: Find equivalent terms in other ontologies](../oxo/OXO-01-find-equivalent-terms.md)
- [OXO-08: Find source of incorrect mapping](../oxo/OXO-08-find-source-of-incorrect-mapping.md)
- [PAIR-03: Decide whether two mapped terms really mean the same thing](PAIR-03-validate-a-mapping.md)

*Checked against the live services on 5 October 2026 (OxO data release of 4 October 2026). Counts change as the data are updated.*
