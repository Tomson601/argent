# argent
Argent is a simple and lightweight web-framework for MicroPython.

# TODO:
- beautify pyproject.toml  
- add post and put methods  
- add custom http_headers option  
- create docs  


# Example:
```python
import argent

@argent.route("/hello/world")
def hello_world(request):
    return(200, {}, "Hello from Argent framework!")

# connect to wi-fi

# create socket

while True:
    argent.listen(socket)
```
