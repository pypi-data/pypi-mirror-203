# Welcome Package

Minimal TUI ready for cross-platform packaging as a pure-Python zipapp.

## Usage

1. Download `welcomepackage.pyz`
2. Run `python welcomepackage.pyz`

## Development workflow

Requires [pdm](https://pypi.org/project/pdm/) and
[pdm-packer](https://pypi.org/project/pdm-packer/).

To run from source:

```sh
pdm sync --dev
pdm run welcomepackage
```

To package for distribution:

```sh
pdm pack
# generates welcomepackage.pyz
# that's it!
```

To package as an executable with
[a portable shebang](https://realpython.com/python-shebang/#how-can-you-define-a-portable-shebang):

```sh
pdm pack --exe -i "/usr/bin/env python3"
# You can now drop this in ~/.local/bin
```

## References

- https://textual.textualize.io/guide/app/#widgets
- https://github.com/frostming/pdm-packer

Other options for zipapp packaging include [pex](https://pypi.org/project/pex/)
and [shiv](https://pypi.org/project/shiv/). For a tutorial, try
<https://realpython.com/python-zipapp/>

# Sharing and contributions

```
Welcome Package
https://lofidevops.neocities.org
Copyright 2023 David Seaward and contributors
SPDX-License-Identifier: CC0-1.0
```

You can copy and modify this project freely and without credit. It's mostly
uncopyrightable anyway.
