# git one time (first time) configuration

## Configure username and email 
- git config --global user.name "Your_First_Name Last_Name"
    - e.g. git config --global user.name "Jack Dawson"
- git config --global user.email <valid_email>
    - e.g. git config --global user.email programmer@gmail.com

---

### To check the current configuration

- git config --global --get user.name
- git config --global --get user.email
---
### To check COMPLETE configuration 

- git config --global --list

---

### Optionally, configure the default text editor for writing commit messages 

- To check the **current editor** configuration
    - git config --global core.editor
- To configure the **default text editor** 
 
|    Configure Editor as     |          Command                                                                                   |
|:--------------------------:|:--------------------------------------------------------------------------------------------------:|
|         vim                | git config --global core.editor "vim"                                                              |
|        VS Code             | git config --global core.editor "code --wait"                                                      |
|    Notepad++ (Windows)     | git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar"  |

---

### Optionally, configure the behavior of git push

- To check the current configuration
    - git config push.default
- To configure the Recommended Configuration - simple (if not already configured)
    - git config --global push.default simple

--- 
### To view all configurations at once (along with the config file name and path)

- To view all configurations at once, along with where they are defined, we can use
    - git config --list --show-origin

---

## Other ways to view and edit the configuration

- Open the global Git configuration file in the current default text editor, allowing us to view and edit all our user-specific Git settings directly
- ***git config --global -e***
- We can manually add, modify, or remove settings in a single go, instead of using separate git config commands for each setting.
- The changes will take effect immediately once we save and close the editor
