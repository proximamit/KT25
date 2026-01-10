# VS Code for Python programming

## 1. Install Python

Before VS Code, make sure Python is installed.

1. Download Python from **python.org**
2. During installation (Windows):
   * Check **“Add Python to PATH”**
3. Verify installation:
 ```bash
   python --version
   ```

   or

   ```bash
   python3 --version
  
   ```
   or 

  ```bash
   python3 -V
   ```

---
## 2. Install Visual Studio Code

1. Download VS Code from **code.visualstudio.com**
    `https://code.visualstudio.com/Download`

2. Install with default settings

---

## 3. Install the Python Extension in VS Code

1. Open **VS Code**
2. Click **Extensions** (left sidebar) or press:

   ```
   Ctrl + Shift + X
   ```
3. Search for **Python**
4. Install **Python Extension for Visual Studio Code by Microsoft**


## 4. Select Python Interpreter

1. Press:

   ```
   Ctrl + Shift + P
   ```
2. Type:

   ```
   Python: Select Interpreter
   ```
3. Choose the Python version we wish to use with VS Code

    - We can see the selected interpreter at the bottom-right of VS Code.

## 5. Run Python Code 

### Option 1: Run Button
- Click the **Run** button (top-right)

### Option 2: Terminal

1. Open terminal:

   ```
   Ctrl + `
   ```
2. Run:

   ```bash
   python hello.py
   ```

---

## 6. Useful VS Code Shortcuts

| Action          | Shortcut              |
| --------------- | --------------------- |
| Command Palette | `Ctrl + Shift + P`    |
| Open Terminal   | `Ctrl + `\` (backtick)|
| Comment Line    | `Ctrl + /`            |

---

- Open the Command Palette with (`Command+Shift+P` on `macOS` and `Ctrl+Shift+P` on `Windows/Linux`) or use just `F1` on all platforms

- Alternatively, from the top `menu` Click `View`, `Command Palette`

- Command Palette is
    - a central hub for controlling the VS Code application
    - an interactive search box - to search for and execute any available command within VS Code

- example usage:
    - Consider a python code with mix of spaces and tabs
    - To fix - replace all tab characters with the spaces
        - Open the Command Palette
        - Start typing `Convert Indentation to Spaces`
        - Select the Convert Indentation to Spaces option from the dropdown list and press Enter to `Run the command`
