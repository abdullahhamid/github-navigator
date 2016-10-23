# GitHub Navigator

This python web application takes a parameter "search_term" as input and queries GitHub API to look for matching repositories. The top 5 newest repositories with some information about latest commits
 are displayed in a html template.
 
## Dependencies

 - [Python] (https://www.python.org/downloads/) - tested on version 2.7.6
 - [pip] (https://pypi.python.org/pypi/pip)
 - [flask] (http://flask.pocoo.org/)
 - [requests] (http://docs.python-requests.org/en/master/)

## Usage

Run the command: 
`python application.py`

Go to browser and make a GET request e.g. 
`http://localhost:5000/navigator?search_term=arrow`

To run the tests, run the command: 
`python application_test.py` 