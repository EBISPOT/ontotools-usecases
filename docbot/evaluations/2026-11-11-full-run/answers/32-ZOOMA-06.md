# 32 ZOOMA-06 (full)

- Captured: 2026-11-11T14:26:02.123Z
- DocBot message id: 13154
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-06-reuse-curated-mappings.md

## Question

Has a curator at one of the EMBL-EBI data resources already mapped this text to an ontology term? And how do I control which resources' curated mappings Zooma draws on?

## Answer

Yes, [Zooma](https://www.ebi.ac.uk/spot/zooma) draws on mappings previously made by curators at EMBL-EBI data resources. When your input text matches a previously curated mapping, [Zooma](https://www.ebi.ac.uk/spot/zooma) suggests the same term with high confidence and identifies the source resource in the “Source” column of the results.

You can control which resources are used as follows:

- **On the website:**

- Open the “Where to get mappings?” section.
- Click the × on a label to exclude a resource.
- Click an excluded resource to include it again.
- Drag the labels to reorder them; the resource in the first position has the highest priority.
- **With the API:**

- Use the `filter` parameter in your POST request to the `https://www.ebi.ac.uk/spot/zooma/v3/api/services/map` endpoint.
- Specify resources to use in `filter.required` and resources to prefer in `filter.preferred`.
- If you leave the `filter` parameter out, [Zooma](https://www.ebi.ac.uk/spot/zooma) will use all available resources.

Note that [Zooma](https://www.ebi.ac.uk/spot/zooma) will not suggest a curated mapping if the target ontology has been excluded.

Would you like to know how to view the provenance of a specific curated suggestion?

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-06-reuse-curated-mappings.md
