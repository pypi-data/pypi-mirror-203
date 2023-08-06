import sys

from .linter.checks import analyse

args = sys.argv
base_path = args[1]
issues = analyse(base_path)

if len(issues):
    print("\n".join(issues))
