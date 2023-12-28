import random


def buildDeck():
    deck = []
    colours = ["Red", "Yellow", "Green", "Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip","Reverse"]
    wilds = ["Wild","Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour,value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])



    return deck

def shuffleDeck(deck):
    for cardPos in range (len(deck)):
        randPos = random.randint(0, 107)
        #swap value of the list with any random one in the deck
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]

    return deck




def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))

    return cardsDrawn

#shows the specific player's hand
def showHands(player, playerHand):
    print("Player {}".format(player+1))
    print("Your Hand")
    print("----------------------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y, card))
        y+=1
    print("----------------------")


#determines whether a player is able to play a card
def canPlay(colour, value, playerHand):
    for card in playerHand:
        if colour in card:
            return True
        elif "Wild" in card:
            return True
        elif value in card:
            return True
    return False




unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []

players = []
colours = ["Red", "Yellow", "Green", "Blue"]


numPlayers = int(input("How many players? "))
while numPlayers<2 or numPlayers>4:
    numpPlayer = int(input("Invalid. Please enter a number between 2-4. How many players? "))


for player in range(numPlayers):
    players.append(drawCards(5))

print(players)

playerTurn = 0 #based off the indexing of the players list
playDirection = 1 #1 means move to right, -1 means move to left
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"


while playing:
    showHands(playerTurn,players[playerTurn])
    print("Card on top of discard pile: {}".format(discards[-1])) #show the last element of list in the discards list
    if canPlay(currentColour,cardVal,players[playerTurn]):
        cardChossen = int(input("Which card you want to play? "))
        while not canPlay(currentColour, cardVal, [players[playerTurn][cardChossen-1]]): #if inputed card is not a valid card
            cardChossen = int(input("Not a valid card, Which card you want to play? "))

        print("You played {}".format(players[playerTurn][cardChossen-1]))
        discards.append(players[playerTurn].pop(cardChossen-1))

        #checks if player won
        if len(players[playerTurn]) == 0:
            playing = False
            winner = "Player {}".format(playerTurn+1)
        else:
            # checks special cards
            splitCard = discards[-1].split(" ", 1)
            currentColour = splitCard[0]

            if len(splitCard) == 1:
                cardVal = "Any"
            else:
                cardVal = splitCard[1]

            if currentColour == "Wild":
                for i in range(len(colours)):
                    print("{}) {}".format(i+1, colours[i]))
                newColour = int(input("What colour would you like to choose? "))
                while newColour < 1 or newColour > 4:
                    newColour = int(input("Invalid option. What colour would you like to choose? "))
                currentColour = colours[newColour - 1]

            if cardVal == "Reverse":
                playDirection = -1 * playDirection

            elif cardVal == "Skip":
                playerTurn += playDirection

                if playerTurn >= numPlayers:
                    playerTurn = 0
                elif playerTurn < 0:
                    playerTurn = numPlayers - 1

            elif cardVal == "Draw Two":
                #identifies which player is drawing the card
                playerDraw = playerTurn+playDirection
                if playerDraw  == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers-1
                players[playerDraw].extend(drawCards(2))

            elif cardVal == "Draw Four":
                playerDraw = playerTurn+playDirection
                if playerDraw == numPlayers:
                    playerDraw = 0
                elif playerDraw < 0:
                    playerDraw = numPlayers - 1
                players[playerDraw].extend(drawCards(4))


    else:
        print("You can't play. You have to draw a card!")
        players[playerTurn].extend(drawCards(1))


    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1

print("Game Over!")
print(winner+" is the winner!")
