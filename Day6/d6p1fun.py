import time


#following globals all used for timer and printing a spinner while calculating
start = time.time()
current_time=0
buf_arg = 0
c = 43
newc=215
oldc=0

#timer (got to be a better way to do this without globals)
def is_time(t):
    global start, current_time
    current_time = time.time()
    if (current_time - start >= t):
        start = current_time
        return True
    else:
        return False
    
def strtointlist(s): #make sure we are dealing with ints NOT strings in the list
    i=0
    for n in s:
        s[i]=int(n)
        i+=1
    return s

def wins(t,d):
    global c,newc,oldc
    wins = 0
    flip_char = False

    for i in range(t + 1):
        current_time = time.time()
        if is_time(0.25): #print a spinning +
            flip_char = not flip_char
            if flip_char:
                oldc = c
                c = newc
                newc = oldc
            print('\b', end=chr(c), flush=True)                          
        distance = (t - i) * i
        if distance > d:
            wins += 1
    return wins

ttl1 = -1
file = open("input3.txt", "r")
data = file.read()
[t,d] = data.strip().splitlines()

times = strtointlist(t.removeprefix('Time:').split())
distance =  strtointlist(d.removeprefix('Distance:').split())
i=0
for n in times:
    if ttl1 < 0: #find the first one
        ttl1 = wins(times[i],distance[i])
    else: #multiply the rest
        ttl1= ttl1*wins(times[i],distance[i]) 
    i+=1
print ('\n',ttl1)


