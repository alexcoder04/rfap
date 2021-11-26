
# List of commands

Note: every command is 4 bytes long.

| command        | hex value   | description                                           |
|----------------|-------------|-------------------------------------------------------|
| ping           | 00 00 00 00 | sign that connection is still alive                   |
| file_info      | f0 01 00 00 | get file information (size, file type, ...)           |
| file_read      | f0 02 00 00 | get file content                                      |
| directory_info | d0 01 00 00 | get directory information                             |
| directory_read | d0 02 00 00 | get directory content                                 |
| ...            | ...         | ...                                                   |

