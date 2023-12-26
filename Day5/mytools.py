def strtointlist(s): #make sure we are dealing with ints NOT strings in the list
    i=0
    for n in s:
        s[i]=int(n)
        i+=1
    return s
from collections import Counter

def duplicates(input):
    card_values = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'T':0,'J':0, 'Q':0, 'K':0, 'A':0}

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
    print ('TEST:',WC)
    
    # Finding no. of  occurrence of a character
    # and get the index of it.
    for letter, count in WC.items():
        if (count > 1):
            card_values[letter] +=1
            print(letter)
    return card_values
 
 

