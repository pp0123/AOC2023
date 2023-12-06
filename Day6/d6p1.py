def strtointlist(s):
    i=0
    for n in s:
        s[i]=int(n)
        i+=1
    return s

def wins(t,d):
    #print (t,':',d)
  
    wins = 0
    for i in range(t + 1):
        print('.', end='')
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
    #print (times[i],':',distance[i])
    if ttl1 < 0:
        ttl1 = wins(times[i],distance[i])
    else:
        ttl1= ttl1*wins(times[i],distance[i]) 
    i+=1
    #print('.', end='')
print (ttl1)


