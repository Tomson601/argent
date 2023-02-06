avaliable_routes = [
    {
        "route": "/",
        "methods": ['GET'],
    },
    {
        "route": "/e",
        "methods": ['GET'],
    },
    {
        "route": "/XDDD",
        "methods": ['GET'],
    },
    {
        "route": "/hello/world",
        "methods": ['GET'],
    }
]

request_data = b'GET / HTTP/1.1\r\nHost: 192.168.1.77\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'


def __handle_route(request):
    decoded_request = request.decode()
    response_array = decoded_request.split("\n")
    route = response_array[0].split(' ')[1]
    return route


def __check_or_append_route(url, methods):
    # Check if path exists:
    found = False
    for path in avaliable_routes:
        if path["route"] == url:
            found = True
            break
    # If path not exists- create new entry in avaliable_routes
    if not found:
        avaliable_routes.append({
            "route": url,
            "methods": methods,
        })


def route(url, methods='GET'):
    return lambda func: __check_or_append_route(url, methods)


@route("/hello/world")
def hello_world_url():
    pass
