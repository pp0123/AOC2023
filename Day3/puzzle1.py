import re

with open("inputtest.txt", "r") as file:
    data = file.readlines()
    #print (data)
    i=0
    ttl= 0 
    a={} #lines by character
    b={} #set of special characters by position
    g={} #set of special characters that are gears by position

    for line in data:
        current_line=line.strip('\n')
        a[i] = current_line
        i=i+1
    numlines=len(a)
    numchar=len(a[0])
    for i in range(numlines):
        for j in range(numchar):
            if a[i][j] not in '0123456789.':
                b[i,j] = a[i][j]               
                if a[i][j] == '*':
                    g[(i,j)] = []
    #print (g)              

            #else:
                #b[i,j] = ' '
    #for i in range(numlines):
        #for j in range(numchar):
            #print (b[i,j], end=' ') 
        #print ('\n')
    for i in range(numlines):
        for c in re.finditer(r'\d+', a[i]): #if we find a number (all possible numbers by coordinate)
            #print (c)
            tomatch = [] #set of coordinates to match against
            for k in range(c.start() - 1, c.end() + 1):
                tomatch.append((i - 1, k))
                tomatch.append((i, k))
                tomatch.append((i + 1, k))
                #print (tomatch)
            valid = False
            for p in tomatch: #are the possible coordinates in tomatch in the set of special characters
                #print (tomatch)
                #print (p)
                #print (g)
                if p in b:
                    valid = True
                    if p in g: # is the special character a gear
                        g[p].append(int(c.group()))
                        #print (tomatch)
                    #print (p)
                #print (g)
                    
            if valid:
                ttl = ttl + int(c.group())
print('Total:\t\t', ttl)
ttl2 = 0
for gear in g:
    if len(g[gear]) == 2:
        ttl2 = ttl2+ (g[gear][0] * g[gear][1])

#for g in gears:
#    if len(gears[g]) == 2:
#        p2_total += (gears[g][0] * gears[g][1])

print('Total part2:\t', ttl2)
            
