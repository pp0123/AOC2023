from timedspinner import printspin 
from mytools import strtointlist

def wins(t,d):
    wins = 0

    for i in range(t + 1):
        
        #print a spinning cursor character
        printspin(0.15)    

        #actual calculation                  
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
print ('\b',ttl1)


