REDMAX = 12
BLUEMAX=14
GREENMAX=13
gamevalue=0
failgamevalue=0
with open("input.txt", "r") as file:
    data = file.readlines()
    total = 0
 
    for line in data:
        current_line=line.strip('\n')
       #print('before:',current_line)
        FAILGAME = -1
        game = current_line.split(':')[0].split()[1]
        sets = current_line.split(':')[1].split(';')
        #print (game)
        for i in sets:
            rgb = i.split(',')
            for j in rgb:
                onergb = j.split()
                match onergb[1]:
                    case "blue":
                        if int(onergb[0]) > BLUEMAX:
                            FAILGAME = 1
                            #print (game,':',"Blue:", onergb[0])
                    case "red":
                        if int(onergb[0]) > REDMAX:
                            FAILGAME = 1
                            #print (game,':',"Red:", onergb[0])
                    case "green":
                        if int(onergb[0]) > GREENMAX:
                            FAILGAME = 1
                            #print (game,':',"Green:", onergb[0])
        if (FAILGAME < 0 ):
            gamevalue = gamevalue + int(game)
            #print ('pass:',game,':',gamevalue)
        else:
            failgamevalue = failgamevalue + int(game)
            #print ('fail:',game,':',failgamevalue)
    print ('fail:',game,':',failgamevalue)
    print ('pass:',game,':',gamevalue)

            
            
