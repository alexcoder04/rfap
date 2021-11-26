
# 0.0.2

 - client-server model
   - client makes request to the server with a certain command
   - server responds
   - example: "read file X" - "content of X"
   - persietent connection, checking from time to time if client is alive
 - multithreaded/multiprocessed
   - every connection runs on a separate thread/process
   - max number of threads -> max number of connected clients
 - header and body length sent plain, everything else is encrypted
   - with own private key (authentication)
   - with recipient's public key (noone else can read)

## Commands

### Basic

 - read file/directory
 - get file/directory information

### Later

 - write file
 - touch/create file
 - delete file/directory
 - copy file/directory
 - move file/directory

## Packet standard

### Overview

| Field         | Length (bytes) | Value          | Description   |
|---------------|----------------|----------------|---------------|
| version       | 2              | binary integer | rfap version  |
| header_length | 4              | integer        | header length |
| header        | variable       | encrypted data | header        |
| data_length   | 4              | integer        | body length   |
| data          | variable       | encrypted data | body          |

### header

| Field           | Length (bytes) | Value   | Description     |
|-----------------|----------------|---------|-----------------|
| command         | 4              | integer | type of packet  |
| metadata        | variable       | string  | YML             |
| header_checksum | 32             | bytes   | header checksum |

### body

| Field         | Length (bytes) | Value       | Description   |
|---------------|----------------|-------------|---------------|
| body          | variable       | binary data | files, ...    |
| body_checksum | 32             | bytes       | body checksum |

