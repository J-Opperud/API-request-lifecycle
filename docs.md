## Overview


The Status Code Detective is a small Python diagnostic program designed to test several REST API endpoints and explain the responses.

The project uses JSONPlaceholder as the test API and the Python requests library to send HTTP requests.

The main objective is to connect HTTP methods and API endpoints with the status codes returned by the server.




## Structure

get_status_category()
        ↓
"What category is this?"

get_description()
        ↓
"What does this status mean?"

print_report()
        ↓
"How should I display it?"


The program separates the diagnostic process into several functions.



This function converts the numeric HTTP status code into a general category.

def get_status_category(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Other"


Using ranges makes the function reusable for many different HTTP status codes.

For example:

200 → Success
201 → Success
204 → Success

400 → Client Error
404 → Client Error

500 → Server Error
503 → Server Error

get_description()

The description function provides a human-readable explanation for common status codes.

Examples:

200 → Request succeeded — resource returned
201 → Resource created successfully
404 → Resource not found


This keeps the status interpretation separate from the actual HTTP request logic.

print_report()

The reporting function combines the status category and description into a readable format.

The output follows this structure:

GET /posts/1
  Status: 200 (Success)
  Description: Request succeeded — resource returned


Keeping formatting in its own function makes the main test section easier to read.

Bonus: Generic Request Function

The project also uses a reusable request function:

def test_request(method, url, json_data=None):
    return requests.request(
        method,
        url,
        json=json_data
    )


Instead of creating separate functions for GET, POST, DELETE, and other methods, the HTTP method can be passed as an argument.

For example:

test_request("GET", url)
test_request("DELETE", url)
test_request("POST", url, post_data)


This demonstrates that the HTTP method can be treated as data rather than hardcoded into separate functions.

Debugging Lesson

One of the bugs encountered during development was a mismatch between the requested endpoint and the endpoint being reported.

For example:

f"{BASE_URL}/post/1"


was being reported as:

GET /posts/1


The missing s caused the API request to target the wrong endpoint.

The corrected request is:

f"{BASE_URL}/posts/1"


This demonstrates an important debugging principle:

The information printed by a diagnostic tool must accurately represent the request actually sent to the server.

HTTP Status Code Model

The project reinforces the standard HTTP status-code categories:

1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error



Status codes communicate the result.

200 indicates success.
201 indicates creation.
404 indicates that a resource could not be found.

Reusable functions improve structure.

Diagnostic output should accurately represent the request being tested.
