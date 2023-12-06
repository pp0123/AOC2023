total = 0
total_part2 = 0
card ={}
mine ={}
with open("./input.txt", "r") as file:
    data = file.readlines()
    totalcards = [1 for _ in data]
    #print ('cards:',len(totalcards),'\n',totalcards)

    for line in data:
        current_line=line.strip('\n')
        print('before:',current_line)
        game,o = current_line.split(':')
        #print ('GAME AS READ:',game)
        game =game.split()[1]
        card,mine = list(o.split ('|'))
        
        card=card.split()
        mine=mine.split()
        c = set(card) 
        m = set (mine)
        union_ab = c & m
        match_num = len(union_ab)
        
        i=0
        for n in (c):
            if (n in mine):
                if ( i < 1):
                    i = 1
                else:
                    i *= 2
        total += i

        #print ('game:', game)
        #print (totalcards)
       
        ttlindex = int(game)-1
        for cardcount in range(len(union_ab)):
            #print ('cards:',totalcards,' index:',ttlindex,' i:', cardcount, ' n:',len(union_ab))
            #cards[index + i + 1] += cards[index]
            #print ('game:',ttlindex-1,' cardcount:',cardcount)
            totalcards[ttlindex + cardcount+1] += totalcards[ttlindex]
     
    for index in range(len(totalcards)):
        total_part2 += totalcards[index]

    print ('total part 1:', total)
    #print ('LINES:',game)
    #print (totalcards)
    print ('total part 2:',total_part2)
    





        