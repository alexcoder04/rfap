
# List of error codes which can be sent in the YAML header

| code | name                   | description                           |
|------|------------------------|---------------------------------------|
| 0    | ok                     | no error                              |
| 1    | file_not_exists        | -                                     |
| 2    | unknown                | unknown/other error                   |
| 3    | invalid_command        | not recognizing the rfap command      |
| 4    | invalid_file_type      | file/dir not applicable               |
| 5    | access denied          | -                                     |
| 6    | invalid content length | -                                     |
| 7    | file_exists            | -                                     |
| 8    | error_while_stat       | could not stat the requested file     |
| 9    | no_pub_key             | public key of the counterpart missing |

