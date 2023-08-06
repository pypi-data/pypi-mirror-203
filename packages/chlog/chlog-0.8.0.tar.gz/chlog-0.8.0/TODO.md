# TODOs

## Bug fixes

## Features

- In new change notes, expand "#1234" to an issue URL, e.g.
  `[1234](https://github.com/myaccount/myproject/issues/1234)`.
  Add a new config option issues-url, in this case

  ```toml
  [tool.chlog]
  issues-url = "https://github.com/myaccount/myproject/issues/"
  ```

## Changes

- Finish the README.

## Vague ideas

- Support for rST changelogs.
- `chlog json` command prints the JSON equivalent of the CHANGELOG.md file.
- Add an option to insert 2 newlines between ## H2 version headings.
  (But not above ## Unreleased.))
