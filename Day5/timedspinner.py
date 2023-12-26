import time
import itertools

#following globals all used for timer and printing a spinner while calculating
start = time.time()
current_time=0
spinner = itertools.cycle('-/|\\')

#timer (got to be a better way to do this without globals)
def is_time(t):
    global start, current_time
    current_time = time.time()
    if (current_time - start >= t):
        start = current_time
        return True
    else:
        return False

def printspin(t):
    if is_time(t):
            print('\b', end=next(spinner), flush=True)    