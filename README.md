# colored_text

Lightweight utilities for applying ANSI colors and styles to Python text output.

## Installation

```bash
pip install colored_text
```

## Usage

```python
from colored_text import Style, available_styles, colorize, print_colored

print(colorize("Hello world", Style.BOLD, Style.BLUE))
print_colored("Warning", "red", "underline")

# See all available styles
print(Style.RED.value, available_styles())
```

Styles can be provided as `Style` enum members or case-insensitive strings. All outputs automatically reset styling at the end of the text.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## Publishing to PyPI

1. Build the package:

   ```bash
   python -m build
   ```

2. Validate the distributions:

   ```bash
   twine check dist/*
   ```

3. Upload to PyPI:

   ```bash
   twine upload dist/*
   ```

Create a draft release in GitHub after validating builds, then publish the artifacts generated in `dist/`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
