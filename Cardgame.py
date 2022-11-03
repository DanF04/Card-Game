import random

Deckplayer=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Deckpc=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
deck2=(Deckplayer, Deckpc)
handPlayer= (str(Deckplayer[-1]) + str(Deckplayer[-2]))
handNPC= (str(Deckpc[-1]) + str(Deckpc[-2]))

def translateDeck (deck):
    translateDeck = []
    for card in deck:
        if card == 11:
            translateDeck.append("J")
        elif card == 12:
            translateDeck.append("Q")
        elif card == 13:
            translateDeck.append("K")
        elif card == 14:
            translateDeck.append("A")
        else:
            translateDeck.append(str(card))
    return translateDeck  

def shuffle(deck):
    random.shuffle(deck)

def fish (deck):
    return[ deck[-1], deck[-2] ]

def sum(deck):
    sumTotal = 0
    for card in deck:
        sumTotal += card
    return sumTotal

def discard (deck):
    n=input("Do you want to discard your cards? ")
    if (n == "yes 1" or n == "yes 1 card"):
        def fish2 (deck):
            return[ deck[-2], deck[-3] ]
        print("Player cards " + str(fish2(translateDeck(Deckplayer))))
        print("PC cards " + str(fish(translateDeck(Deckpc))))   
    elif (n == "yes 2" or n == "yes 2 cards"):
        def fish3 (deck):
            return[ deck[-3], deck[-4] ]
        print("Player cards " + str(fish3(translateDeck(Deckplayer))))
        print("PC cards " + str(fish(translateDeck(Deckpc))))
    elif (n == "no" or n == "0"):
        def fish4 (deck):
            return[ deck[-1], deck[-2] ]
        print("Player cards " + str(fish4(translateDeck(Deckplayer))))
        print("PC cards " + str(fish(translateDeck(Deckpc))))
    
        
        

def compare (handPlayer, handNPC):
    sumPlayer = sum(handPlayer)
    sumNPC = sum(handNPC)

    if (sumPlayer < sumNPC):
        print("PC wins! Because it has a bigger sum of cards compared to the player.")
    elif (sumPlayer > sumNPC):
        print("Player wins! Because it has a bigger sum of cards compared to PC.")
    elif (sumPlayer == sumNPC):
        print("DRAWWWWWWWWWWW!!!!!!!!!!!")

while True:
    print("Player deck " + str(translateDeck(Deckplayer)))
    print("PC deck " + str(translateDeck(Deckplayer)))
    print("Shuffling decks...")
    shuffle(Deckplayer)
    shuffle(Deckpc)
    print("Player shuffled deck " + str(translateDeck(Deckplayer)))
    print("PC shuffled deck " + str(translateDeck(Deckpc)))
    print("Fishing two cards...")
    print("Player cards " + str(fish(translateDeck(Deckplayer))))
    print("PC cards " + str(fish(translateDeck(Deckpc))))
    discard(str(translateDeck(Deckplayer)))
    compare(fish(Deckplayer), fish(Deckpc))
    break

    

    
