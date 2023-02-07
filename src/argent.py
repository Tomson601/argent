BUFFER_SIZE = 512

http_headers = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'

url_linker = []


def __get_route(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    route = response_array[0].split(' ')[1]

    return route


def __get_method(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    method = response_array[0].split(' ')[0]

    return method


def __validate_method(method, route):
    for entry in url_linker:
        if entry["route"] == route:
            if method in entry["methods"]:
                return True
    return False


def __send_respone(client, code, headers, response):
    headers = f'HTTP/1.0 {code} OK\r\nContent-type: text/html\r\n\r\n'
    client.send(headers)
    client.send(response)
    client.close()


def __create_url_linker(url, methods, function):
    # Check if path exists:
    found = False
    for entry in url_linker:
        if entry["route"] == url:
            found = True
            break
    # If path not exists- create new entry in url_linker
    if not found:
        url_linker.append({
            "route": url,
            "methods": methods,
            "function": function,
        })


def __get_route_function(route):
    function = None

    for entry in url_linker:
        if entry["route"] == route:
            function = entry["function"]

    return function


def __create_root_site():
    html_root = "<html><body><h1>Server root:\n</h1>"
    html_root += "<h2>possible routes:\n</h2>"
    for entry in url_linker:
        html_root += "<h3>- " + entry["route"] + "</h3>" + "\n"
    html_root += "</body></html>"

    return html_root


def listen(socket):
    html_root_view = __create_root_site()
    client, addrress = socket.accept()
    request = client.recv(BUFFER_SIZE)

    route = __get_route(request)
    function = __get_route_function(route)
    method = __get_method(request)

    print(f'New connection from: {addrress}')
    print("\n", request, "\n")

    if function != None:
        # Check if method is defined
        if __validate_method(method, route) == False:
            __send_respone(client, 405, http_headers, "405 Method not allowed")
        # If method is defined, send normal response
        else:
            code, headers, response = function(request)
            __send_respone(client, code, http_headers, response)
    # if "/"- root url is not defined in url_linker send default response:
    elif route == "/":
        __send_respone(client, 200, http_headers, html_root_view)
    else:
        with open("404.html", "r") as html_404:
            __send_respone(client, 404, http_headers, html_404.read())


def route(url, methods=['GET']):
    return lambda function: __create_url_linker(url, methods, function)
