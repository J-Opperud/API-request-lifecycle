
## Overview
A Python diagnostic tool that sends HTTP requests to the JSONPlaceholder
 REST API and reports the response status, status category, and a brief description.

Assignment Objective

The goal of this assignment is to practice interpreting HTTP status codes and understanding how REST APIs respond to successful requests, client errors, and other responses.



## Technologies
Python 3
requests
REST API
JSONPlaceholder
Running the Project

Install the requests library:

pip install requests


## Run the diagnostic script:

python status-code-detective.py

Status Code Categories

The script groups HTTP responses into broad categories:

2xx → Success
4xx → Client Error
5xx → Server Error


Responses outside these ranges are categorized as Other.

## Project Structure
API-diagnostic/
├── status-code-detective.py
├── README.md
└── docs/
    └── status-detective.md

