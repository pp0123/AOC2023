
with open("input.txt", "r") as file:
    data = file.readlines()
    total = 0
 
    for line in data:
        current_line=line.strip('\n')
        print('before:',current_line)
        current_line = current_line.replace('one','o1e')
        current_line = current_line.replace('two','t2o')
        current_line = current_line.replace('three','t3e')
        current_line = current_line.replace('four','f4r')
        current_line = current_line.replace('five','f5e')
        current_line = current_line.replace('six','s6x')
        current_line = current_line.replace('seven','s7n')
        current_line = current_line.replace('eight','e8t')
        current_line = current_line.replace('nine','n9e')
        print (current_line)
