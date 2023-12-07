def strtointlist(s): #make sure we are dealing with ints NOT strings in the list
    i=0
    for n in s:
        s[i]=int(n)
        i+=1
    return s
