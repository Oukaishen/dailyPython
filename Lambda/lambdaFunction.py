def build(x,y):
    return lambda :x**2+y**2

# lambda function can be a function's return value
f = build(1,2)
print(f)
print(f())

a = 1;
b = 2;
c = 3;

def showthree(a,b,c):
    print(a,b,c)
    pass

f = lambda a:showthree(a,b,c)
f(8)