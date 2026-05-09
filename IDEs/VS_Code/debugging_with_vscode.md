# Debugging using VS Code 

To debug a Python program in Visual Studio Code, we use:

- **Breakpoints** - to pause execution at a line
- **Step Over / Step Into / Continue** - move through code line-by-line
- **Variables panel / Watch / Debug Console** - inspect values as they change

# To put a breakpoint

### Using Mouse
- Click in the **left gutter** beside the line number.
- A red dot appears.
- for e.g. we can place it inside the `for` loop to stop every iteration
-  To remove the breakpoint, Click on the **Red Dot**

### Using Keyboard
- Place the cursor on the line with the breakpoint and press `F9` 
- `F9` can be used to toggle it off (or on)

# Start debugging

- Click on the **Down Arrow** next to the **Play** icon on the ***top right***
- The **Play** icon will be displayed only when we open a Python file 
in the editor and Python extension is installed
- In the Menu opened, click on **Python Debugger: Debug Python File**

### or 

- Click on the **Run and Debug icon** in the ***Activity Bar** (in the extreme
left)

### or 

- Press `Ctrl + Shift + D`
- and click on **Run and Debug**

## Example Workflow

1. Put breakpoint
1. Start debugging (as mentioned above)
1. Use `F10` repeatedly to **Step Over**
1. Watch Variables panel (e.g. watch how variables change in a loop)
1. Press `Shift + F5` to end debugging
1. Click on the **Red Dot(s)** in the gutter to remove ***Breakpoints***

---

# Summary

| Action    | Shortcut           | Meaning                                     |
| --------- | ------------------ | ------------------------------------------- |
| Continue  | `F5`               | Run until next breakpoint                   |
| Step Over | `F10`              | Execute current line, stay in same function |
| Step Into | `F11`              | Go inside function call                     |
| Step Out  | `Shift + F11`      | Exit current function                       |
| Restart   | `Ctrl + Shift + F5`| Restart debugger                            |
| Stop      | `Shift + F5`       | End debugging                               |

---