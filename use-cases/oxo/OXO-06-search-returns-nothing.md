# OXO-06: Find mappings when a search comes back empty

**Question:** I searched OxO for a term that I know exists, and got nothing (or less than I expected). Are there really no mappings — or are they hidden?

**Tools:** [OxO](https://www.ebi.ac.uk/spot/oxo)

**You need:** the term you searched for.

**You get:** the looser links and the mappings involving obsolete terms that OxO leaves out by default.

## Background

By default OxO answers with mappings that make a definite claim about how two terms relate, such as exact, close, broad or narrow match. It leaves out three things:

- **cross-references** (`oboInOwl:hasDbXref`) — links between two identifiers that do not say what the relationship is;
- **subclass links** (`rdfs:subClassOf`) — one term is a kind of the other, not its equivalent;
- anything involving an **obsolete term**.

For many terms, cross-references are all there is, so a default search finds nothing.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/oxo> and enter your term as usual.
2. Click **▸ More options** under the **Search** button.
3. Under **Also show**, tick what you want to include:
   - **Cross-reference (oboInOwl:hasDbXref)**;
   - **Subclass (rdfs:subClassOf)**;
   - **Obsolete terms**.
4. Click **Search**.
5. Read the **Predicate** column carefully. A row with `OBOINOWL:hasDbXref` tells you only that the source linked the two identifiers. It may be an equivalence, but it may equally be a broader term, a related entry in a database, or a pathway the term takes part in.
6. When you close **More options**, the options you changed are summarised next to it — for example **(also showing cross-references)** — so that you do not forget they are on.

If the search is still empty, check these as well:

7. **Direction.** Your term is matched as the subject of a mapping. If you chose **From ontologies** or **To ontologies**, try clearing them, or swapping them with **⇄**.
8. **Label matching.** If you typed a label, it must match a term's whole label. Under **More options → Label matching**, choose **Partial match**, or search by identifier instead.
9. **The identifier itself.** Check that the prefix is one OxO knows: start typing it into **From ontologies** and see whether it is offered.

### With the API

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["GO:0004340"], "includeWeakPredicates": ["hasDbXref", "subClassOf"], "page": 0, "size": 100, "groupBySpo": true}'
```

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/oxo/api/v2/mappings/search' \
  -H 'Content-Type: application/json' \
  -d '{"queries": ["EFO:0000612"], "includeObsolete": true, "objectPrefixes": ["MONDO"], "page": 0, "size": 100, "groupBySpo": true}'
```

## Example

**A term with cross-references only.** The Gene Ontology term *glucokinase activity* (`GO:0004340`) returns no mappings by default. With **Cross-reference** ticked it returns six, all `OBOINOWL:hasDbXref`: two Rhea reactions (`RHEA:36495`, `RHEA:17825`), three Reactome entries and one MetaCyc reaction. These are related database records rather than equivalent terms — which is why they are not shown as mappings by default.
Open the example: <https://www.ebi.ac.uk/spot/oxo/search/GO:0004340?wp=hasDbXref>

**An obsolete term.** `EFO:0000612` (*obsolete_myocardial infarction*) returns nothing by default. With **Obsolete terms** ticked and **To ontologies** set to `MONDO`, it returns three inferred exact matches, the closest (distance 1) being *myocardial infarction*, `MONDO:0005068`.
Open the example: <https://www.ebi.ac.uk/spot/oxo/search/EFO:0000612?obs=1&to=MONDO>

## Good to know

- The suggestion list under the term box follows the same settings. A term whose mappings are all hidden is not suggested, so its absence from the suggestions does not mean OxO does not know the term.
- The **Obsolete terms** setting also governs mappings *to* obsolete terms: a current term's mapping to a deprecated term stays hidden until you tick the box.
- Looking for the successor of an obsolete term? Ask the ontology first — OLS shows the replacement the ontology itself records (see [OLS-05](../ols/OLS-05-check-obsolete-term.md)).

## See also

- [OXO-01: Find equivalent terms in other ontologies](OXO-01-find-equivalent-terms.md)
- [TRIO-02: Bring outdated annotations up to date](../three-tools/TRIO-02-update-outdated-annotations.md)

*Checked against the live service on 5 October 2026 (data release of 4 October 2026). Counts change with each data release.*
