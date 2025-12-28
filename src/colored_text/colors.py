"""Utilities for styling text with ANSI escape codes."""

from __future__ import annotations

from enum import Enum
from typing import Iterable, TextIO

RESET = "\033[0m"


class Style(str, Enum):
    """Supported ANSI styles and colors."""

    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    ITALICS = ITALIC
    UNDERLINE = "\033[4m"

    DARK_GRAY = "\033[30m"
    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_YELLOW = "\033[33m"
    DARK_BLUE = "\033[34m"
    DARK_PURPLE = "\033[35m"
    DARK_CYAN = "\033[36m"
    DARK_WHITE = "\033[37m"

    GRAY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    LIGHT_GREY_HIGHLIGHT = "\033[40m"
    LIGHT_RED_HIGHLIGHT = "\033[41m"
    LIGHT_GREEN_HIGHLIGHT = "\033[42m"
    LIGHT_YELLOW_HIGHLIGHT = "\033[43m"
    LIGHT_BLUE_HIGHLIGHT = "\033[44m"
    LIGHT_PURPLE_HIGHLIGHT = "\033[45m"
    LIGHT_CYAN_HIGHLIGHT = "\033[46m"
    LIGHT_WHITE_HIGHLIGHT = "\033[47m"

    GREY_HIGHLIGHT = "\033[100m"
    RED_HIGHLIGHT = "\033[101m"
    GREEN_HIGHLIGHT = "\033[102m"
    YELLOW_HIGHLIGHT = "\033[103m"
    BLUE_HIGHLIGHT = "\033[104m"
    PURPLE_HIGHLIGHT = "\033[105m"
    CYAN_HIGHLIGHT = "\033[106m"
    WHITE_HIGHLIGHT = "\033[107m"


def available_styles() -> tuple[str, ...]:
    """Return the list of available style names."""

    return tuple(Style.__members__.keys())


def _normalize_style(style: Style | str) -> Style:
    if isinstance(style, Style):
        return style
    try:
        return Style[style.upper()]
    except KeyError as exc:
        raise ValueError(
            f"Unknown style '{style}'. Valid styles are: {', '.join(available_styles())}"
        ) from exc


def colorize(text: str, *styles: Style | str) -> str:
    """Return the text wrapped in the provided ANSI styles."""

    normalized = (_normalize_style(style) for style in styles)
    prefix = "".join(style.value for style in normalized)
    return f"{prefix}{text}{RESET}"


def print_colored(
    text: str, *styles: Style | str, end: str = "\n", file: TextIO | None = None
) -> None:
    """Print text with the provided styles applied."""

    print(colorize(text, *styles), end=end, file=file)


__all__ = ["Style", "available_styles", "colorize", "print_colored"]
