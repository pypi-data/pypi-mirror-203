# Code Analyza

A code analyser package for Python.

## Getting Started

### Installation

Code Analyza is available via PyPi.

```bash
pip install code-analyza
```

### Usage

Run as a script:

```bash
code_analyza path/to/file/or/directory
```

Import as a module:

```python
from code_analyza.linter.checks import analyse

base_path = # set path/to/file/or/directory
issues = analyse(base_path)
```

## Style Conventions

Code Analyza currently implements 9 conventions as specified by the [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). They include: 

- Code Lay-out
  - Indentation
  - Maximum Line Length
  - Blank Lines
- Comments
  - Inline Comments
- Naming Conventions
  - Class, Function and Variable Names
  - Function and Method Parameters
- Semicolons 
- Todos
- Default Arguments

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## Support

Give a ⭐️ if you like this project!

## Acknowledgements

- [PEP 8](https://peps.python.org/pep-0008/)
- [Ruff](https://github.com/charliermarsh/ruff)

## 📝 Copyright & License

Copyright (c) 2023 Clifton Davies. This project is licensed under [MIT](https://opensource.org/licenses/MIT). See LICENSE file for details.