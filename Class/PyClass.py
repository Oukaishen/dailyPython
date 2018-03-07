
"""Quite important site
https://docs.python.org/3/tutorial/classes.html
"""

class MyClass:
    """A simple example clasee"""
    i = 12345
    def f(self):
        return "hello world."

x = MyClass()

#point 1: x.f is not the same as MyClass.f
print(hex(id(MyClass)))
print(MyClass.f)
print(hex(id(MyClass.f)))
# this will cause error cause this is not instance object
#print(MyClass.f())
print(x.f)
print(x)