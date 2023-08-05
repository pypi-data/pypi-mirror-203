# Insights4CI - REST API Client

This directory is holding a rudimentary Python library for the insights4ci REST
API.

:warning: Since Insights4CI API is in constant development, this is the best
way to consume the API. We will keep this client in sync with the API.

## Installing it

    $ pip install . --user

or in "development mode":

    $ pip install -e .

The pip command-line flag -e is short for --editable, and . refers to the
current working directory, so together, it means to install the current
directory (i.e. your project) in editable mode. This will also install any
dependencies declared with install_requires and any scripts declared with
console_scripts. Dependencies will be installed in the usual, non-editable
mode.

## Using it

Now, you can import and consume the library:


```python
from insights4ci.client.api import Insights4CIClient, Project                                                                                                                      

client = Insights4CIClient(url="http://localhost:8000")                                                                                                                            
for project in Project.get_all(client): 
	print(project.data)
``` 
