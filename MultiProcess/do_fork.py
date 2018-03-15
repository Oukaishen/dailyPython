import os

print("Process {} starts".format(os.getpid()))
pid = os.fork()
if pid == 0:
    print("I am the child process {} and my parent is {}".format(os.getpid(),os.getppid()))
else :
    print("I am the parent {} and just create {}".format(os.getpid(),pid))