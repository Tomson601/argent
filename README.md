# argent
Argent is a simple and lightweight web-framework for MicroPython.

# TODO:
- beautify pyproject.toml  
- add post and put methods  
- add custom http_headers option  
- create docs  


# Example:
```python
import argent, socket

@argent.route("/hello/world")
def hello_world(request):
    return(200, {}, "Hello from Argent framework!")

# connect to wi-fi

# create socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

# run argent client
while True:
    argent.listen(socket)
```
