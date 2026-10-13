# OXO-03: Get all the mappings between two ontologies

**Question:** Which terms in one ontology correspond to terms in another — for example, all mappings from the Human Disease Ontology (DOID) to the Experimental Factor Ontology (EFO) — and can I have them as a file?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** the prefixes of the source and target ontologies (for example `DOID` and `EFO`).

**You get:** every mapping whose subject is in the source and whose object is in the target, on screen and as an SSSOM file.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/oxo>.
2. Leave the term box empty.
3. In **From ontologies**, choose the source (for example `DOID`). Each entry in the list shows how many mappings it takes part in.
4. In **To ontologies**, choose the target (for example `EFO`). Once a single source is chosen, this list offers only the ontologies that can be reached from it, with the number of mappings into each.
5. Click **Search**. The count above the table names the direction, for example **Mappings found: 327 · from DOID → EFO**.
6. Narrow the result if you need to, using the filter icons in the column headers — for instance **Type → Asserted only** (see [OXO-05](OXO-05-filter-by-evidence.md)).
7. Click the download icon next to the count to save the mappings as `oxo2-mappings.tsv`, an SSSOM file with one line per mapping.
8. To see the mappings in the opposite direction, click the **⇄** button between the two lists and search again.

### With the API

As a page of JSON:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings?from=DOID&to=EFO&page=0&size=100'
```

As a complete SSSOM file:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings?from=DOID&to=EFO&format=sssom-tsv' -o doid-efo.sssom.tsv
```

To find out which targets a source can be mapped to, and how many mappings there are into each:

```bash
curl -s 'https://www.ebi.ac.uk/spot/oxo/api/v2/ontologies?forSubject=DOID'
```

## Example

From `DOID` to `EFO` the table lists 327 rows, and the downloaded file has 335 mapping lines. The first lines of the file look like this:

```
# curie_map:
#   DOID: http://purl.obolibrary.org/obo/DOID_
#   EFO: http://www.ebi.ac.uk/efo/EFO_
#   …
subject_id	subject_label	predicate_id	predicate_modifier	object_id	object_label	mapping_justification	mapping_set_id
DOID:10350	breast cyst	SKOS:exactMatch		EFO:1000848	breast cyst	SEMAPV:MappingChaining	https://www.ebi.ac.uk/oxo2/inferences
```

Open the example: <https://www.ebi.ac.uk/spot/oxo/search/_map?from=DOID&to=EFO>

## Good to know

- The table counts rows, and it folds mappings that say the same thing (same subject, predicate and object) from different sources into one row; click the arrow at the start of such a row to unfold it. The downloaded file is not folded, which is why it can have more lines than the table has rows.
- Direction matters. *From DOID to EFO* and *from EFO to DOID* are separate searches and need not return the same number of rows.
- Results include inferred mappings. A row whose **Mapping set** is `https://www.ebi.ac.uk/oxo2/inferences` was derived by OxO; its derivation is one click away (see [OXO-04](OXO-04-check-mapping-provenance.md)).
- Cross-references and subclass links between the two ontologies are not included unless you tick them under **More options → Also show** (see [OXO-06](OXO-06-search-returns-nothing.md)).
- Between large ontologies the result can run to many thousands of mappings (from `MONDO` to `MESH`, more than 15,000). The file download is the practical way to work with results of that size.

## See also

- [OXO-02: Map a list of identifiers to one target ontology](OXO-02-map-list-to-target.md)
- [OXO-07: See which mapping sets OxO holds and browse one](OXO-07-browse-mapping-sets.md)

*Checked against the live service on 5 October 2026 (data release of 4 October 2026). Counts change with each data release.*
