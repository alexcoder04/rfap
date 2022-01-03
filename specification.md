
# General

 - client-server model
   - client makes request to the server with a certain command
   - server responds
   - example: "read file X" -> "content of X"
   - persistent connection, checking from time to time if client is alive
 - the communication runs over TCP sockets
 - version as well as header and body length sent plain, everything else is encrypted and signed
 - default port: `6700`

# Commands

For an overview of commands, please see [commands.md](./commands.md)

# Packet standard

| Section       | Field           | Length            | Value   | Description     |
|---------------|-----------------|-------------------|---------|-----------------|
| version       | -               | 2                 | integer | rfap version    |
| header_length | -               | 4                 | integer | header length   |
| header        | command         | 4                 | integer | type of packet  |
| header        | metadata        | variable, max 8KB | string  | YML metadata    |
| header        | header_checksum | 32                | bytes   | header checksum |
| body_length   | -               | 4                 | integer | body length     |
| body          | body            | variable, max 4GB | bytes   | packet body     |
| body          | body_checksum   | 32                | bytes   | body checksum   |

## Notes

 - length is given in bytes
 - all integers are sent big-endian
 - all strings are encoded in UTF-8
 - for YML metadata specification, see [metadata-example.yml](./metadata-example.yml)
 - the whole header section and the whole body section are encrypted
   - PGP encryption is used for that
   - the data is first encrypted using recipient's public key
   - then it's signed with own private key
 - the checksum is a SHA256 hash
   - of `command+metadata` for the header section
   - of the body for the body section
 - maximal length of the header section is 8KB
 - for now, body length is limited to 4GB

# Versioning

The version always consists of two numbers: the major and the minor version.
These correspond to the release tag and the two bytes sent in every packet.

