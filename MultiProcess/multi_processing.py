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