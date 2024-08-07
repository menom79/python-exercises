#Assignment 8.1
def create_deck_of_cards():
    suits = ["♠","♣","♥","♦"]
    labels = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    for i in range(13):
        for j in range(4):
            deck.append(suits[j]+labels[i])
    return deck

print(create_deck_of_cards())

#Assignment 8.2
import random
def shuffle_deck(deck):
    for i in range(len(deck)):
        swap = random.randrange(0,len(deck)-1)
        temp_storage = deck[swap]
        deck[swap] = deck[i]
        deck[i] = temp_storage
    return deck

print(shuffle_deck(create_deck_of_cards()))

#Assignment 8.3
storage = {
    "APF-862": "Ford",
    "UVA-116": "Hyundai",
    "CVO-484": "Dodge",
    "CAR-537": "Toyota",
    "UDI-897": "Chevrolet",
    "JLM-835": "Audi",
    "JGM-687": "Kia",
    "EFV-371": "Volvo",
    "AHE-997": "Porsche",

}
print(dict(sorted(storage.items(), key=lambda item: item[1])))
print(dict(sorted(storage.items())))
