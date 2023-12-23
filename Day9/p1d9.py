from mytools import strtointlist

ttl = 0 
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]
    al = list()
    
    def next_sequence(a):
        next_s = []

        #build next sequence
        for j in range(len(a)-1):
                next_s.append(a[j+1]-(a[j]))
        
        #if (sum(next_s)==0): #this does not work and cost me hours  [3,6,9,-3,-15] also sums to zero!!!
        if all(x==0 for x in next_s):
             return(a[-1])
        else:
             return(a[-1]+next_sequence(next_s))

    for line in data:
        #al.append([int(x) for x in line.split()])
        al.append(strtointlist(line.split()))
    
    #reduce sequece
    for i in (range(len(al))):
        ttl += next_sequence(al[i])
        
    print (ttl)

   