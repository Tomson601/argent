
BUFFER_SIZE = 512

http_headers = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'

avaliable_routes = [
    {
        "route": "/",
        "methods": ['GET'],
        "headers": http_headers,
        "response": "Hello from Raspberry Pi Pico!",
        "response_file": None,
    }
]


# Create Request class


def __handle_route(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    route = response_array[0].split(' ')[1]
    return route


def __handle_respone(client, route):
    client.send(avaliable_routes[0]["headers"])
    client.send(avaliable_routes[0]["response"])
    client.close()


def __check_or_append_route(url, methods, response):
    # Check if path exists:
    found = False
    for path in avaliable_routes:
        if path["route"] == url:
            found = True
            break
    # If path not exists- create new entry in avaliable_routes
    if not found:
        # If response is defined, it is master choice
        if response:
            response_file = None
        elif response_file:
            response = None
        else:
            response = "Default view"

        avaliable_routes.append({
            "route": url,
            "methods": methods,
            "response": response,
            "response_file": response_file
        })


def listen(socket):
    client, addrress = socket.accept()
    print(f'New connection from: {addrress}')

    request = client.recv(BUFFER_SIZE)

    route = __handle_route(request)
    # Check if route exists:
    found = False
    for path in avaliable_routes:
        if path["route"] == route:
            found = True
            break
        if not found:
            # return response(404)
            pass
    respone = __handle_respone(client, route)

    # accept socket connection
    # read_request
    # match_route
    # send response
    # close connection

# 'GET', 'POST', 'PUT'


def route(url, methods='GET'):
    return lambda func: __check_or_append_route(url, methods)
