# 28 ZOOMA-02 (full)

- Captured: 2026-11-11T14:24:07.733Z
- DocBot message id: 13146
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md

## Question

My project annotates with particular ontologies. How do I make Zooma suggest terms from those ontologies only — or prefer them over others?

## Answer

To configure [Zooma](https://www.ebi.ac.uk/spot/zooma) to suggest or prefer terms from specific ontologies, you can define a custom list of ontologies in order of preference. The first ontology in your list that contains a good match will be prioritized.

### On the website

1. Open [Zooma](https://www.ebi.ac.uk/spot/zooma) and enter your values.
2. Click the heading **3 Which ontologies to map to?** to open the section.
3. Open the list at the top of the section and select **Choose custom ontologies**.
4. Build your list by adding the ontologies you want to use, ensuring they are ordered by your preference (not alphabetically).

### Using the API

You can specify your preferred ontologies using the `targetOntologies` parameter in your JSON request. For example:

```
{
  "properties": [{"textToMap": "heart attack"}],
  "targetOntologies": ["mondo", "hp"],
  "includeOtherOntologies": false
}
```

When you provide an ordered list, [Zooma](https://www.ebi.ac.uk/spot/zooma) will provide a single answer based on your priority. If you do not provide a list, [Zooma](https://www.ebi.ac.uk/spot/zooma) may return multiple suggestions from different ontologies when equally good matches exist. Note that when you build a custom list, `includeOtherOntologies` is unticked by default.

Would you like to know how to use [OLS](https://www.ebi.ac.uk/ols4) to browse ontologies before adding them to your [Zooma](https://www.ebi.ac.uk/spot/zooma) configuration?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- OLS -> https://www.ebi.ac.uk/ols4
- Zooma -> https://www.ebi.ac.uk/spot/zooma

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-02-choose-target-ontologies.md
