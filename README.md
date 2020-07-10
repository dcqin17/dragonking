# dragonking (A Python Package)

## Purpose

The dragonking python package implements published statistical tests and test statistics for identification of dragon kings.

## Installation

To install the dragonking python package with pip, simply run:

```
pip install dragonking
```

## Example usage of the inward procedure (outward is identical).

```
dk.inward(
  teststat = dk.mrs,
  data = [0, 0.3, 0.6, 0.31, 0.2, 0.1],
  r = 1,
  m = 1,
  alpha = 0.15
)
```

## Contributions

Please report any bugs, suggestions, or feature requests at the repository's [issues page](https://github.com/dcqin17/dragonking). We welcome any contributions in the form of pull requests from forked versions of this repo.
