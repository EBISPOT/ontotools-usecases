# PAIR-06: Find a term by hand when Zooma cannot map a value

**Question:** Zooma found nothing for one of my values, or nothing that fits. How do I find the right term myself — and what do I do if there isn't one?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma) shows which values are left over; [OLS](https://www.ebi.ac.uk/ols4) is where you look for a term by hand.

**You need:** a **Results** table in Zooma with values that are unmapped, or mapped to the wrong thing.

**You get:** a term for each leftover value, or the knowledge that no suitable term exists yet.

## Steps

### 1. Zooma — list what is left over

1. In the **Results** table, collect the values that need attention:
   - values marked **Did not map**;
   - values whose only suggestions are grey (low score);
   - values whose suggestion you checked and rejected (see [PAIR-01](PAIR-01-check-zooma-suggestions.md)).
2. For a rejected suggestion, click the **thumbs down** first and look through Zooma's longer list of candidates. If the right term is there, select it and you are done.

### 2. OLS — look for the term yourself

Work through these in order, and stop when you find a term that fits.

3. **Search with the words of the value.** In <https://www.ebi.ac.uk/ols4>, type the value into **Search OLS...** and press **Enter**. Under **Ontology** on the left, tick the ontologies you annotate with.
4. **Search with other words.** Think of how a specialist would put it — the technical name rather than the everyday one, the full name rather than the abbreviation, the singular rather than the plural — and search again.
5. **Search by meaning.** Set **Search Model** to an embedding model and search with the original wording (see [OLS-07](../ols/OLS-07-semantic-search.md)). This finds terms whose labels share no words with yours.
6. **Browse.** Find a broader term that certainly applies — the organ, the disease group, the general kind of thing — open it, and expand it in the **Tree** panel. Read through its children for the one that matches (see [OLS-03](../ols/OLS-03-explore-hierarchy.md)).
7. When you find a candidate, check its **Definition** and its parents before you use it, and copy its identifier.

### 3. When there is no term

8. If the nearest term is broader than your value, use the broader term and keep your original text alongside it, so that nothing is lost.
9. If nothing fits at all, ask for a new term. Open the ontology's page in OLS and use its **Issue Tracker** button (where the ontology provides one) to reach the place where its maintainers take requests. Describe the concept, give a definition and say where the term should sit in the hierarchy.

### With the APIs

A lexical search and a search by meaning, both restricted to one ontology:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/search?q=enlarged%20lymph%20nodes&ontology=hp&rows=5'
```

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/v2/ontologies/hp/classes/llm_search?q=enlarged%20lymph%20nodes&model=llama-embed-nemotron-8b_pca512&size=5'
```

## Example

The value `enlarged lymph nodes`, to be annotated with the Human Phenotype Ontology (HP) or Mondo.

**Zooma** offers two suggestions, both yellow and both wrong: *adenoid hypertrophy* (`MONDO:0000740`, 75.50%) and *Lymph node with expanded mantle zones* (`HP:0020253`, 75.45%).

**OLS**, searching HP for `enlarged lymph nodes`, lists terms for enlarged nodes in particular places — *Hilar lymph node enlargement*, *Submandibular lymph node enlargement*, *Enlarged mesenteric lymph node* — and, a little further down, *Cervical lymphadenopathy*. That last label supplies the technical word. Searching HP for `lymphadenopathy` then gives the general term as its first result: *Lymphadenopathy*, `HP:0002716`, defined as "Enlargement (swelling) of a lymph node", with *Swollen lymph nodes* among its synonyms and several of the place-specific terms among its children. That is the term for the value.

## Good to know

- Everyday wording is the commonest reason a value goes unmapped. One good search result often hands you the technical word, as *lymphadenopathy* did here.
- Abbreviations, codes local to your organisation and misspellings also defeat automatic mapping. Expand or correct them and run them through Zooma again before you search by hand.
- Some values should not be mapped: "not recorded", "see notes", "other". Decide how to represent these in your data rather than forcing a term onto them.
- Once you have settled on a term for a value, keep the pair. A list of your own decisions is the quickest way to map the same value next time.

## See also

- [OLS-07: Find a term by meaning when you do not know the wording](../ols/OLS-07-semantic-search.md)
- [ZOOMA-05: Understand why Zooma suggested a term, choose a better one, and keep a record](../zooma/ZOOMA-05-review-and-choose-alternative.md)

*Checked against the live services on 5 October 2026. Suggestions and search results change as ontologies are updated.*
