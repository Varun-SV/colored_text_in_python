from colored_text import Style, available_styles, colorize, print_colored


def test_colorize_applies_styles_in_order():
    result = colorize("hello", Style.BOLD, Style.RED)
    assert result == f"{Style.BOLD.value}{Style.RED.value}hello\033[0m"


def test_colorize_accepts_string_styles_case_insensitive():
    result = colorize("hi", "red", "underline")
    assert result.startswith(Style.RED.value + Style.UNDERLINE.value)
    assert result.endswith("\033[0m")


def test_invalid_style_raises_value_error():
    try:
        colorize("text", "not-a-style")
    except ValueError as exc:
        assert "Unknown style" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid style")


def test_print_colored_writes_to_stdout(capsys):
    print_colored("warn", Style.YELLOW, end="")
    captured = capsys.readouterr()
    assert captured.out == f"{Style.YELLOW.value}warn\033[0m"


def test_available_styles_exposes_enum_names():
    styles = available_styles()
    assert "BOLD" in styles
    assert "RED" in styles
