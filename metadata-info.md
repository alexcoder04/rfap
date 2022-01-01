
# Additional information about the metadata fields

 - regular command = file/directory command, not ping/disconnect/...

| Field          | Value         | Sent if                | Required?                      |
|----------------|---------------|------------------------|--------------------------------|
| ErrorCode      | int           | always                 | yes if !=0, otherwise optional |
| ErrorMessage   | string        | ErrorCode != 0         | optional                       |
| RequestDetails | array[string] | info/directory_read    | yes                            |
| Path           | string        | all regular commands   | yes                            |
| Type           | string        | all regular commands   | yes                            |
| Modified       | int           | info                   | yes                            |
| Destination    | string        | copy/move commands     | yes                            |
| FileSize       | int           | info on file           | yes                            |
| FileType       | string        | info on file           | yes                            |
| DirectorySize  | int           | info on dir, requested | yes                            |
| ElementsNumber | int           | info on dir, requested | yes                            |

