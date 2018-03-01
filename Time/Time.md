# Time 

The standard doc can be found [here](https://docs.python.org/3/library/time.html).

Common used methods includes **time()**,

## Code Snippet

```python
def time_function(f,*args):
    """
    call a function f with args and return the time (in seconds) that it took to execute
    :param f:
    :param args:
    :return:
    """
    import time
    tic = time.time()
    f(*args)
    toc = time.time()
    return toc - tic

def sum2num(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

timecost = time_function(sum2num,2,3,4,6)
print("The function took {:.6f} seconds to finish".format(timecost))
```

The result is, understandings about ***args** can be found in [here](https://stackoverflow.com/questions/6289646/python-function-as-a-function-argument) and [here](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000).

```
The function took 0.000003 seconds to finish
```

