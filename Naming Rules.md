# Comic Collection Photo Naming Rules

Photo names consist of fields separated by a delimiter.  The delimiter is the underscore character ('_'), which is unlikely to appear in a comic name.

Fields appear in a specific order:

1. Name
2. Publisher
3. Volume
4. Number
5. Month/season
6. Year

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad v1 #35, EC, July 1958 | `Mad_EC_1_35_July_1958.jpg` |
| Detective Comics, DC, v1 #1, Sep 1940 | `Detective Comics_DC_1_1_Sep_1940.jpg` |  

Fields can be empty.  That is indicated by consecutive delimiters, or by a field with only whitespace in it.  A field with only whitespace is treated the same as a non-existent field.  The output CSV file must have nothing in the corresponding field.

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad 110, Sep 1966 | `Mad___110_Sep_1966.jpg` |
| Mad 110, Sep 1966 | `Mad_ _ _110_Sep_1966.jpg` |
| Mad 110, Sep 1966 | `Mad_     _     _110_Sep_1966.jpg` |
| Detective Comics Annual #4 1953 | `Detective Comics___4__1953.jpg` |  

Only the `Name` field is required.  All other fields are optional, but the order is fixed.  Thus, empty fields that appear at the end of the name may be omitted.

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad 250 (date unknown)  | `Mad___250.jpg` |
| Simpsons Shenanigans - Bongo | `Simpsons Shenanigans_Bongo.jpg` |
