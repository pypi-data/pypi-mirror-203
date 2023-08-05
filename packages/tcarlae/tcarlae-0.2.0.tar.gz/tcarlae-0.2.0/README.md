# T. carlae

Minimal Python repository with a simple development workflow. Share and enjoy!

## Workflow

```bash
$ git clone https://gitlab.com/lfdo/tcarlae.git
$ cd tcarlae
$ pdm install --dev
$ pdm run tcarlae
Hello world!
```

Alternatively:

```bash
$ pdm run python -m tcarlae.cli
Hello world!
```

And to publish:

```bash
$ git tag -a 2.0.0 -m "Version 2.0.0"
$ pdm publish  # uses tag for version number
```

# Sharing and contributions

```
T. carlae
https://lofidevops.neocities.org
Copyright 2023 David Seaward and contributors
SPDX-License-Identifier: CC0-1.0
```

You can copy and modify this project freely and without credit. It's mostly
uncopyrightable anyway.

# Colophon

The Barbados threadsnake (known as Tetracheilostoma carlae or T. carlae) is the
smallest known snake species in the world.
