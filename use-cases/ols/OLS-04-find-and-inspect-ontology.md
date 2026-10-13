# OLS-04: Find an ontology for a domain and inspect it

**Question:** Which ontologies cover my subject area, and is a particular ontology suitable — what is its scope, which version is loaded, how big is it and under which licence is it published?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4)

**You need:** a subject area (for example *disease*) or the name of an ontology.

**You get:** a shortlist of ontologies and, for each, its description, version, size, licence and contents.

## Steps

### On the website

1. Open <https://www.ebi.ac.uk/ols4> and click **Ontologies** in the menu at the top.
2. Shorten the list in either of two ways:
   - click one of the category labels above the table (for example **health**, **phenotype** or **anatomy and development**) to show only the ontologies in that category;
   - type into **Filter by Ontology**, **Filter by ID** or **Filter by Description** — for example `disease` in **Filter by Description**.
3. Read the **Description** column to judge each ontology's scope. Use **Rows per page** and the page numbers under the table to see more rows.
4. Click a row to open the ontology's page. (The links in the **Actions** column jump straight to a search within the ontology, or to its **Classes**, **Properties** or **Individuals**.)
5. On the ontology's page, check:
   - the title, the **Version** and the description at the top;
   - **Imports from** and **Exports to** — the ontologies it reuses terms from, and the ontologies that reuse its terms;
   - the **Homepage**, **Mailing List** and **Issue Tracker** buttons, where the ontology provides them;
   - the tabs **Classes (n)**, **Properties (n)** and **Individuals (n)**, which give the ontology's size and let you browse its contents as a **Tree** or a **List**;
   - **Ontology Information**, which lists the **Ontology IRI**, the **Version IRI**, when the ontology was **Last loaded** into OLS, and the ontology's own metadata such as its **License**.
6. To try the ontology out, type a concept into the **Search …** box on the ontology's page; the search is limited to that ontology.

### With the API

Search the ontologies by name and description:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/v2/ontologies?search=disease&size=20'
```

Each entry of `elements` has an `ontologyId`, `title` and `description`.

Fetch one ontology's details:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/efo'
```

`config.title`, `config.description`, `config.version` and `config.homepage` describe the ontology; `numberOfTerms`, `numberOfProperties` and `numberOfIndividuals` give its size; `updated` is when OLS last loaded it.

List every ontology in OLS:

```bash
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies?size=500'
```

## Example

Typing `disease` into **Filter by Description** reduces the list from 286 ontologies to about twenty, among them the Human Disease Ontology (DOID) and the Mondo Disease Ontology (MONDO).

Opening **MONDO** shows 63,460 classes, 493 properties and 18 individuals; a **Version IRI** ending in `releases/2026-09-01/mondo-international.owl`; and the **License** `http://creativecommons.org/licenses/by/4.0/`.

## Good to know

- The **Data Content** box on the OLS home page shows how many ontologies, classes, properties and individuals are loaded, and when the data was last updated.
- OLS reloads ontologies regularly from the location their maintainers publish them at, so **Last loaded** tells you how current the copy in OLS is, and **Version** tells you which release it is.
- If the ontology you need is not in OLS, you can request it through the OLS issue tracker linked from **Report an Issue** on the home page.

## See also

- [OLS-01: Find the ontology term for a concept](OLS-01-find-term-for-concept.md)
- [ZOOMA-02: Choose the ontologies Zooma maps to](../zooma/ZOOMA-02-choose-target-ontologies.md)

*Checked against the live service on 5 October 2026. Counts and versions change as ontologies are updated.*
