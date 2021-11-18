
## RFAP packet standard, version 0.0.1

| Field           | Length (bytes) | Value          | Description                     |
|-----------------|----------------|----------------|---------------------------------|
| version         | 2              | binary integer | rfap version                    |
| command         | 4              | binary integer | type of packet                  |
| session_id      | 32             | binary code    | current session id              |
| message_id      | 16             | bytes          | message id (for reference)      |
| header          | variable       | string         | key-value pairs of data         |
| header_end      | 4              | fix code       | end of header                   |
| data_length     | 16             | binary integer | body length                     |
| header_checksum | 32             | bytes          | checksum of all previous fields |
| body            | variable       | binary data    | files, ...                      |
| body_end        | 4              | fix code       | end of body                     |
| body_checksum   | 32             | bytes          | body checksum                   |

## Commands

| code (hex) | description        |
|------------|--------------------|
| 0x000000   | other ERROR        |
| 0x010100   | login request      |
| 0x010101   | login success      |
| 0x010102   | login failed       |
| 0x010200   | logout             |
| 0x020100   | file/dir info req  |
| 0x020101   | file/dir info resp |
| 0x030000   | ls req             |
| 0x030001   | ls resp            |
| 0x030100   | mkdir              |
| 0x030200   | rmdir              |
| ...        | ...                |
| 0xFF0001   | invalid command    |

