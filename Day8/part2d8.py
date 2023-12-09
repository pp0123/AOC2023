from math import gcd
from functools import reduce

direction = {}
end_points=[]
start_points = {}
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

#stole this idea if lcm
def find_lcm(x, y):
    # Function for finding the least common multiple of two numbers using greatest common divisor function
    return (x * y) // gcd(x, y)

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
            if (current_direction[-1] == 'Z'):
                #return True, step, current_direction
                return step, current_direction
        if (current_direction[-1] == 'Z'):
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

    #setup up and run part 1
    current_direction = 'AAA'
    step, current_direction = mapit(header,direction,current_direction,step)
    print ("Part 1:",step, current_direction)

    #setup and run part 2
    starting_locations = [key for key in direction_keys if key[-1] == 'A']#all locations that end with 'A'
    for i in (starting_locations):
        current_direction=i
        step=0
        step, current_direction = mapit(header,direction,current_direction,step)
        end_points.append(step)

    #stole this lcm logic...way too smart for me
    lcm = reduce(find_lcm, end_points)
    print("PART 2:",lcm)
 
        



