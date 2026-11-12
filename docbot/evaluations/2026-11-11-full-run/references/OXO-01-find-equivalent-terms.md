# OXO-01: Find equivalent terms in other ontologies

**Question:** I have a term in one ontology — for example *myocardial infarction*, `MONDO:0005068`. What is it called in other ontologies and coding systems such as MeSH, ICD-10-CM or SNOMED CT?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** the term's identifier (`MONDO:0005068`), its IRI, or its label.

**You get:** the mappings from your term to terms elsewhere, each with its type (for example exact match), where it came from and how OxO knows it.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/oxo>.
2. Leave **Single term** selected and type the term into **Which term do you want to map?**. After two characters a list of suggestions opens, showing each term's label, identifier and IRI, and the number of mappings it has.
3. Click a suggestion — this runs the search at once — or finish typing and press **Enter**.
4. Read the count above the table (**Mappings found: …**) and then the rows. Each row is one statement, *subject — predicate — object*:
   - **Subject** is your term;
   - **Predicate** says how the two terms relate, for example `SKOS:exactMatch` (same meaning), `SKOS:closeMatch`, `SKOS:broadMatch` or `SKOS:narrowMatch`;
   - **Object** is the term in the other ontology.
5. Use the remaining columns to judge each mapping:
   - **Type** is **Asserted** if somebody published the mapping, or **SSSOM inference** if OxO derived it by chaining published mappings;
   - **Mapping justification** says how the mapping was made (for example `ManualMappingCuration` or `LexicalMatching`);
   - **Mapping confidence** is the confidence its publisher gave, if any;
   - **Distance** is 1 for an asserted mapping and grows with the number of ontologies an inferred mapping passes through;
   - **Mapping set** is the collection the mapping belongs to.
6. To see only mappings into particular ontologies, choose them in **To ontologies** and click **Search** again.
7. Click the **OLS** link next to a term to read its definition in OLS, or the eye icon at the end of a row to see everything recorded about that mapping (see [OXO-04](OXO-04-check-mapping-provenance.md)).

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["MONDO:0005068"], "page": 0, "size": 100, "groupBySpo": true}'
```

The mappings are in `mappings.content`; `mappings.totalElements` is their number. Each mapping has a `subject_id`, `predicate_id`, `object_id`, `object_label`, `inference_type` (`ASSERTED` or `SSSOM_INFERENCE`), `distance`, `mapping_justification` and `mapping_set_id`. Add `"objectPrefixes": ["MESH", "ICD10CM"]` to keep only mappings into those ontologies.

## Example

`MONDO:0005068` has 42 mappings: 9 asserted and 33 inferred. Among the asserted ones:

| Predicate | Object | Label |
|---|---|---|
| `SKOS:exactMatch` | `MESH:D009203` | |
| `SKOS:exactMatch` | `ICD10CM:I21` | Acute myocardial infarction |
| `SKOS:exactMatch` | `SCTID:22298006` | |
| `SKOS:exactMatch` | `DOID:5844` | myocardial infarction |
| `SKOS:exactMatch` | `NCIT:C27996` | Myocardial Infarction |
| `SKOS:closeMatch` | `HP:0001658` | Myocardial infarction |

Open the example: <https://www.ebi.ac.uk/spot/oxo/search/MONDO:0005068>

## Good to know

- Your term is matched as the **subject** of a mapping. Mappings published in the other direction are still found, because OxO derives the reverse of every exact match — but they appear as **SSSOM inference** with distance 1, not as **Asserted**.
- A label must match completely (ignoring upper and lower case). `cataract` finds *cataract* but not *congenital cataract*. Under **More options → Label matching** you can switch to **Partial match**. Identifiers and IRIs are always matched exactly.
- A label can belong to terms in several ontologies, and all of them are searched. Use an identifier, or choose **From ontologies**, when you mean one particular term.
- Loose links — cross-references and subclass relations — and mappings that involve obsolete terms are hidden unless you ask for them (see [OXO-06](OXO-06-search-returns-nothing.md)).
- Some terms have no label in the table. OxO shows the labels that its mapping sources supply; follow the **OLS** link, or look the identifier up at its home resource, to see what it means.
- The address of a results page describes the whole search, so you can bookmark it or send it to a colleague.

## See also

- [OXO-05: Keep only the mappings that meet your evidence requirements](OXO-05-filter-by-evidence.md)
- [PAIR-02: Find a term and get its code in another vocabulary](../two-tools/PAIR-02-find-term-and-translate.md)

*Checked against the live service on 5 October 2026 (data release of 4 October 2026). Counts change with each data release.*
