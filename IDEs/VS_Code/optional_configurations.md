### Set up a vertical line to show the limit of characters on a line 

- Click on `Manage` (cogwheel or gear icon at the bottom left)
- Click on `Settings`   
- In the `Search Settings` textbox, type **rulers**
- Click on the link  `Edit in settings.json`
- Update the settings to show a vertical line at the 80th character position

```json
    "editor.rulers": [
        80,
    ]
```

### Optional VS Code Extensions for Formatting

- (optional) Search and install the `Black` or `autopep8` formatting extensions
