# gerent
Gerent is a simple and lightweight web-framework for MicroPython.

### pypi link:
https://pypi.org/project/gerent/
# TODO:
- beautify pyproject.toml  
- ✅ add post and put methods  
- ✅ add custom http_headers option  
- create docs (how does it work, pictures)  
- add favicon.ico support  
- ✅ create API root, with all url's  
- add examples  
- beutify micropython code?  
- add unitest tests  

# Example:
```python
import argent, socket

@argent.route("/hello/world")
def hello_world(request):
    return(200, {}, "Hello from Argent framework!")

# create socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

# run argent client
while True:
    argent.listen(s)
```
# DOCS:
### Sample url_linker:
```python
  {'route': '/hello/world', 'function': <function hello_world at 0x2000bf00>}  
  {'route': '/api', 'function': <function hello_world at 0x2000c0f0>}  
  {'route': '/controll/pico', 'function': <function hello_world at 0x2000c170>}  
  {'route': '/weather', 'function': <function hello_world at 0x2000c1f0>}  
  {'route': '/controll/esp8266', 'function': <function hello_world at 0x2000c270>}  
```

### Errors (TODO):
```python
Traceback (most recent call last):
  File "<stdin>", line 65, in <module>
  File "argent.py", line 95, in listen
  File "argent.py", line 8, in __get_route
IndexError: list index out of range
```
