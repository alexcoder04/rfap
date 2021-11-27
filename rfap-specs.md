
# 0.0.2

## General notes

 - client-server model
   - client makes request to the server with a certain command
   - server responds
   - example: "read file X" -> "content of X"
   - persistent connection, checking from time to time if client is alive
 - multithreaded/multiprocessed
   - every connection runs on a separate thread/process
   - max number of threads -> max number of connected clients
 - header and body length sent plain, everything else is encrypted
   - with own private key (authentication)
   - with recipient's public key (privacy)
 - default port: `6700`

## Commands

For full overview, see [commands.md](./commands.md)

### Basic

 - read file/directory
 - get file/directory information
 - ping (connection is alive)
 - disconnect

### Optional (for now)

 - write file
 - touch/create file
 - delete file/directory
 - copy file/directory
 - move file/directory

## Packet standard

### Overview

| Field         | Length (bytes) | Value          | Description   |
|---------------|----------------|----------------|---------------|
| version       | 2              | integer        | rfap version  |
| header_length | 4              | integer        | header length |
| header        | variable       | encrypted data | header        |
| data_length   | 4              | integer        | body length   |
| data          | variable       | encrypted data | body          |

#### Notes

 - For now, header and body are sent plain. The encryption will be included later.
 - Checksums are going to be implemented only in future releases, as well
 - all integers are sent big-endian

### Header

| Field           | Length (bytes) | Value   | Description               |
|-----------------|----------------|---------|---------------------------|
| command         | 4              | integer | type of packet            |
| metadata        | variable       | string  | YAML data (UTF-8 encoded) |
| header_checksum | 32             | bytes   | header checksum           |

### Body

| Field         | Length (bytes) | Value       | Description   |
|---------------|----------------|-------------|---------------|
| body          | variable       | binary data | files, ...    |
| body_checksum | 32             | bytes       | body checksum |

## Versioning

This protocol does not use semantic versioning. The version is always one whole
number corresponding to the release tag on GitHub and the number sent in the
first two bytes of a packet.

