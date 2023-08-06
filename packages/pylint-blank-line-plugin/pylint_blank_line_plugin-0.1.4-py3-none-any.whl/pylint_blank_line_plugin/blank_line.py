from pylint.lint import PyLinter

from pylint_blank_line_plugin.checker import BlankLineChecker


def register(linter: PyLinter) -> None:
    linter.register_checker(BlankLineChecker(linter))
