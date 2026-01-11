import os
import sys

def supports_color():
    if not sys.stdout.isatty():
        return False

    if os.name == "nt":
        return (
            "ANSICON" in os.environ or
            "WT_SESSION" in os.environ or
            os.environ.get("TERM_PROGRAM") == "vscode"
        )

    return True

#ANSI color codes have:
# Normal colors 30-37
# Bright colors 90-97

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAILRED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

if not supports_color():
    for attr in vars(BColors):
        if not attr.startswith("_"):
            setattr(BColors, attr, "")

# Usage
print(BColors.HEADER + "This is HEADER text" + BColors.ENDC)
print(f"{BColors.OKBLUE}This is OK in BLUE{BColors.ENDC}")
print(BColors.OKGREEN + "This is green text" + BColors.ENDC)
print(f"{BColors.WARNING}This is a warning in yellow{BColors.ENDC}")
print(f"{BColors.FAILRED}This is red text{BColors.ENDC}")
print(f"{BColors.FAILRED}{BColors.BOLD}This is bold red text{BColors.ENDC}")
