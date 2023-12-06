f = open("inputtest.txt").readlines()
total = 0
s = 0
cards = [1 for _ in f]
for index, line in enumerate(f):
    i=0
    print (line)
    line = line.split(":")[1]
    print (line)
    a, b = line.split("|")
    a, b = a.split(), b.split()
    print (a,'|',b)

    for n in (a):
        if (n in b):
            print (n)
            print (n in b)
            print (n,':',b)
            if ( i < 1):
                i += 1
            else:
                i = i * 2
    print  (i)

    total += i

    