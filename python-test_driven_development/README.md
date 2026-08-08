# Python - Test-driven development

This project applies test-driven development in Python: writing
interactive doctests (`.txt` files under `tests/`) alongside each
function, and writing formal `unittest`-based test suites, covering
edge cases like empty inputs, wrong types, and boundary values.

## Requirements
- Editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- First line of every file: `#!/usr/bin/python3`
- Code follows pycodestyle (version 2.7.*)
- All files end with a new line and must be executable
- Every module and function has a real, descriptive docstring
- All tests run via `python3 -m doctest ./tests/*` or `python3 -m unittest tests.*`
