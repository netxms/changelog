#!/usr/bin/env python3

import argparse


def load_changelog(file_name:str) -> dict[str, list[str]]:
    records:dict[str, list[str]] = {}
    with open(file_name) as f:
        version = None
        for line in f:
            line = line.rstrip()
            if line == "":
                continue
            if line.startswith("# "): # version
                version = line[2:]
            else:
                if version is None:
                    continue
                if version not in records:
                    records[version] = []
                records[version].append(line)
    return records

def render_version(records:list[str], header_offset:int = 0):
    for line in records:
        if line.startswith("#"):
            print(f"\n{'#' * (header_offset)}{line}\n")
        else:
            print(line)

def render(all_versions:list[str], oss:dict[str, list[str]], atm:dict[str, list[str]], cortex:dict[str, list[str]], ist:dict[str, list[str]]):
    print(r"""

\pagebreak

    """)

    for version in all_versions:
        print(f"\n# Version {version}\n")
        if version in oss:
            print("\n## Improvements\n")
        for line in oss.get(version, []):
            if line.startswith("#"):
                print(f"\n{line}\n")
            else:
                print(line)

        if version in atm:
            print("\n## Improvements for ATM\n")
            render_version(atm[version], 1)

        if version in cortex:
            print("\n## Improvements for Cortex\n")
            render_version(cortex[version], 1)

        if version in ist:
            print("\n## Improvements for IST\n")
            render_version(ist[version], 1)


def main():
    # parse command line arguments; single flag for now: --oss
    parser = argparse.ArgumentParser()
    parser.add_argument("--oss", action="store_true", help="Generate changelog for OSS")
    args = parser.parse_args()

    oss_changelog = load_changelog("ChangeLog.md")
    all_versions = set(oss_changelog.keys())
    if not args.oss:
        atm_changelog = load_changelog("ChangeLog-ATM.md")
        cortex_changelog = load_changelog("ChangeLog-Cortex.md")
        ist_changelog = load_changelog("ChangeLog-IST.md")
        all_versions.update(atm_changelog.keys())
        all_versions.update(cortex_changelog.keys())
        all_versions.update(ist_changelog.keys())
    all_versions = {version for version in all_versions if not version.endswith("-CURRENT")}

    def version_sort(version:str) -> tuple[int, int, int, int]:
        result = [0, 0, 0, 0]

        elements = version.replace('-', '.').split(".")
        for i, element in enumerate(elements):
            if element.startswith("RC"):
                result[i] = -20 + int(element[2:])
            elif element.startswith("M"):
                result[i] = -50 + int(element[1:])
            else:
                result[i] = int(element)
        return tuple(result)

    all_versions = sorted(all_versions, reverse=True, key=version_sort)

    if not args.oss:
        render(all_versions, oss_changelog, atm_changelog, cortex_changelog, ist_changelog)
    else:
        render(all_versions, oss_changelog, {}, {}, {})

if __name__ == "__main__":
    main()
