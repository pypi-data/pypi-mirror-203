# Poetry Git Version Plugin

Poetry plugin to get package version from git.

## Functionality

- Git tag parsing
- Make alpha version
- Substitution of the project tag (if any) in the poetry.version value
- Maintenance of PEP 440
- Command to output a new version

## Quick start

```bash
poetry self add poetry-git-version-plugin
poetry git-version # Write your git tag
poetry -v git-version # print process
```

## Dependencies

```toml
[tool.poetry.dependencies]
python = ">=3.7"
poetry = ">=1.2.0"
```

## Setup

```toml
[tool.poetry-git-version-plugin]
# Ignore "tag missing" errors and other errors
# Default = true
ignore_errors = true

# If the tag is missing.
# Returns a version, computed from the latest version tag.
# It takes the version tag, increases the version tag by the number of commits since, adds a local label specifying the git commit hash and the dirty status.
# Example: 1.3.2+5-5babef6
make_alpha_version = true

# Format for alpha version
# Default = '{version}.a{distance}+{commit_hash}'
format_alpha_version = '{version}+{distance}'
```

## Contribute

Issue Tracker: <https://gitlab.com/rocshers/python/poetry-git-version-plugin/-/issues>  
Source Code: <https://gitlab.com/rocshers/python/poetry-git-version-plugin>
