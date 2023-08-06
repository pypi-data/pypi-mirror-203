# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright 2023 David Seaward and contributors

from importlib.metadata import version, PackageNotFoundError


def get_version(package_name):
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "unknown"


def invoke():
    package_list = [
        "carmine",
        "black",
        "coverage",
        "mdformat",
        "mdformat_mkdocs",
        "mkdocs",
        "mkdocs_awesome_pages_plugin",
        "mkdocs_mermaid2_plugin",
        "pytest",
        "reuse",
    ]

    for package in package_list:
        _version = get_version(package)
        print(f"{package}: {_version}")


if __name__ == "__main__":
    invoke()
