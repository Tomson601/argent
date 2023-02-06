# argent
Argent is a simple and lightweight web-framework for MicroPython.

# TODO:
- beautify pyproject.toml  

# Example:
```python
import argent

@argent.url("/hello/world")
def hello_url(request):
    return(200, {}, 'Hello url!')

# this_section --> connect to wi-fi

# this section --> create socket

while True:
    argent.listen(socket)
```
