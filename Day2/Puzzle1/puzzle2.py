
ttlgamevalue=0
with open("input.txt", "r") as file:
    data = file.readlines()
 
    for line in data:
        current_line=line.strip('\n')
        #print('before:',current_line)
        REDMAX = 0
        BLUEMAX= 0
        GREENMAX=0
        game = current_line.split(':')[0].split()[1]
        sets = current_line.split(':')[1].split(';')
        #print (game)
        #print (sets)
        for i in sets:
            rgb = i.split(',')
            #print (rgb)
            for j in rgb:
                onergb = j.split()
                match onergb[1]:
                    case "blue":
                        if (int(onergb[0]) > BLUEMAX):
                            BLUEMAX = int(onergb[0])
                            #print (game,':',"Blue:", onergb[0])
                    case "red":
                        if (int(onergb[0]) > REDMAX):
                            REDMAX = int(onergb[0])
                            #print (game,':',"Red:", onergb[0])
                    case "green":
                        if (int(onergb[0]) > GREENMAX):
                            GREENMAX = int(onergb[0])
                            #print (game,':',"Green:", onergb[0])
        print ('game:',game,'red:',REDMAX,' green:',GREENMAX, ' blue:', BLUEMAX,'gamepower:',BLUEMAX*GREENMAX*REDMAX)
        ttlgamevalue = ttlgamevalue + (REDMAX * GREENMAX * BLUEMAX)
        print ('ttlgamevalue:',ttlgamevalue)
    
