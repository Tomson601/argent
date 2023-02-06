



# Create Request class

def listen(socket):
    # accept socket connection
    # read_request
    # match_route
    # send response
    # close connection

def route(rule, method='GET'):
    return lambda func: __on_request(method, rule, func)
