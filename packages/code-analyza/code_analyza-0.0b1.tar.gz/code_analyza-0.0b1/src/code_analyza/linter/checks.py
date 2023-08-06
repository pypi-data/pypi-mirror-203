import ast
import os
import re

from .utils import find_indices, list_file_paths

errors = []
blank_lines = 0


def add_error(path, line_no, issue):
    errors.append(f"{path}: Line {line_no}: {issue}")


def check_line_length(current_line, line_no, path):
    """Line length is not greater than 79 characters"""
    if len(current_line) > 79:
        add_error(path, line_no, "S001 Too long")


def check_indentation(current_line, line_no, path):
    """Indentation is not a multiple of four"""
    line_length = len(current_line)
    if line_length != 1 and (line_length - len(current_line.lstrip())) % 4 != 0:
        add_error(path, line_no, "S002 Indentation is not a multiple of four")


def check_semicolon(semicolon_index, line_no, path):
    pass
    """Unnecessary semicolon after a statement that isn't a comment"""
    if semicolon_index:
        add_error(path, line_no, "S003 Unnecessary semicolon")


def check_inline_comments(comment_index, current_line, line_no, path):
    """Less than two spaces before inline comments"""
    if comment_index and (len(current_line[:comment_index]) - len(current_line[:comment_index].rstrip())) < 2:
        add_error(path, line_no, "S004 At least two spaces required before inline comments")


def check_todo(comment_index, current_line, line_no, path):
    """TODO found (in comments only and case-insensitive)"""
    lowercase = current_line.lower()
    if "todo" in lowercase:
        if comment_index is not None and lowercase.rindex("todo") > comment_index:
            add_error(path, line_no, "S005 TODO found")


def check_blank_line(current_line, line_no, path):
    """More than two blank lines preceding a code line (applies to the first non-empty line)"""
    global blank_lines

    for char1 in current_line:
        if char1 == "\n":
            blank_lines += 1
        elif char1 != "\n":
            if blank_lines > 3:
                add_error(path, line_no, "S006 More than two blank lines used before this line")
            blank_lines = 0


def check_naming_spaces(current_line, line_no, path):
    """Too many spaces after a class or function name"""
    class_re1 = r"\s*class\B"
    class_re2 = r"\s*class\s{2,}"
    function_re1 = r"\s*def\B"
    function_re2 = r"\s*def\s{2,}"

    if re.match(class_re1, current_line) or re.match(class_re2, current_line):
        add_error(path, line_no, "S007 Too many spaces after 'class'")
    elif re.match(function_re1, current_line) or re.match(function_re2, current_line):
        add_error(path, line_no, "S007 Too many spaces after 'def'")


def check_naming_style(path, current_line=None, line_no=None, node=None):
    """
    Class names should be written in CamelCase.
    Function names should be written in snake_case.
    Argument names should be written in snake_case.
    Variable names should be written in snake_case.
    """
    if current_line:
        class_re = r"\s*class\s*[a-z]\w*-*\w*"
        function_re = r"\s*def\s*_*[A-Z]\w*-*\w*"
        class_match = re.match(class_re, current_line)
        function_match = re.match(function_re, current_line)

        if class_match:
            class_name = class_match.group().replace("class", "").lstrip()
            add_error(path, line_no, f"S008 Class name {class_name} should be written in CamelCase")
        elif function_match:
            function_name = function_match.group().replace("def", "").lstrip()
            add_error(path, line_no, f"S009 Function name {function_name} should be written in snake_case")
    else:
        arg_var_re = r"_*[A-Z]\w*-*\w*"

        for arg in node.args.args:
            arg_match = re.match(arg_var_re, arg.arg)
            if arg_match:
                add_error(path, arg.lineno, f"S010 Argument name '{arg_match.group()}' should be written in snake_case")
                break

        for line in node.body:
            if isinstance(line, ast.Assign) and not isinstance(line.targets[0], ast.Attribute):
                var_match = re.match(arg_var_re, line.targets[0].id)
                if var_match:
                    add_error(path, line.lineno,
                              f"S011 Variable '{var_match.group()}' should be written in snake_case")
                    break


def check_default_arg_value(node, path):
    """The default argument value is mutable."""
    for arg in node.args.defaults:
        if not isinstance(arg, ast.Constant):
            add_error(path, node.lineno, "S012 The default argument value is mutable.")
            break


def analyse_file(path):
    """Analyse a file for PEP violations"""
    _file = open(path)
    issues = []

    for number, line in enumerate(_file, start=1):
        check_line_length(line, number, path)
        check_indentation(line, number, path)
        semicolon, comment = find_indices(line)

        if not line.startswith("#"):
            check_semicolon(semicolon, number, path)
            check_inline_comments(comment, line, number, path)

        check_todo(comment, line, number, path)
        check_blank_line(line, number, path)
        check_naming_spaces(line, number, path)
        check_naming_style(path, line, number)

    _file.seek(0)
    tree = ast.parse(_file.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            check_naming_style(path, node=node)
            check_default_arg_value(node, path)

    _file.close()
    issues += errors
    errors.clear()
    return issues


def analyse_directory(base_path):
    """Analyse a directory for PEP violations"""
    issues = []
    file_paths = list_file_paths(os.listdir(base_path), base_path)

    for file_path in file_paths:
        issues += analyse_file(file_path)

    errors.clear()
    return issues


def analyse(base_path):
    if os.path.isfile(base_path) and base_path.endswith(".py"):
        return analyse_file(base_path)
    elif os.path.isdir(base_path):
        return analyse_directory(base_path)
