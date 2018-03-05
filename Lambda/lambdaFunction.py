def build(x,y):
    return lambda :x**2+y**2

# lambda function can be a function's return value
f = build(1,2)
print(f)
print(f())