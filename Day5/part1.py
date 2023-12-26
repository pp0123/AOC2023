import re
from timedspinner import printspin
seeds = []

def print_map(s,m):
    print ('\n\n\n',s,len(m[s]))
    for i in range(len(m[s])):
        for num_times in range(m[s][i][2]):
            s_num = m[s][i][1] + num_times
            d_num = m[s][i][0] + num_times
            print ('seed:',s_num,':',d_num)

def get_mapping_value(k,m,v):
    for i in range(len(m[k])):
            for num_times in range(m[k][i][2]):
                s_num = m[k][i][1] + num_times
                d_num = m[k][i][0] + num_times
                printspin(0.10)
                #print ('seed:',s_num,':',d_num)
                if v == s_num:
                    #print ('Found:',s_num)
                    return d_num
    return v

def get_mapping_value2(k,m,v):
    d_num = v
    for i in range(len(m[k])):
            #print ('v:',v, m[k][i][0],m[k][i][0]+m[k][i][2],(v>= m[k][i][0]) and v < (m[k][i][0]+m[k][i][2]))
            if (v > m[k][i][1]) and v <= (m[k][i][1]+m[k][i][2]):
                #found it in the range, how toset d_num?
                d_num = m[k][i][0] + (v - m[k][i][1])
                #print('D:',d_num)
                return d_num
    return v

maps = {}
current_map = []
j=0
with open("./input.txt", "r") as file:
    data = file.readlines()
    header = data[0].strip('\n')
    s = strtointlist(header.split(':')[1].split())
    seeds = s
    print ('header:',header,'\ns:',seeds)
    map_name = ''

    for index in range(2, len(data)):
        current_line = data[index].strip()
        #print ("CL:",current_line)
        if (current_line.endswith('map:')):
            map_name = current_line.split()[0]
            #print ("first if", map_name)
            continue
        if re.match(current_line,'^\n$'):
            map_name = ''
            current_map = []
            continue
        else:
            current_value=data[index].strip('\n').split()
            current_map.append([int(i) for i in current_value])
            maps[map_name]=current_map
            #current_map = []
            #print('MAPNAME:', map_name,"current_map:",current_map)
        
    print ('Got Maps:',maps)
  
    all_locations=[]

    #print_map('seed-to-soil',maps)
    for i in range(len(seeds)):
        soil = get_mapping_value2('seed-to-soil',maps,seeds[i])
        #print ('s:', seeds[i],soil)
        fertilizer = get_mapping_value2('soil-to-fertilizer',maps,soil)
        water = get_mapping_value2('fertilizer-to-water',maps,fertilizer)
        light = get_mapping_value2('water-to-light',maps,water)
        temp = get_mapping_value2('light-to-temperature',maps,light)
        humid = get_mapping_value2('temperature-to-humidity',maps,temp)
        location = get_mapping_value2('humidity-to-location',maps,humid)
        all_locations.append(location)
        #print ('seed:',seeds[i],'location:',location)
        #print ('soil-to-fertilizer map:',seed_to_soil(seeds[i],maps),soil_to_fertilizer(seed_to_soil(seeds[i],maps),maps))
    print (min(all_locations))


  

