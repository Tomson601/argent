BUFFER_SIZE = 512

http_headers = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'

url_linker = []


def __get_route(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    route = response_array[0].split(' ')[1]
    return route


def __send_respone(client, code, headers, response):
    client.send(headers)
    client.send(response)
    client.close()


def __create_url_linker(url, methods, function):
    # Check if path exists:
    found = False
    for path in url_linker:
        if path["route"] == url:
            found = True
            break
    # If path not exists- create new entry in url_linker
    if not found:
        url_linker.append({
            "route": url,
            "function": function,
        })


def __get_route_function(route):
    function = None

    for entry in url_linker:
        if entry["route"] == route:
            function = entry["function"]

    return function


def listen(socket):
    client, addrress = socket.accept()
    request = client.recv(BUFFER_SIZE)
    route = __get_route(request)
    function = __get_route_function(route)

    print(f'New connection from: {addrress}')
    print("\n", request, "\n")

    if function != None:
        code, headers, response = function(request)
        __send_respone(client, code, http_headers, response)
    else:
        with open("404.html", "r") as html_404:
            __send_respone(client, 404, http_headers, html_404.read())


def route(url, methods='GET'):
    return lambda function: __create_url_linker(url, methods, function)
