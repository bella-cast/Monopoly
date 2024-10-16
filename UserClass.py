'''This class holds all the attributes relating to the users of Monopoly,such
as their name and bank balance. It also has methods for cash transactions,
such as buying a property or paying another user rent.'''

class Player:

    def __init__(self, name, cash= 500):
        self.name = name
        self.cash = cash
        self.properties = []#Card names are stored here once they are bought

    isTurn = False #Needs to be true for turn to start
    inJail = False #If true, the player skips a turn
    
    #The land method in the Property class is called before the buy method.
    #It makes sure the card hasn't been bought before letting the user buy it
    def buy(self, card):
        if self.cash > card.buyprice:
            self.properties.append(card.name) #Add card name to property list
            self.cash -= card.buyprice
            print(f'You have just bought {card.name} for ${card.buyprice}')
            print(f'You have ${self.cash} in your bank account')
            card.isTaken = True #Card cannot be bought again
        else:
            print('You do not have enough money to buy this property.')

    #This method is used to pay the other user rent for landing on their property
    #The main code checks if the bank balance is less than zero after paying
    def pay(self, card, otherplayer):
        self.cash-= card.landprice
        otherplayer.cash += card.landprice
        print(f'Your bank balance is now ${self.cash}')
        
        

    
