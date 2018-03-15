# Introduction to Python Multi-Processing

This note gives a very brief introdution to Python multi-processing. It is referred to this [post](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000). And I will add my own thought.

## About fork

`fork()` is not supported in Windows. My test environment is Mac. `fork()` is a very special funtional invocation, it will return twice. 

* The `fork()` in **parent process** will return the ID of child process. 
* The `fork()` in **child process** will always return 0.

### Code Snippet

```python
import os

print("Process {} starts".format(os.getpid()))
pid = os.fork()
if pid == 0:
    print("I am the child process {} and my parent is {}".format(os.getpid(),os.getppid()))
else :
    print("I am the parent {} and just create {}".format(os.getpid(),pid))
```

The result is

```
Process 10098 starts
I am the parent 10098 and just create 10099
I am the child process 10099 and my parent is 10098
```

## Cross Platform Multi-Processing

`fork()` is Unix/Lnix based. Python supports cross platform multi-processing using `multiprocessing`package.

*  `start()` ignites the process
* `join()` waits this process finishes before it continues

### Code Snippet

```python
from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process {} {}".format(name,os.getpid()))

if __name__ == "__main__":
    print("Inside parent process {}".format(os.getpid()))
    p = Process(target=run_proc, args=('kasihen',))
    print("now we start the child process")
    p.start()
    p.join()
    print("Come back to parent process{}".format(os.getpid()))
```

The result is 

```
Inside parent process 10145
now we start the child process
Run child process kasihen 10146
Come back to parent process10145
```



To be continued…...

