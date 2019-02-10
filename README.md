# Simple Python Debugger

Simple Python Debugger (sdebugger) is a simplistic debugger that helps user keep track which function is running with what arguments and their running time. It also check for potential type error using user's type annotations and the arguments type

# Install
```sh
pip install sdebugger
```
### 
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Usage

Use as a decorator
```sh
from sdebugger import Decorators

@Decorators.typecheck
@Decorators.timecheck
class Test:
    def __init__(self):
        pass 
    def method1(self):
        pass 
    def method2(self):
        pass 
```

User as a function

```sh
from sdebugger import Decorators

class Test:
    def __init__(self):
        pass 
    def method1(self):
        pass 
    def method2(self):
        pass 

newclass1 = Decorators.typecheck(Test())
newclass2 = Decorators.timecheck(newclass1())
```

Nested function

```sh
from sdebugger import Decorators

class Test:
    def __init__(self):
        pass 
    def method1(self):
        pass 
    def method2(self):
        pass 

newclass = Decorators.timecheck(Decorators.typecheck(Test()))
```
MIT
