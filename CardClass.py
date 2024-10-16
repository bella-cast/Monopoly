''' This class holds all the attributes relating to the properties in Monopoly.
Each property/card has a name, the initial buy price (buyprice), 
and the amount of rent the other player has to pay when landing in that space
(landprice).'''

from random import *

class Property:

    def __init__(self, name, buyprice, landprice):
        self.name = name
        self.buyprice = buyprice
        self.landprice = landprice
        
        

    isTaken = False #shows if the card is owned or not
    Houses = 0 #houses are added when the user decides to build

    def land(self,user, otherplayer): #This method is called when the user lands on a card
        print(f'You landed on {self.name}')
        if not self.isTaken: #if the card hasn't been bought yet, the user can buy it
            print(f'{self.name} costs ${self.buyprice}.\nRent costs ${self.landprice}\nWould you like to buy it?')
            buy = input('Enter y/n \n')
            if buy == 'y':
                user.buy(self)#transaction occurs in user class in the buy method
            else:
                print('You\'ll have to land here again to buy this property.')
        else:
            if self.name != 'GO!' and self.name != 'Chance Card!': #if card is owned but isn't Go or Chance (don't need to pay rent for those)
                if self.name in user.properties: #If user owns it, they don't pay rent
                    print('You own this property.')
                else: 
                    print(f'{self.name} is already owned. You must pay ${self.landprice}')
                    user.pay(self, otherplayer) #If owned by the other player, the user pays through the pay method in the user class
            else:
                if self.name == 'Chance Card!':#We don't need to check if the card is Go because nothing special happens there.
                    #Extra money from go is given in the move function in the main code
                    pick = randint(1,6) #pick a card
                    money = randint (1,200)#Value to be recieved/given, a changing value makes it less repetitive
                  #Cards either give money, take money or put the user in jail. 
                    if pick == 1:
                        print(f'Your card says:\n There was a fight in one of your properties.\n Pay ${money} in repairs')
                        user.cash -= money
                        print(f'Your new balance is ${user.cash}')
                    elif pick ==2:
                        print(f'Your card says:\n You run over {otherplayer.name}. Go to Jail.')
                        user.inJail = True
                        user.isTurn = False #End turn so that if they have doubles it doesn't repeat.
                    elif pick ==3:
                        print('Your card says:\n You successfully steal a street performers earnings.')
                        user.cash += money
                        print(f'Collect the ${money} he made. Your bank balance is now ${user.cash}')
                    elif pick == 4:
                        print(f'Your card says:\n {otherplayer.name} is suing you because you fold your socks instead of rolling them.')
                        user.cash -= money
                        otherplayer.cash += money
                        print(f'You must pay {otherplayer.name} ${money}. Your new balance is ${user.cash}')
                    elif pick == 5:
                        print(f'Your card says:\n Your pet ferret dies. Pay ${money} in funeral fees.')
                        user.cash -= money
                        print(f'Your new balance is ${user.cash}')
                    else:
                        print('Your card says:\n You get caught shoplifting. Go to Jail.')
                        user.inJail = True
                        user.isTurn = False


                        
                        
    def addHouse(self,user): #This method is called when the user chooses to build in the main script
        if user.cash > 50: #Houses cost 50$
            if self.Houses <4:#Maximum of four houses can be built
                self.Houses += 1
                self.landprice *= 1.5 #increase in rent when there are houses
                user.cash -= 50
                print(f'You have built a house on {self.name}.\nThere are now {self.Houses} houses on {self.name}')
                print(f'The new cost of rent on {self.name} is {self.landprice}')
            else:
                print('You have the maximum number of houses.')
                print(f'The value of your property is {self.landprice}')
        else:
            print('You do not have enough money to build a house')
            
        
                  

    
            
