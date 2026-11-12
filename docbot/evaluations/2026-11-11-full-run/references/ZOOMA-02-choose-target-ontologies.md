# ZOOMA-02: Choose the ontologies Zooma maps to

**Question:** My project annotates with particular ontologies. How do I make Zooma suggest terms from those ontologies only — or prefer them over others?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma)

**You need:** the ontologies you want to use, in order of preference (for example Mondo first, then the Human Phenotype Ontology).

**You get:** suggestions drawn from the ontologies you chose, with your preferred ontology winning when several have a matching term.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/spot/zooma> and enter your values (see [ZOOMA-01](ZOOMA-01-map-list-of-values.md)).
2. Click the heading **3 Which ontologies to map to?** to open the section.
3. Open the list at the top of the section. It shows the current choice — to begin with, the preset **EFO and OBO Foundry**. Choose one of:
   - a **preset**, a ready-made list of ontologies (the number in brackets is how many it contains);
   - **Choose custom ontologies**, to build your own list;
   - **All ontologies (not recommended)**, to search every ontology with equal priority.
4. If you chose **Choose custom ontologies**, type an ontology's name into **Search ontologies by name, e.g. EFO** and click it in the list that appears. Repeat for each ontology you want.
5. Put the chosen ontologies in order of preference. They are listed from most to least preferred; drag an ontology by the handle at its left to move it. Click the **×** at its right to remove it, or **Clear all** to start again.
6. Decide what should happen to matches in other ontologies with the tick box **Include results from other ontologies**:
   - **unticked** — suggestions come from your chosen ontologies only;
   - **ticked** — suggestions from other ontologies are allowed as well.
7. Click **Map … strings**. The **Source** column of the results shows which ontology each suggestion came from.

### With the API

Give the ontologies, in order of preference, as `targetOntologies` (lower-case ontology identifiers), and set `includeOtherOntologies`:

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [{"textToMap": "heart attack"}],
        "targetOntologies": ["mondo", "hp"],
        "includeOtherOntologies": false
      }'
```

The presets offered on the website are available from the API too:

```bash
curl -s 'https://www.ebi.ac.uk/spot/zooma/v3/api/ontology-presets'
```

## Example

The value `heart attack` matches a term in several ontologies. What Zooma suggests depends on the list:

| Chosen ontologies (in order) | Suggestion |
|---|---|
| Mondo, then HP | *myocardial infarction* `MONDO:0005068` (100%) |
| HP, then Mondo | *Myocardial infarction* `HP:0001658` (100%) |
| none (all ontologies) | four suggestions at 100%, from DOID, HP, Mondo and NCIT |

With an ordered list Zooma gives one answer. With no list it cannot choose between equally good matches, and leaves the choice to you.

## Good to know

- The first ontology in your list that has a good match wins, so order the list by which ontology you would rather annotate with — not alphabetically.
- When you pick a preset or build a custom list, **Include results from other ontologies** starts unticked.
- With **All ontologies (not recommended)** selected, Zooma shows the warning *ZOOMA performs better when given specific target ontologies*. Use it only for exploring.
- Not sure which ontologies suit your data? Browse them in OLS first (see [OLS-04](../ols/OLS-04-find-and-inspect-ontology.md)).
- Your choice is remembered in your browser and marked with a **customized** label next to the section heading.

## See also

- [ZOOMA-01: Map a list of free-text values to ontology terms](ZOOMA-01-map-list-of-values.md)
- [PAIR-05: Convert free-text values into identifiers of a specific vocabulary](../two-tools/PAIR-05-free-text-to-vocabulary-codes.md)

*Checked against the live service on 5 October 2026. Suggestions change as ontologies are updated.*
