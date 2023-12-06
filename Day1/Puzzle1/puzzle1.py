total = 0


with open("input4.txt", "r") as file:
    data = file.readlines()
    total = 0
 
    for line in data:
        current_line=line.strip('\n')
       # f = re.search(r"\d", current_line)
      #  print("Digit found at position", f.start())
       # print("First value = ",current_line[f.start()])
        print ('______')
        print ('current_line:',current_line)
        num = 0
        found_first = 0
        first = -1
        last = 0
        for c in current_line:
            print ('c:',c)
            if c.isdigit():
                if first < 0:
                    print ('c1:',c)
                    print ('first:', first)
                    first = int(c) * 10
                    last = int(c)
                else:
                    last = int(c)
                print ('first:', first)
                print ('last:', last)
                num=first+last
                print ('num:', num)
        print ('______')
        total = total + num
        print ('total:', total)
        
#print("Extracted numbers from the list : " + num) 
        #if re.search(p, current_line) is not None:
        #    for catch in re.finditer(p, current_line):
        #        print(catch[0]) # catch is a match object

 #       first=first_digit()
 #       last=last_digit()
 #       num=first*10 + last
 #       total=total+num

 #   print total
