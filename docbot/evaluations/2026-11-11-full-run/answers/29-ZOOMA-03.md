# 29 ZOOMA-03 (full)

- Captured: 2026-11-11T14:24:15.794Z
- DocBot message id: 13148
- Complete: True
- Reference: https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md

## Question

My values are in a column of a spreadsheet, perhaps with a second column saying what kind of thing each value is. How do I get ontology terms for that column without retyping it?

## Answer

To map values from a spreadsheet column to ontology terms using [Zooma](https://www.ebi.ac.uk/spot/zooma), follow these steps:

1. **Prepare your file:** Save or export your spreadsheet as a CSV, TSV, or plain text file.
2. **Upload:** Open [Zooma](https://www.ebi.ac.uk/spot/zooma) and click **Upload CSV** to select your file.
3. **Configure layout:** In the CSV Import Preview window, verify the delimiter and quote character settings. Ensure **First row is header** is ticked if your file includes column names.
4. **Map columns:**

- Set the **Term column** to the column containing the values you wish to map.
- Set the **Type column** to the column that describes the kind of thing each value is (e.g., “disease” or “organism part”). If you do not have a type column, set this to **None**.
5. **Import and Map:** Click the **Import** button. Once the values appear in the Map Strings box, click the **Map** button to process them.
6. **Download:** Review the results and click the download icon next to the Results heading to save the output as a `zooma_results.tsv` file.
7. **Join:** You can join the downloaded file back to your original spreadsheet by matching the `textToMap` and `propertyType` columns to the original values and types.

For large datasets, it is recommended to remove duplicates from your column before uploading to save time, as you can join the results back to the full column later.

## Links in answer

- Zooma -> https://www.ebi.ac.uk/spot/zooma
- Zooma -> https://www.ebi.ac.uk/spot/zooma

## Sources shown

- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/zooma/ZOOMA-03-annotate-spreadsheet-column.md
- https://github.com/EBISPOT/ontotools-usecases/blob/dev/use-cases/three-tools/TRIO-01-harmonise-free-text-to-codes.md
