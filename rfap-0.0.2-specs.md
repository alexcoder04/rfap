
# 0.0.2

 - client-server model
   - client makes request to the server with a certain command
   - server responds
   - example: "read file X" - "content of X"
 - header and body length sent plain, everything else is encrypted
   - with own private key (authentication)
   - with recipient's public key (noone else can read)

## packet standard

| Field         | Length (bytes) | Value          | Description   |
|---------------|----------------|----------------|---------------|
| header_length | 16             | integer        | header length |
| header        | variable       | encrypted data | header        |
| data_length   | 16             | binary integer | body length   |
| data          | variable       | encrypted data | body          |

### header

| Field           | Length (bytes) | Value          | Description                     |
|-----------------|----------------|----------------|---------------------------------|
| version         | 2              | binary integer | rfap version                    |
| command         | 4              | binary integer | type of packet                  |
| session_id      | 32             | binary code    | current session id              |
| message_id      | 16             | bytes          | message id (for reference)      |
| header          | variable       | string         | key-value pairs of data         |
| header_checksum | 32             | bytes          | checksum of all previous fields |

### body

| Field           | Length (bytes) | Value          | Description                     |
|-----------------|----------------|----------------|---------------------------------|
| body            | variable       | binary data    | files, ...                      |
| body_checksum   | 32             | bytes          | body checksum                   |

