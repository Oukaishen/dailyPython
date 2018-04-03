# Lambda 

kaishen, 8 Mar, 2018. Sicked in home -.-

Lambda is quite useful when you want to directly input a function as an argument.

Lambda no need to write `return`, it will return the expression's value.

## Some Key point

```python
def(x):
	return x*x
```

is equivalent to

```python
lambda x:x*x
```

### Arguments

With lambda expression, you can have no argument, 1 argument, 2 arguments, *args, and even **kargs.

**no arg**

```python
l1 = lambda : True
print(l1)
print(l1())
```

```
<function <lambda> at 0x10453bb70>
True
```

**2 args**

```python
l2 = lambda g,t: 0.5*g*t**2
print(l2)
print(l2(9.8,1))
```

```
<function <lambda> at 0x10453ab70>
4.9
```

***args and \*kwargs**

```python
l3 = lambda *args, **kwargs: (args,kwargs)
print(l3)
tuple1 = (1,2,3)
dic1 = {"k1":1,"k2":2}
print(l3(*tuple1,**dic1))
```

```
<function <lambda> at 0x103d3ac80>
((1, 2, 3), {'k1': 1, 'k2': 2})
```

### Lambda as return value

lambda can act as returned value

```python
def build(x,y):
    return lambda :x**2+y**2

# lambda function can be a function's return value
f = build(1,2)
print(f)
print(f())
```

```
<function build.<locals>.<lambda> at 0x103d3ad90>
5
```



