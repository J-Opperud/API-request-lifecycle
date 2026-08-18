

## Objective

Understand the structure of an HTTP request and response by inspecting:

HTTP method
URL
Request headers
Request body
Response status code and reason
Response headers
Response body
Request elapsed time
API Transactions
Request	Method	Endpoint	Body
Get user	GET	/users/1	None
Create post	POST	/posts	JSON
Update post title	PATCH	/posts/1	JSON
Request Anatomy
SCRIPT
    │
    │  Request
    │  ├── Method
    │  ├── URL
    │  ├── Headers
    │  └── Body
    ▼
JSONPlaceholder
    │
    │  Response
    │  ├── Status code + reason
    │  ├── Headers
    │  └── Body
    ▼
SCRIPT

Project Structure
request-anatomy/
├── request_anatomy.py
└── README.md

## Requirements
Python 3
requests

Install the dependency:

pip install requests

## Run
python request_anatomy.py


The script prints each transaction with clear separators so the request and response anatomy can be compared.

## Design

The request inspection and output formatting are handled through reusable functions rather than duplicating the same logic for each API call.

make request
     ↓
inspect request
     ↓
inspect response
     ↓
print anatomy


This keeps the implementation DRY while giving all three transactions a consistent output format.


Although this exercise focuses on successful transactions, real-world API clients also need to account for:

Network and connection failures
Request timeouts
HTTP error responses (4xx and 5xx)
Redirects
Empty response bodies
Missing response headers
Invalid JSON responses
Authentication and sensitive headers
Large response bodies
Retries and rate limiting

These are documented as considerations rather than over-engineering this small exercise.


That mental model is useful when building, testing, and debugging REST APIs.

