l1 = lambda : True
print(l1)
print(l1())

l2 = lambda g,t: 0.5*g*t**2
print(l2)
print(l2(9.8,1))

l3 = lambda *args, **kwargs: (args,kwargs)
print(l3)
tuple1 = (1,2,3)
dic1 = {"k1":1,"k2":2}
print(l3(*tuple1,**dic1))

def build(x,y):
    return lambda :x**2+y**2

# lambda function can be a function's return value
f = build(1,2)
print(f)
print(f())

# lambda can shadow the global variable
a = 1;
b = 2;
c = 3;

def showthree(a,b,c):
    print(a,b,c)
    pass

f = lambda a:showthree(a,b,c)
f(8)