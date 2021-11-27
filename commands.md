
# List of commands

Note: every command is 4 bytes long.

| command          | hex value   | description                                           |
|------------------|-------------|-------------------------------------------------------|
| ping             | 00 00 00 00 | sign that connection is still alive                   |
| file_info        | f0 01 00 00 | get file information (size, type, ...)                |
| file_read        | f0 02 00 00 | get file content                                      |
| file_delete      | f1 01 00 00 | deletes a file                                        |
| file_create      | f1 02 00 00 | creates a file                                        |
| file_copy        | f1 03 00 00 | copies a file                                         |
| directory_info   | d0 01 00 00 | get directory information (size, ...)                 |
| directory_read   | d0 02 00 00 | get directory content                                 |
| directory_delete | d1 01 00 00 | deletes a directory                                   |
| directory_create | d1 02 00 00 | creates a directory                                   |
| directory_copy   | d1 03 00 00 | copies a directory                                    |

