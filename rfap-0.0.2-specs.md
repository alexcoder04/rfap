
## RFAP packet standard, version 0.0.2

| Field         | Length (bytes) | Value          | Description   |
|---------------|----------------|----------------|---------------|
| header_length | 16             | integer        | header length |
| header        | variable       | encrypted data | header        |
| data_length   | 16             | binary integer | body length   |
| data          | variable       | encrypted data | body          |

