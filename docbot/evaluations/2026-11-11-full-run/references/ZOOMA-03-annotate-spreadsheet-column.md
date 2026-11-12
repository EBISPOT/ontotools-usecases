# ZOOMA-03: Annotate a column of a spreadsheet

**Question:** My values are in a column of a spreadsheet, perhaps with a second column saying what kind of thing each value is. How do I get ontology terms for that column without retyping it?

**Tools:** [Zooma](https://www.ebi.ac.uk/spot/zooma)

**You need:** the spreadsheet saved as a text file: comma-separated (`.csv`), tab-separated (`.tsv`) or plain text (`.txt`).

**You get:** a file of suggested terms that you can join back to your spreadsheet.

## Steps

### On the website

1. In your spreadsheet program, save or export the sheet as CSV or TSV.
2. Open <https://www.ebi.ac.uk/spot/zooma> and click **Upload CSV**, at the right above the input box. Choose your file.
3. The **CSV Import Preview** window opens with the first rows of your file. Zooma guesses how the file is laid out; check 
its guesses and correct them where needed:
   - **Delimiter** — the character that separates the columns: comma, tab, semicolon or pipe;
   - **Quote character** — the character that surrounds values containing the delimiter: double quote, single quote, or **None**;
   - **First row is header** — tick this if the first row holds column names rather than data.
4. In **Term column**, choose the column that holds the values to map. The column is marked **→ Term** in the preview.
5. In **Type column**, choose the column that says what kind of thing each value is (for example a column holding `disease` 
or `organism part`), marked **→ Type** in the preview. If your file has no such column, choose **None**.
6. Check the number of rows found, then click **Import … terms** button. The values are added to the **Map Strings** box, one per line, each followed by its type if you chose a type column.
7. Look over the box, edit it if you wish, and click **Map … strings**.
8. Review the results (see [ZOOMA-01](ZOOMA-01-map-list-of-values.md) and [ZOOMA-05](ZOOMA-05-review-and-choose-alternative.md)), then click the download icon next to the **Results** heading to save `zooma_results.tsv`.
9. Join the downloaded file to your spreadsheet. Its `textToMap` column holds your original value and `propertyType` holds the type; match on these to bring `ontologyTermLabel`, `ontologyTermID` and `mappingConfidence` into your sheet. Where a value has several suggestions there are several rows, so decide first which one to keep.

### With the API

The API takes values as JSON, not as a file. Convert each row of your file into an entry of `properties` — the value as `textToMap` and, if you have one, its kind as `propertyType` — and send them as in [ZOOMA-01](ZOOMA-01-map-list-of-values.md):

```bash
curl -s -X POST 'https://www.ebi.ac.uk/spot/zooma/v3/api/services/map' \
  -H 'Content-Type: application/json' \
  -d '{
        "properties": [
          {"textToMap": "lung adenocarcinoma", "propertyType": "disease"},
          {"textToMap": "doxycycline", "propertyType": "compound"}
        ]
      }'
```

## Example

A file `samples.csv`:

```
sample_id,value,kind
S1,lung adenocarcinoma,disease
S2,doxycycline,compound
S3,cerebellum,organism part
```

In the preview, make sure **First row is header** is ticked, set **Term column** to `value` and **Type column** to `kind`, 
and click the **Import 3 terms** button. The **Map Strings** box then holds three lines, such as `lung adenocarcinoma` *Tab* 
`disease`, and the button reads **Map 3 strings**.

## Good to know

- When a file has more than one column, Zooma pre-selects the first column as **Term column** and the second as **Type column**. 
In the example above that would be `sample_id` and `value` — so always check both, and set **Type column** to **None** if you have no type column.
- Imported values are added to whatever is already in the **Map Strings** box. Click **Clear** first if you want to start from an empty box.
- Repeated values are sent as they are. To save time on a long column, remove duplicates before you upload and join the results back by value.
- The file is read in your browser; only the values you import are sent to Zooma when you click **Map**.
- Kinds that appear in existing curated mappings include `disease`, `organism`, `organism part`, `cell type`, `cell line`, 
`compound`, `strain` and `developmental stage`. You are not limited to these.

## See also

- [ZOOMA-01: Map a list of free-text values to ontology terms](ZOOMA-01-map-list-of-values.md)
- [TRIO-01: Harmonise free-text values into ontology terms and codes](../three-tools/TRIO-01-harmonise-free-text-to-codes.md)

*Checked against the live service on 5 October 2026.*
