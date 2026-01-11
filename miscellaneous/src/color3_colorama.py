# In case of issue
"""
from colorama import init, Fore, Back, Style
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    from colorama import init, Fore, Back, Style
ModuleNotFoundError: No module named 'colorama'
"""
# Install colorama
## pip install colorama

from colorama import init, Fore, Back, Style

# Initialize colorama (needed for Windows)
init(autoreset=True)

print(Fore.RED + "This is red text")
#print(Fore.RED + "This is red text" + Style.RESET_ALL)
print(Back.GREEN + "This has a green background")
print(Fore.YELLOW + Back.BLUE + "Yellow text on blue background")
print(Style.BRIGHT + "This is bright text")
print(Style.BRIGHT + Fore.BLUE + "This is bright blue text")
print("This text is normal because of autoreset=True")

