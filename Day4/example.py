f = open("inputtest.txt").readlines()

s = 0
cards = [1 for _ in f]
print ('CARDS:', type(cards),len(cards))
print (cards)
for index, line in enumerate(f):
    print (index)
    line = line.split(":")[1]
    print (line)
    a, b = line.split("|")
    a, b = a.split(), b.split()
    print (a,'|',b)
    

    n = len(set(a) & set(b))

    if n > 0:
        s += 2 ** (n - 1)
    print (cards)
    print ('index:',index)
    
    for i in range(n):
        print ('cards:',cards,' index:',index,' i:', i, ' n:',n)
        cards[index + i + 1] += cards[index]
    print ('CARDS:', type(cards))
    print (cards)
print(s, sum(cards))