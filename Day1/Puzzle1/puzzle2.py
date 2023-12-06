total = 0
str_digits = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten"
      ]
def splitnonalpha(s):
   pos = 1
   while pos < len(s) and s[pos].isalpha():
      pos+=1
   return (s[:pos], s[pos:])

with open("input.txt", "r") as file:
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
        for word in splitnonalpha(current_line):
            print ('word:', word)
'''
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
        
'''