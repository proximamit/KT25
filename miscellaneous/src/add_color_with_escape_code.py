# Define color codes
class BColors:
    HEADER = '\033[95m' # Purple
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAILRED = '\033[91m' # Red
    ENDC = '\033[0m' # Reset
    BOLD = '\033[1m'

# Usage
print(BColors.HEADER + "This is HEADER text" + BColors.ENDC)
print(f"{BColors.OKBLUE}This is OK in BLUE{BColors.ENDC}")
print(BColors.OKGREEN + "This is green text" + BColors.ENDC)
print(f"{BColors.WARNING}This is a warning in yellow{BColors.ENDC}")
print(f"{BColors.FAILRED}This is red text{BColors.ENDC}")
print(f"{BColors.FAILRED}{BColors.BOLD}This is bold red text{BColors.ENDC}")
