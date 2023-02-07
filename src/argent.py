BUFFER_SIZE = 512

http_headers = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'

url_linker = []


def __get_route(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    route = response_array[0].split(' ')[1]
    return route


def __send_respone(client, code, headers, response):
    print("\n")
    print(type(headers), headers)
    print(type(response), response)
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
    for entry in url_linker:
        if entry["route"] == route:
            function = entry["function"]

    return function


def listen(socket):
    client, addrress = socket.accept()
    print(f'New connection from: {addrress}')

    request = client.recv(BUFFER_SIZE)

    route = __get_route(request)
    
    print(route)
    
    function = __get_route_function(route)
    print(function)
    if function != None:
        code, headers, response = function(request)
        __send_respone(client, code, http_headers, response)
    else:
        __send_respone(client, 404, http_headers, "ERROR 404, not found")
    # socket.close()


def route(url, methods='GET'):
    return lambda function: __create_url_linker(url, methods, function)

# @route("/hello/world")
# def hello_world_url(request):
#     return(200, {}, "Hello world!")

