<div align="center">
  <img src="./assets/rfap_icon_v1.svg" width="20%" height="auto">
</div>
<h1 align="center">Reliable File Access Protocol</h1>

**This project is in alpha stage, so expect radical changes to come.**

This repository contains documentation, specifications, overviews,
organizational information and general discussions about the protocol. See
[related projects](#related-projects-in-progress) for actual implementations.

## Protocol specifications (in progress)

 - for general protocol specifications, see [specification.md](./specification.md)
 - for YML metadata specification, see [metadata-example.yml](./metadata-example.yml)
   and [metadata-info.md](./metadata-info.md)
 - for a full overview of commands, see [commands.md](./commands.md)
 - for a full overview of error codes, see [errors.md](./errors.md)

## Related projects (in progress)

 - https://github.com/alexcoder04/rfap-go-server - reference server implementation
 - https://github.com/alexcoder04/librfap - Python library
 - https://github.com/BoettcherDasOriginal/rfap-cs-lib - C# library
 - https://github.com/alexcoder04/rfap-pycli - Python CLI client based on librfap
 - https://github.com/alexcoder04/rfap-fuse - FUSE implementation in Python based on librfap

## Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for more information if you are
interested in contributing to this project.

## Why did we start this project?

FTP is too old.

NFS is unencrypted.

SMB is too complex.

WebDAV makes not much sense.

SSHFS is for nerds.

*So what is the best way to share files?*

