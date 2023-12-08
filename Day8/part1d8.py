direction = {}
step=0 
#notFound = False
def build_dict(d):
    for index in range(2, len(d)):
        name,value = d[index].strip().split('=')
        value=value.strip(' (')
        value=value.strip(' )')
        name = name.strip()
        value = value.replace(' ','')
        direction[name.strip()]=value.split(',')
    return direction

def mapit(header,direction,current_direction,s):
        step = s
        for i in enumerate(header):
            step +=1
            if (i[1] == 'L'):
                current_direction=direction[current_direction][0]
            elif (i[1] == 'R'):
                current_direction=direction[current_direction][1]
            else:
                print('ERROR')
            if (current_direction == 'ZZZ'):
                #return True, step, current_direction
                return step, current_direction
        if (current_direction == 'ZZZ'):
            #return True,step, current_direction
            return step, current_direction

        else:
            return mapit(header,direction,current_direction,step)
            #return False,step, current_direction
        
        
with open("input.txt", "r") as file:
    data = file.readlines()
    header = data[0].strip('\n')
    direction = build_dict(data)
    direction_keys = list(direction.keys())

    current_direction = 'AAA'
    #current_direction = '11A'
    print (current_direction)
    #while (notFound == False):
    #    notFound, step, current_direction = mapit(header,direction,current_direction,step)
    #notFound, step, current_direction = mapit(header,direction,current_direction,step)
    #print (notFound, step, current_direction)

    step, current_direction = mapit(header,direction,current_direction,step)
    print (step, current_direction)
    
        



