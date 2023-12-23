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
        if all(x==0 for x in next_s):
             return(a[0]) #return first element this time
        else:
             return(a[0] + (-1* next_sequence(next_s))) #subtract one sequence end fromt he other as we reduce sequences to zero

    for line in data:
        al.append(strtointlist(line.split()))
    
    #reduce sequece
    for i in (range(len(al))):
        ttl += next_sequence(al[i])
        
    print (ttl)

   