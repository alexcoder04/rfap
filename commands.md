
# List of commands

[Server commands](#server-commands)

[File commands](#file-commands)

[Directory commands](#directory-commands)

## Notes

 - Every command is 4 bytes long.
 - The fourth byte indicates a request with 00 and an response with 01.

## Server commands

| command    | hex value   | description                                 |
|------------|-------------|---------------------------------------------|
| ping       | 00 00 00 00 | sign that connection is still alive         |
| disconnect | 01 00 00 00 | disconnects a client                        |
| pub_key    | 02 00 00 00 | exchange public keys                        |
| info       | a0 01 00 00 | get file or directory info                  |
| error      | ff ff ff ff | something went wrong (e.g. unknown command) |

## File commands

| command     | hex value   | description      |
|-------------|-------------|------------------|
| file_read   | f0 02 00 00 | get file content |
| file_delete | f1 01 00 00 | deletes a file   |
| file_create | f1 02 00 00 | creates a file   |
| file_copy   | f1 03 00 00 | copies a file    |
| file_move   | f1 04 00 00 | moves a file     |
| file_write  | f2 01 00 00 | edits a file     |

## Directory commands

| command          | hex value   | description           |
|------------------|-------------|-----------------------|
| directory_read   | d0 02 00 00 | get directory content |
| directory_delete | d1 01 00 00 | deletes a directory   |
| directory_create | d1 02 00 00 | creates a directory   |
| directory_copy   | d1 03 00 00 | copies a directory    |
| directory_move   | d1 04 00 00 | moves a directory     |

