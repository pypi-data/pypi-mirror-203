import os

from src.code_analyza.linter.checks import analyse

TOO_LONG_LINE = 'Too long line is not mentioned. '
error_code_long = "s001"

INDENTATION = "Invalid check of indentation. "
error_code_indention = "s002"

UNNECESSARY_SEMICOLON = "Your program passed the line with an unnecessary semicolon or has an incorrect format. "
error_code_semicolon = "s003"

TWO_SPACES_BEFORE_COMMENT = "The program should warn about the line with less than 2 spaces before a comment. "
error_code_comments = "s004"

TODO = "Your program passed the line with TODO comment or has an incorrect format. "
error_code_todo = "s005"

TOO_MANY_BLANK_LINES = "Your program didn't warn about more than two blank lines between lines. "
error_code_blank_lines = "s006"

error_code_class_def_spaces = "s007"
SPACES_AFTER_CLASS_FUNC = "Your program should warn about multiple spaces after keyword 'class' and 'def'. "

error_code_class_name = "s008"
CLASS_NAME = "The program should warn about incorrect class name. "

error_code_func_name = "s009"
FUNC_NAME = "The program passed the function with the name not in snake_case style. "

error_code_arg_name = "s010"
ARG_NAME = "Your program should warn about function argument written not in snake_case style. "

error_code_var_func_name = "s011"
VAR_FUNC_NAME = "The program omitted warning about incorrect variable name in the function's body. " \
                "It should be written in the snake_case style. "

error_code_default_argument_is_mutable = "s012"
MUTABLE_ARG = "The program didn't warn about mutable function argument. "

FALSE_ALARM = "False alarm. Your program warned about correct line. "

cur_dir = os.path.abspath(os.curdir)


def test_1():
    file_path = f"tests{os.sep}linter_test_cases{os.sep}test1.py"
    output = [line.lower() for line in analyse(file_path)]

    if len(output) != 9:
        assert False

    if not (output[0].startswith(f"{file_path}: line 1: s004") or
            output[7].startswith(f"{file_path}: line 13: s004")):
        assert False

    if not (output[1].startswith(f"{file_path}: line 2: s003") or
            output[3].startswith(f"{file_path}: line 3: s003") or
            output[6].startswith(f"{file_path}: line 13: s003")):
        assert False

    if not (output[2].startswith(f"{file_path}: line 3: s001") or
            output[4].startswith(f"{file_path}: line 6: s001")):
        assert False

    if not (output[5].startswith(f"{file_path}: line 11: s006")):
        assert False

    if not output[8].startswith(f"{file_path}: line 13: s005"):
        assert False


def test_2():
    file_path = f"tests{os.sep}linter_test_cases{os.sep}test2.py"
    output = [line.lower() for line in analyse(file_path)]

    if not output:
        assert False

    for issue in output:
        if issue.startswith(f"{file_path}: line 6: ") or issue.startswith(f"{file_path}: line 10: "):
            assert False

    if not len(output) == 3:
        assert False

    if not output[0].startswith(f"{file_path}: line 1: {error_code_class_def_spaces}"):
        assert False

    if not output[1].startswith(f"{file_path}: line 4: {error_code_class_name}"):
        assert False

    if not output[2].startswith(f"{file_path}: line 14: {error_code_func_name}"):
        assert False


def test_3():
    file_path = f"tests{os.sep}linter_test_cases{os.sep}test3.py"
    output = [line.lower() for line in analyse(file_path)]

    if not output:
        assert False

    for issue in output:
        if issue.startswith(f"{file_path}: line 1: "):
            assert False

        if (issue.startswith(f"{file_path}: line 2: {error_code_default_argument_is_mutable}") or
                issue.startswith(f"{file_path}: line 6: {error_code_default_argument_is_mutable}") or
                issue.startswith(f"{file_path}: line 12: {error_code_default_argument_is_mutable}")):
            assert False

    if not len(output) == 1:
        assert False

    if not output[0].startswith(f"{file_path}: line 9: {error_code_default_argument_is_mutable}"):
        assert False


def test_4():
    file_path = f"tests{os.sep}linter_test_cases{os.sep}test4.py"
    output = [line.lower() for line in analyse(file_path)]

    if not output:
        assert False

    for issue in output:
        if issue.startswith(f"{file_path}: line 1: "):
            assert False

        if issue.startswith(f"{file_path}: line 6: {error_code_arg_name}"):
            assert False

        if issue.startswith(f"{file_path}: line 9: {error_code_arg_name}"):
            assert False

    if not len(output) == 1:
        assert False

    if not output[0].startswith(f"{file_path}: line 2: {error_code_arg_name}"):
        assert False


def test_5():
    file_path = f"tests{os.sep}linter_test_cases{os.sep}test5.py"
    output = [line.lower() for line in analyse(file_path)]

    if len(output) < 1:
        assert False

    for issue in output:
        if issue.startswith(f"{file_path}: line 1: "):
            assert False

        if issue.startswith(f"{file_path}: line 6: {error_code_var_func_name}"):
            assert False

        if issue.startswith(f"{file_path}: line 8: {error_code_var_func_name}"):
            assert False

    if not len(output) == 2:
        assert False

    for i, j in enumerate([3, 9]):
        if not output[i].startswith(f"{file_path}: line {j}: {error_code_var_func_name}"):
            assert False


def test_6():
    file3 = f"tests{os.sep}linter_test_cases{os.sep}test3.py"
    file4 = f"tests{os.sep}linter_test_cases{os.sep}test4.py"
    file5 = f"tests{os.sep}linter_test_cases{os.sep}test5.py"
    output = analyse(file3) + analyse(file4) + analyse(file5)

    if len(output) != 4:
        assert False

    if file3 not in output[0] or file4 not in output[1] or file5 not in output[2]:
        assert False
