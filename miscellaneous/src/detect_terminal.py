import os

print(os.environ.get("TERM_PROGRAM"))

# Output:
'''
vscode - If executed from VS Code
None - If executed from Linux terminal
'''

for key in ["TERM_PROGRAM", "WT_SESSION", "ANSICON"]:
    print(key, "=", os.environ.get(key))
