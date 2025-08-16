# Virtual Environments in Python

## There are different modules to create virtual environments in Python.
## However `venv` is the built-in module since Python 3.3 and is preferred over legacy 3rd party modules 

### A `virtual environment` is an isolated environment to manage project-specific dependencies without interfering with other projects or the original Python installation
---

### Create and Enter virtual environment

- `cd` to the root directory of the project 
- Choose a name for the virtual environment. While any name can be used, some of the common names used are `.venv`, `venv`, `myenv`. Sometimes project specific names are used for virtual environment directory 

```python
    python -m venv venv
```
- the last argument provided is the name of the directory that will contain the virtual environment files
- this creates a folder (with the chosen name) containing the isolated Python environment
---
### To exit the virtual environment

`deactivate`
---
### To activate the virtual environment

> Windows

`venv\scripts\activate`

> Linux

`source venv/bin/activate`

### Create a requirements.txt file in the root directory of the Python project
- Generate the file automatically using pip freeze
- After installing all necessary packages in the virtual environment, use pip freeze to generate the file
- pip freeze > requirements.txt
- Alternatively create the file manually and enter the names of the required external modules
- To install modules from requirements.txt

`pip install -r requirements.txt`

---