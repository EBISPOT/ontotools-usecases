# OLS-03: See where a term sits in the hierarchy

**Question:** What are the broader and narrower terms of *myocardial infarction* — its parents, its children and everything beneath it?

**Tools:** [OLS](https://www.ebi.ac.uk/ols4)

**You need:** the term you are interested in (find it with [OLS-01](OLS-01-find-term-for-concept.md) or [OLS-02](OLS-02-look-up-identifier.md)).

**You get:** the path from the top of the ontology down to the term, and the list of terms below it.

## Steps

### On the website

1. Open the term's page in OLS, for example [myocardial infarction (`MONDO:0005068`)](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068).
2. Scroll to the **Tree** panel. It shows the path from the root of the ontology down to your term. With **Show counts** ticked, the number in brackets after each term is the number of terms beneath it.
3. Read upwards from your term to see its **ancestors** (broader terms). If the term has more than one parent, the tree shows each path.
4. Click the expand icon in front of your term to list its **children** (the terms directly beneath it). Expand a child to go further down.
5. Tick **Show all siblings** to also list the terms that share a parent with the terms on the path.
6. Click any term in the tree to move to that term's page.
7. Switch from **Tree** to **Graph** to see the term's neighbourhood as a diagram, including relationships other than "is a". Use the **Relationship Types** list to show or hide each kind of relationship; click a node to move to that term.
8. Scroll to **Class Relations** to read the term's parents and other relationships as statements (**Subclass of**), and the statements that other terms make about this one (**Related from**).

### With the API

Use the term's IRI, URL-encoded twice, in the path.

```bash
# Direct children
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068/children?size=100'
```

```bash
# Everything beneath the term
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068/hierarchicalDescendants?size=100'
```

```bash
# Everything above the term
curl -s 'https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0005068/hierarchicalAncestors?size=100'
```

The terms are in `_embedded.terms`; `page.totalElements` is the total and `page.totalPages` tells you whether to request further pages (`&page=1`, …).

`parents`, `children`, `ancestors` and `descendants` follow "is a" (subclass) links only. The `hierarchical…` variants also follow relationships the ontology treats as hierarchical, such as "part of".

## Example

For myocardial infarction (`MONDO:0005068`) the **Tree** panel shows this path:

```
disease
└─ human disease
   └─ disease by body system or component
      └─ cardiovascular disorder
         └─ heart disorder
            └─ myocardial disorder
               └─ myocardial infarction
```

The term has one parent (*myocardial disorder*, `MONDO:0024643`), 14 direct children — among them *acute myocardial infarction* (`MONDO:0004781`) and *silent myocardial infarction* (`MONDO:0003678`) — and 20 descendants in total.

## Good to know

- The tree starts from the ontology's preferred top-level terms. Choose **All classes** instead of **Preferred roots** to start from the true roots of the ontology.
- Tick **Show obsolete terms** to include deprecated terms in the tree.
- To browse a whole ontology from the top, open the ontology's own page (see [OLS-04](OLS-04-find-and-inspect-ontology.md)).

## See also

- [OLS-08: Search only within one branch of an ontology](OLS-08-search-within-branch.md)
- [PAIR-04: Build a code list for a disease area](../two-tools/PAIR-04-code-list-for-branch.md)

*Checked against the live service on 5 October 2026. Counts change as ontologies are updated.*
