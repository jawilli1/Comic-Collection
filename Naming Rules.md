# Comic Collection Photo Naming Rules

Photo names consist of fields separated by a delimiter.  The delimiter is the caret character ('^'), which is unlikely to appear in a comic name.

Fields appear in a specific order:

1. Name
2. Number
3. Publisher
4. Volume
5. Month
6. Year
7. Series

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad v1 #35, EC, July 1958 | `Mad^EC^1^35^July^1958^Mad.jpg` |
| Detective Comics, DC, v1 #1, Sep 1940 | `Detective Comics^DC^1^1^Sep^1940^Detective Comics.jpg` |  

Fields can be empty.  That is indicated by consecutive delimiters, or by a field with only whitespace in it.  A field with only whitespace is treated the same as a non-existent field.  The output CSV file must have nothing in the corresponding field.

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad 110, Sep 1966 | `Mad^^^110^Sep^1966^Mad.jpg` |
| Mad 110, Sep 1966 | `Mad^ ^ ^110^Sep^1966^Mad.jpg` |
| Mad 110, Sep 1966 | `Mad^     ^     ^110^Sep^1966^Mad.jpg` |
| Detective Comics Annual #4 1953 | `Detective Comics^^^4^^1953^Detective Comics.jpg` |  

Only the `Name` field is required.  All other fields are optional, but the order is fixed.  Thus, empty fields that appear at the end of the name may be omitted.

**Example**

| Comic info | Photo name |
| --- | --- |
| Mad 250 (date unknown)  | `Mad^^^250.jpg` |
| Simpsons Shenanigans - Bongo | `Simpsons Shenanigans^Bongo.jpg` |
