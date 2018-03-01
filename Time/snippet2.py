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