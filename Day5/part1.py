import re
seeds = []

def convert_number(s, d, r):
    source = int(s)
    destination = int(d)
    ranges = r
    #print ('s:',source,'d:',destination,'r:',ranges)

    for ds, ss, l in ranges:
        dest_start = int(ds)
        source_start = int(ss)
        length = int(l)
        print ('ds:',dest_start,'ss:',source_start,'l:',length)
        print ('ss:',source_start,' s:', source,' s_l', source_start + length)
        if source_start <= source < (source_start + length):
            print ("YES:",dest_start + (source - source_start))
            return dest_start + (source - source_start)
    print ("NO:",destination)
    return destination  # If no mapping is found, return the original source

def find_lowest_location(seeds, maps):
    current_numbers = seeds
    print (seeds,maps)
    for map_name, ranges in maps.items():  
        print (map_name) 
        print('rng:',ranges)    
        current_numbers = [convert_number(num, num, ranges) for num in current_numbers]
        print ('cn:',current_numbers)
    #return
    return min(current_numbers)

maps = {}
current_map = []
j=0
with open("./input.txt", "r") as file:
    data = file.readlines()
    header = data[0].strip('\n')
    s = header.split(':')[1].split()
    for i in range(1, len(s)):
                seeds.append(int(s[i]))
    print (seeds)
    nextline =data[2].strip('\n')
    #print (seeds)
    map_name = nextline.split()[0]
    #print ('map:',map_name)    
    for index in range(3, len(data)):
        current_line=data[index].strip('\n')   
        #print ('current_line:',current_line)  
        if (current_line.endswith('map:')):
            maps[map_name] = current_map
            j=1
            current_map=[]
            #print (maps[map_name])
            continue
        if re.match(current_line,'^\n$'):
            index +=1
            nextline =data[index].strip('\n')
            map_name = nextline.split()[0]
            #print('MAPNAME:', map_name)
            j+=1
        else:
            current_value=data[index].strip('\n').split()
            current_map.append([int(i) for i in current_value])
            #maps[map_name]=data[index].strip('\n').split(':')


    for key, values in maps.items():
        for i in range(len(values)):
            print(key,'[',i,']:', values[i])    
    #print ('\nSEEDS:',seeds)


    result = find_lowest_location(seeds, maps)
    print("Lowest location number:", result)


