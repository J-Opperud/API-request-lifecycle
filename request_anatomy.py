import time
import requests





BASE_URL = "https://jsonplaceholder.typicode.com"


def print_request_anatomy(response, elapsed_ms):
    request = response.request

    print("=" * 70)
    print(f"{request.method} {request.url}")
    print("=" * 70)



    print("\n Request Headers")
    print("-" * 70 + "\n")

    for name, value in request.headers.items():
        print(f"{name}: {value}")

    print("\n Request Body")
    print("-" * 70 + "\n")

    if request.body:
        print(request.body)

    else:
        print("None")

    print("\n Response")
    print("-" * 70 + "\n")

    print(f"Status: {response.status_code} {response.reason}")


    print("\n Response Headers")
    print("-" * 70 + "\n")



    print(f"Content-Type: {response.headers.get(
        'Content-Type',
        '(not provided)')}"
         )


    print(f"Content-Lenght: {response.headers.get(
        'Content-Lenght',
        '(not provided)')}"
         )

    print("\n Response Body")
    print("-" * 70 + "\n")
    

    print(response.text)
   

    print("\nELAPSED TIME")
    print("-" * 70)
    print(f"{elapsed_ms:.2f} ms")

    print()

def make_request(method, url, **kwargs):

    start = time.perf_counter()
    try:
        response = requests.request(
            method,
            url,
            **kwargs,
            )
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")



    elapsed_ms = (
        time.perf_counter() - 
        start) * 1000
    print_request_anatomy(response, elapsed_ms)

    return response


def main():
    # 1. GET a specific user
    make_request(
        "GET",
        f"{BASE_URL}/users/1"
        )

    # 2. POST a new post
    make_request(
        "POST",
        f"{BASE_URL}/posts",
        json={
            "title": "Learning REST APIs",
            "body": "Inspecting HTTP request and response anatomy.",
            "userId": 1,},
            )

    # 3. PATCH an existing post's title
    make_request(
        "PATCH",
        f"{BASE_URL}/posts/1",
        json={
            "title": "Updated REST API Title",},
            )


if __name__ == "__main__":
    main()
