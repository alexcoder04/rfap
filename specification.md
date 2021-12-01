
# General

 - client-server model
   - client makes request to the server with a certain command
   - server responds
   - example: "read file X" -> "content of X"
   - persistent connection, checking from time to time if client is alive
 - multithreaded/multiprocessed
   - every connection runs on a separate thread/process
   - max number of threads -> max number of connected clients
 - version as well as header and body length sent plain, everything else is encrypted
   - with own private key (authentication)
   - with recipient's public key (privacy)
 - default port: `6700`

# Commands

For full overview, see [commands.md](./commands.md)

## Basic

 - read file/directory
 - get file/directory information
 - ping (connection is alive)
 - disconnect

## Optional (for now)

 - write file
 - touch/create file
 - delete file/directory
 - copy file/directory
 - move file/directory

# Packet standard

## Overview

| Section       | Field           | Length   | Value   | Description     |
|---------------|-----------------|----------|---------|-----------------|
| version       | -               | 2        | integer | rfap version    |
| header_length | -               | 4        | integer | header length   |
| header        | command         | 4        | integer | type of packet  |
| header        | metadata        | variable | string  | YML metadata    |
| header        | header_checksum | 32       | bytes   | header checksum |
| body_length   | -               | 4        | integer | body length     |
| body          | body            | variable | bytes   | packet body     |
| body          | body_checksum   | 32       | bytes   | body checksum   |

### Notes

 - length is given in bytes
 - all integers are sent big-endian
 - all strings are encoded in UTF-8
 - for YML metadata specification, see [metadata-example.yaml](./metadata-example.yaml)
 - in future, header and body sections will be encrypted (for now plain)
 - checksums are to be implemeted in a future release, as well
 - maximal length of the header/body section is each 16MB

# Versioning

This protocol does not use semantic versioning. The version is always one whole
number corresponding to the release tag on GitHub and the number sent in the
first two bytes of a packet.

