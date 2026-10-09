1. What happens when you docker run the same image twice?

Docker creates two separate containers from the same image. Each container has its own writable filesystem, processes, and network identity.
Separate containers Each runs independently and has its own container ID.

2. What happens to files created inside a container when it stops?

Files created inside a container's writable layer normally remain when the container stops, but they are lost when the container is removed.
You can restart the same container and find the file. If you remove the container the file is deleted along with the container's writable layer.

3. How is the -p flag used to map ports?

The -p flag publishes a container port on the host machine so that applications outside the container can reach it.

docker run -p HOST_PORT:CONTAINER_PORT IMAGE

docker run -d -p 8080:80 nginx

This means:

    Host port: 8080

    Container port: 80

    Result: Requests to port 8080 on your host are forwarded to port 80 in the container.
