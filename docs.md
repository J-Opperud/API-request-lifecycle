## Overview

Inspect and document the complete anatomy of multiple API transactions.

The goal is to understand what is being sent in an HTTP request and what is being returned in the HTTP response.

## Structure

SCRIPT
│
│ Request
│ ├── Method
│ ├── URL
│ ├── Headers
│ └── Body
▼
JSONPlaceholder
│
│ Response
│ ├── Status code + reason
│ ├── Headers
│ └── Body
▼
SCRIPT

Design

We have three transactions:

- Request
  Method Endpoint body

- Get user
  GET /users/1 None
- Create post
  POST /posts JSON
- Update title
  PATCH /posts/1 JSON

Rather than writing the printing logic three times, we'll make a reusable function:

make request
↓
inspect request
↓
inspect response
↓
print anatomy

keeps the solution DRY.

## Time study

- perf_counter()

Is designed for measuring elapsed time. The difference between the start and end times gives the request duration in seconds, which is multiplied by 1000 to convert it to milliseconds.

It is useful for observing API latency, although it is not a precise measurement of server processing time because the duration also includes network and client-side overhead.

## Implementation Flow

Start
↓
Define reusable request function
↓
Make GET request
↓
Print request + response anatomy
↓
Make POST request
↓
Print request + response anatomy
↓
Make PATCH request
↓
Print request + response anatomy
↓
End
