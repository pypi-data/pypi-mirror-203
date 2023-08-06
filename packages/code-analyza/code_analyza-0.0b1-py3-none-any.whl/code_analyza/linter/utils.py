import os


def find_indices(current_line):
    """Returns:
    - index of first semicolon that is not within a string or comment
    - index of first comment"""
    semicolon_index, comment_index = None, None
    quote = ""
    escape_chars = 0

    for index, char in enumerate(current_line):
        if escape_chars == 1:
            escape_chars = 2
        elif escape_chars == 2:
            escape_chars = 0

        if quote == "" and escape_chars == 0 and (char == "'" or char == '"' or char == "'''" or char == '"""'):
            quote += char
        elif quote == char and escape_chars == 0:
            quote = ""
        elif char == "\\" and quote:
            escape_chars = 1
        elif char == ";" and quote == "" and semicolon_index is None:
            semicolon_index = index
        elif char == "#" and quote == "" and comment_index is None:
            comment_index = index
            break

    return semicolon_index, comment_index


def list_file_paths(folder, basepath, paths=[]):
    """List paths for all python files within the project directory"""
    for content in folder:
        full_path = os.path.join(basepath, content)

        if os.path.isfile(full_path) and content.endswith(".py"):
            paths.append(full_path)
        elif os.path.isdir(full_path):
            list_file_paths(content, full_path, paths)

    return paths
