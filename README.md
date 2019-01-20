# method-versioning

> A processing module that accepts processing data and a "version of the steps".

## Project structure

method-versioning structure looks as follows:

    method-versioning/
    ├── method_versioning
    ├── tests
    └── main.py

### method_versioning folder

The folder is a Python package, which contains the decorator for methods versioning.

The content:

    method_versioning/
    ├── __init__.py
    └── decorator.py

* **decorator.py:** contains a decorator ***versioning***, which set function attributes such as *mv_name* and *mv_version*.

### tests folder

The folder is a Python package, which contains test functions and a test config file.

The content:

    tests/
    ├── __init__.py
    ├── add_functions.py
    ├── config.py
    ├── divide_functions.py
    └── multiply_functions.py

* **add_functions.py, divide_functions.py and multiply_functions.py:** contains test functions and their versions.

#### config.py

A file, which have to contain the next variables:
* **FUNCTION_PATHES** a list of paths, where processing functions is located.
* **PIPELINE_FUNCTIONS** a list of dictionaries, which defines functions, their versions and order of executing.
* **DATA** a dictionary, which contains input processing data.


### main.py

An entry-point of the package, which uses the decorator ***versioning*** and a ***config file*** for data processing pipelines. Path to the config file have to be in dot-notation. 


## Running the tests

Run the following command to start unit tests:
```console
python main.py --config tests.config
``` 


## How to use?

* Create your own package with functions and their versions using the decorator **method_versioning.decorator.versioning**.
* Create a config file with the variables **FUNCTION_PATHES**, which points on your scripts with the functions, **PIPELINE_FUNCTIONS** and **DATA**.
* Run the following command:
```console
python main.py --config <path.to.your.config.file>
``` 

And there you go!
