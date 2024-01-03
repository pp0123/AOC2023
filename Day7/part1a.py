from functools import cmp_to_key
from collections import Counter

card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J': 11, 'Q': 12, 'K': 13, 'A': 14}

from enum import Enum
 
class HandType(Enum):
    Five= 64
    Four = 32
    Full = 16
    Three = 8
    TwoPair = 4
    Pair = 2
    High = 0

def max_card_value(a,b):
   #print (a,b)
   for i in range(len(a)):
            card_a = a[i]
            card_b=b[i]
            if card_a == card_b:
                continue
            a_wins = (card_values[card_a]) > (card_values[card_b])
            return 1 if a_wins else -1

def get_hand_value(hand):
        counts = sorted(Counter(hand).values(), reverse=True)
        #print ("HC:",hand,counts)

        if counts[0] == 5:
            return HandType.Five.value
        if counts[0] == 4:
            return HandType.Four.value
        if counts[0] == 3 and counts[1] == 2:
            return HandType.Full.value
        if counts[0] == 3:
            return HandType.Three.value
        if counts[0] == 2 and counts[1] == 2:
            return HandType.TwoPair.value
        if counts[0] == 2:
            return HandType.Pair.value
        return HandType.High.value  

def max_hand(a,b):
    cards_a = a[0]
    cards_b = b[0]
    if (get_hand_value(cards_a)>get_hand_value(cards_b)):
        return 1
    elif (get_hand_value(cards_a)<get_hand_value(cards_b)):
        return -1
    else:
        return (max_card_value(cards_a,cards_b))
    

with open("input.txt", "r") as file:
    data = file.readlines()
    i = 0
    all_hands = []
    ttl = 0
    for line in data:
        card_entry = []
        current_line=str(line.strip("\n"))
        hand = current_line.split()
        all_hands.append(hand)

    #print ("AH:",all_hands)
    all_hands.sort(key=cmp_to_key(max_hand))
    #print ("AH:",all_hands)
    for i in range(len(all_hands)):
        ttl += (i+1)*int(all_hands[i][1])
    print ("TTL:", ttl)
