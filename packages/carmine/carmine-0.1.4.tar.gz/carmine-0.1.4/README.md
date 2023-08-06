# Carmine toolchain

An opinionated Python toolchain made by crushing bugs.

## Usage

Add `carmine` as a developer dependency, and all the included tools will be
available for documentation, linting and testing.

Run `carmine` to see a list of top-level dependencies and version numbers.

For documentation on individual tools, see links below.

### Document toolchain

- [mkdocs](https://www.mkdocs.org)

    - [mdformat_mkdocs](https://pypi.org/project/mdformat_mkdocs/)
    - [mkdocs-awesome-pages-plugin](https://pypi.org/project/mkdocs-awesome-pages-plugin/)
    - [mkdocs-mermaid2-plugin](https://pypi.org/project/mkdocs-mermaid2-plugin/)

### Linter toolchain

- [black](https://black.readthedocs.io/en/stable/)

- [mdformat](https://mdformat.readthedocs.io/en/stable/)

- [reuse](https://reuse.software)

### Testing toolchain

- [coverage](https://coverage.readthedocs.io/en/stable/)

- [pytest](https://docs.pytest.org/en/stable/)

### Under consideration

- [duty](https://pawamoy.github.io/duty/)

- [griffe](https://mkdocstrings.github.io/griffe/)

- [mkdocs-coverage](https://pawamoy.github.io/mkdocs-coverage/)

- [mkdocstrings](https://mkdocstrings.github.io)

### Recommended extras

**Command line interface**

- [Click](https://palletsprojects.com/p/click/)

- [mkdocs-click](https://pypi.org/project/mkdocs-click/)

**Slides**

- [slide-template](https://github.com/fhiegel/slide-template) (MkDocs)

<!-- start @generated footer -->

# Sharing and contributions

```
Carmine toolchain
https://lofidevops.neocities.org
Copyright 2023 David Seaward and contributors
SPDX-License-Identifier: Apache-2.0
```

Shared under Apache-2.0. We adhere to the Contributor Covenant 2.1, and certify
origin per DCO 1.1 with a signed-off-by line. Contributions under the same
terms are welcome.

Submit security and conduct issues as private tickets. Sign commits with
`git commit --signoff`. For a software bill of materials run `reuse spdx`. For
more details see CONDUCT, COPYING and CONTRIBUTING.
