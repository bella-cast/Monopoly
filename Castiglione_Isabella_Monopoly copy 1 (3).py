'''This is the main code of the Monopoly game. It imports from two other classes, UserClass and Cardclass, as well as a graphics module, which displays the
game board, and the random module, which is used to roll the dices. In this code, the board, player chips and cards are created, as well as the main loop
which does the turn system (PlayerA's turn...PlayerB's turn...etc.)'''

from graphics import *
from CardClass import *
from UserClass import *
from random import *

#These blocks of code create the board by dividing the graph into rectangles and colouring them in.
win = GraphWin() #This specific line instantiates the blank graph


rect1 = Rectangle(Point(0,0), Point(50,50)) #The graph works as a coordinate system, so the two points are the coordinates of opposing corners in the rectangle
rect2 = Rectangle(Point(50, 0), Point(100, 50))
rect3 = Rectangle(Point(100, 0), Point(150, 50))
rect4 = Rectangle(Point(150, 0), Point(200, 50))
rect5 = Rectangle(Point(0,50), Point(50, 100))
rect6 = Rectangle(Point(0,100), Point(50, 150))
rect7 = Rectangle(Point(0,150), Point(50, 200))
rect8 = Rectangle(Point(50,150), Point(100, 200))
rect9 = Rectangle(Point(100,150), Point(150, 200))
rect10 = Rectangle(Point(150,150), Point(200, 200))
rect11 = Rectangle(Point(150,50), Point(200, 100))
rect12 = Rectangle(Point(150,100), Point(200, 150))


rect1.setFill('silver')
rect2.setFill('light blue')
rect3.setFill('light blue')
rect4.setFill('silver')
rect5.setFill('violet')
rect6.setFill('light green')
rect7.setFill('silver')
rect8.setFill('light green')
rect9.setFill('light pink')
rect10.setFill('silver')
rect11.setFill('light yellow')
rect12.setFill('light pink')

def Board(): #This function calls the rectangles created above to appear on the graph by using the graph as an argument in the draw function. (.draw(win))
    rect1.draw(win)
    rect2.draw(win)
    rect3.draw(win)
    rect4.draw(win)
    rect5.draw(win)
    rect6.draw(win)
    rect7.draw(win)
    rect8.draw(win)
    rect9.draw(win)
    rect10.draw(win)
    rect11.draw(win)
    rect12.draw(win)

#The Property cards are instantiated, with the arguments representing the card name, the price to buy the card and the landing rent price
Go = Property('GO!', 0, 0)
ArcticAveA = Property('Arctic Avenue A', 40, 15)
ArcticAveB = Property('Arctic Avenue B', 40, 15)
SkyAve = Property('Skyway Avenue', 300, 80)
MarvinGB = Property('Marvin Gardens B', 200, 50)
Grey = Property('Chance Card!', 0, 0)
MarvinGA = Property('Marvin Gardens A', 200, 45)
PennAveB = Property('Pensylvannia Avenue B', 100, 30)
OceanAve = Property('Ocean Avenue', 70, 25)
PennAveA = Property('Pennsylvannia Avenue A', 100, 30)

#These cards cannot be bought by a player, so they are set as taken.
Go.isTaken = True
Grey.isTaken = True

def Landed(x, y): #The users coordinates are inputted as arguments
    if 0<y<50: #This function compares the coordinates to the coordinates of the rectangles to determine where on the graph the user is.
      if 0<x<50:
          return Go #Once a match is found, the name of the card the user landed on is returned.
      elif 50<x<100:
          return ArcticAveA
      elif 100<x<150: 
          return ArcticAveB
      else:
          return Grey
    elif 0<x<50:
      if 50<y<100:
          return SkyAve
      elif 100<y<150:
          return MarvinGB
      else: 
          return Grey
    elif 150< y< 200:
      if 50<x<100:
          return MarvinGA
      elif 100<x<150 :   
          return PennAveB
      else:
          return Grey
    else:
      if 50<y<100: 
          return OceanAve 
      else:
          return PennAveA
        
#These two blocks of code create the player chips on the board
Player1 = Circle(Point(25,15), 5)#The arguments in Point()are the starting x and y coordinates of the chip
Player1.setOutline('black')
Player1.setFill('white')

Player2 = Circle(Point(25,35), 5)
Player2.setOutline('black')
Player2.setFill('black')


def Move( roll, x, y, lastx, lasty,player,counter=0):
    #This function uses the users present and past coordinates, plus their roll from the dice to determine
    #their next move (either left, down, right or up)
    if x == 25 and (y == 15 or y == 35) and counter!= 0:#those x and y values are the coordinates for both players when the chip is on Go
        lastx = x #the counter can't be one because then the user will get money for the starting position on Go.
        lasty = y
        player.cash += 50
        print('You passed GO! Collect $50') #Check if the user passes Go and give them $50
        print(f'Your balance is now ${player.cash}')
    if counter != roll: #when counter does not equal roll, you still have to move
        #using coordinates of the graph to determine the next move
        #since the function always goes left and down first, save lastx and lasty to prevent it from moving back onto itself
        if x + 50 < 200 and x+50!= lastx: #left
            lastx=x
            x+=50
            return Move( roll, x, y, lastx, lasty,player, counter+1) #enter new values into the function until the counter equals the roll (reaches destination)
                
        elif y + 50 < 200 and y+50 != lasty: #down
            lasty=y
            y+=50
            return Move( roll, x, y ,lastx, lasty,player, counter+1)
        
        elif x - 50 > 0: #right
            lastx=x
            x-= 50
            return Move( roll, x, y, lastx, lasty,player, counter+1)
        
        else: #up
            lasty=y
            y-=50
            return Move( roll, x, y, lastx, lasty, player,counter +1)
    else:
        return x,y,lastx, lasty #return these values so they can be updated in the code





#The user's properties are saved in a list, but only the name (card.name) is saved so that it can easily be outputted to the screen.
#This dictionary compares the name of the card to the card it comes from so that the card.addHouse method can be used when building
BuildingList = { 
    'GO!' : Go,
    'Arctic Avenue A' : ArcticAveA,
    'Arctic Avenue B' : ArcticAveB,
    'Skyway Avenue' : SkyAve,
    'Marvin Gardens B' : MarvinGB,
    'Marvin Gardens A' : MarvinGA,
    'Pensylvannia Avenue B' : PennAveB,
    'Ocean Avenue' : OceanAve,
    'Pennsylvannia Avenue A' : PennAveA
    }
#This function displays a house on the board once it is built depending on where the property is and how many houses are already there.    
def BuildaHouse(name): #the property card is inputted as an argument
    if name == ArcticAveA:
        if ArcticAveA.Houses == 1: 
            house = Rectangle(Point(50,40),Point(62,50))#Each house has a width of 10 and a length of 12, with a space (1) between each house
            house.setFill('red')                        #The houses are instantiated based on the coordinates of the property on the graph
            house.draw(win)
        elif ArcticAveA.Houses ==2:
            house = Rectangle(Point(63,40),Point(75,50))
            house.setFill('red')
            house.draw(win)
        elif ArcticAveA.Houses ==3:
            house = Rectangle(Point(76,40),Point(88,50))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(89,40),Point(100,50))
            house.setFill('red')
            house.draw(win)
    elif name == ArcticAveB:
        if ArcticAveB.Houses == 1:
            house = Rectangle(Point(100,40),Point(112,50))
            house.setFill('red')
            house.draw(win)
        elif ArcticAveB.Houses ==2:
            house = Rectangle(Point(113,40),Point(125,50))
            house.setFill('red')
            house.draw(win)
        elif ArcticAveB.Houses ==3:
            house = Rectangle(Point(126,40),Point(138,50))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(139,40),Point(150,50))
            house.setFill('red')
            house.draw(win)
    elif name == SkyAve:
        if SkyAve.Houses == 1:
            house = Rectangle(Point(40,50),Point(50,62))
            house.setFill('red')
            house.draw(win)
        elif SkyAve.Houses ==2:
            house = Rectangle(Point(40,63),Point(50,75))
            house.setFill('red')
            house.draw(win)
        elif SkyAve.Houses ==3:
            house = Rectangle(Point(40,76),Point(50,88))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(40,89),Point(50,100))
            house.setFill('red')
            house.draw(win)
    elif name ==MarvinGB:
        if MarvinGB.Houses == 1:
            house = Rectangle(Point(40,100),Point(50,112))
            house.setFill('red')
            house.draw(win)
        elif MarvinGB.Houses ==2:
            house = Rectangle(Point(40,113),Point(50,125))
            house.setFill('red')
            house.draw(win)
        elif MarvinGB.Houses ==3:
            house = Rectangle(Point(40,126),Point(50,138))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(40,139),Point(50,150))
            house.setFill('red')
            house.draw(win)
    elif name ==MarvinGA:
        if MarvinGA.Houses == 1:
            house = Rectangle(Point(50,150),Point(62,160))
            house.setFill('red')
            house.draw(win)
        elif MarvinGA.Houses ==2:
            house = Rectangle(Point(63,150),Point(75,160))
            house.setFill('red')
            house.draw(win)
        elif MarvinGA.Houses ==3:
            house = Rectangle(Point(76,150),Point(88,160))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(89,150),Point(100,160))
            house.setFill('red')
            house.draw(win)
    elif name == PennAveB:
        if PennAveB.Houses == 1:
            house = Rectangle(Point(100,150),Point(112,160))
            house.setFill('red')
            house.draw(win)
        elif PennAveB.Houses ==2:
            house = Rectangle(Point(113,150),Point(125,160))
            house.setFill('red')
            house.draw(win)
        elif PennAveB.Houses ==3:
            house = Rectangle(Point(126,150),Point(138,160))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(139,150),Point(150,160))
            house.setFill('red')
            house.draw(win)
    elif name == OceanAve:
        if OceanAve.Houses == 1:
            house = Rectangle(Point(150,50),Point(160,62))
            house.setFill('red')
            house.draw(win)
        elif OceanAve.Houses ==2:
            house = Rectangle(Point(150,63),Point(160,75))
            house.setFill('red')
            house.draw(win)
        elif OceanAve.Houses ==3:
            house = Rectangle(Point(150,76),Point(160,88))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(150,89),Point(160,100))
            house.setFill('red')
            house.draw(win)
    else:
        if PennAveA.Houses == 1:
            house = Rectangle(Point(150,100),Point(160,112))
            house.setFill('red')
            house.draw(win)
        elif PennAveA.Houses ==2:
            house = Rectangle(Point(150,113),Point(160,125))
            house.setFill('red')
            house.draw(win)
        elif PennAveA.Houses ==3:
            house = Rectangle(Point(150,126),Point(160,138))
            house.setFill('red')
            house.draw(win)
        else:
            house = Rectangle(Point(150,139),Point(160,150))
            house.setFill('red')
            house.draw(win)

if __name__ == '__main__': #main script
    Board()#displays board game
    Player1.draw(win)#displays player chips on the board
    Player2.draw(win)
    #all x and y variables that have a 1 after correspond to player one (same thing with 2 for player two)
    x1 = 25 
    y1 = 15
    lastx1 = 25 #use last x and y to track movements so that the chip doesn't go back onto itself. 
    lasty1 = 15
    x2 = 25
    y2 = 35
    lastx2 = 25
    lasty2 = 35
    

    print('Welcome to Monopoly!')
    a = input('Player One, what is your name? \n')#Get names of players
    b = input('Player Two, what is your name? \n')

    PlayerA = Player(a)#names are used when instantiating the players in userclass
    PlayerB = Player(b)

    print(f'Okay {PlayerA.name}, you\'re going first as the WHITE chip.')
    print('Each turn you will have the option to roll, review and build.\nYou don\'t need both properties of the same colour to build.\nThe grey tiles, other than Go, are all Chance Cards.\nYou start with $500')
    PlayerA.isTurn = True #Both user.isTurn start off as False
        
   
    
    while True:
        if PlayerA.isTurn:
            print(f'\n{PlayerA.name}, its your turn')
            rollcount = -1 #Used to count the amount of rolls (for doubles) and if a certain number is reached, the user goes to jail
            while PlayerA.isTurn:
                if PlayerA.inJail : #check if the user is in jail before letting them roll (jail time = 1 skipped turn)
                    print('You are in jail. Skip this turn.')
                    PlayerA.inJail = False
                    PlayerB.isTurn = True #True for player B so that their turn starts
                    PlayerA.isTurn = False
                    continue #Continue or else the turn keeps going
                else:
                    #display all options 
                    print('\n  Enter \'r\' to roll the dice.\n  Enter \'f\' to see your finances/properties.\n  Enter \'b\' to build.\n  Enter \'q\' to quit.')
                    move = input()
                    if move.lower() == 'r': # rolling the dice 1 and 2
                        r1 = randint(1,6)
                        r2 = randint(1,6)
                        if r1 == r2: #doubles
                            print(f'You rolled a {r1} and a {r2}. Doubles! You\'ll get to go again!')
                            PlayerA.isTurn = True #Player gets to go again
                            rollcount += 1 
                            if rollcount ==2:
                                print('You got doubles three times! You are in Jail. Skip one turn.')
                                PlayerA.isTurn = False
                                PlayerA.inJail = True #If the user rolls doubles three times (rollcount == 2 ), they go to Jail
                                PlayerB.isTurn = True
                                continue #end turn here       
        
                        else:
                            print(f'You rolled a {r1} and a {r2}.')
                            PlayerA.isTurn = False #their turn won't repeat (no doubles)
                        new= Move(r1+r2, x1, y1, lastx1, lasty1,PlayerA) #save new as a variable so that the returned values can be saved as x1 or x2 (depending on user)
                        x1= new[0]
                        y1 = new[1]
                        lastx1 = new[2]
                        lasty1 = new[3]
                        Player1.undraw() #delete old player chip
                        Player1 = Circle(Point(x1,y1), 5) #redraw at new coordinates
                        Player1.setFill('white')
                        Player1.draw(win)
                        card=Landed(x1, y1) #use coordinates to find which card was landed on 
                        card.land(PlayerA, PlayerB) #use the card and the land method to see if the property can be bought, or if rent needs to be paid
                        if PlayerA.cash <0: #if the user pays rent but has no money left
                            print(f'{PlayerA.name}, you lose! You are bankrupt!')
                            print(f'Congrats on winning, {PlayerB.name}!')
                            PlayerA.isTurn = False #both turns are false, goes to 'else' in the loop and breaks
                            PlayerB.isTurn = False
                            continue #continue so that it stops here
                        if  not PlayerA.isTurn: #if there weren't doubles (it gets set as false above)
                            PlayerB.isTurn = True #Player B's turn
            
                    elif move.lower() == 'f': #review bank balance and properties
                        print(f'You have ${PlayerA.cash} and own these properties:{PlayerA.properties}')
                
                    elif move.lower() == 'b':#building houses
                        if len(PlayerA.properties)> 0: #if the user owns a property
                            question = input('Do you want to build a house for $50? Enter y/n:\n')
                            if question.lower() == 'y':
                                print(f'Select the index (start counting from 1) of the property you want to build on: {PlayerA.properties}')
                                index = int(input())
                                if index > len(PlayerA.properties)or index == 0: #make sure integer is valid for the list so the game doesn't crash
                                    print('Pick an index in the list')
                                    continue #brings back to option list (r, f, b, q) 
                                BuildingList[PlayerA.properties[index -1]].addHouse(PlayerA)#find the property in the list, compare it to the dictionary
                                #with the card name, use the addHouse method to build
                                BuildaHouse(BuildingList[PlayerA.properties[index -1]]) #call this function to display the house on the board
                            else:
                                print('Okay. You can build another time.')
                        else:

                            print('You need to own a property before you can build.')
                            
                    elif move.lower() == 'q': #quit
                        PlayerA.isTurn = False #set both turns to False
                        PlayerB.isTurn = False
                    
                    else:
                        print('Please pick an option.')
        elif PlayerB.isTurn : #exact same as above but varaiables relate to PlayerB
            print(f'\n{PlayerB.name}, its your turn')
            rollcount = -1
            while PlayerB.isTurn:
                if PlayerB.inJail :
                    print('You are in Jail. Skip this turn')
                    PlayerB.inJail = False
                    PlayerA.isTurn = True
                    PlayerB.isTurn = False
                    continue
                else:
                    print('\n  Enter \'r\' to roll the dice.\n  Enter \'f\' to see your finances/properties.\n  Enter \'b\' to build.\n  Enter \'q\' to quit.')
                    move = input()
                    if move.lower() == 'r':
                        r1 = randint(1,6)
                        r2 = randint(1,6)
                        if r1 == r2:
                            print(f'You rolled a {r1} and a {r2}. Doubles! You\'ll get to go again!')
                            PlayerB.isTurn = True
                            rollcount += 1
                            if rollcount ==2:
                                print('You rolled doubles three times! You\'re in Jail, skip the next turn.')
                                PlayerB.isTurn = False
                                PlayerB.inJail = True
                                PlayerA.isTurn = True
                                continue
                                     
        
                        else:
                            print(f'You rolled a {r1} and a {r2}.')
                            PlayerB.isTurn = False
                        new= Move(r1+r2, x2, y2, lastx2, lasty2,PlayerB)
                        x2= new[0]
                        y2 = new[1]
                        lastx2 = new[2]
                        lasty2 = new[3]
                        Player2.undraw()
                        Player2 = Circle(Point(x2,y2), 5)
                        Player2.setFill('black')
                        Player2.draw(win)
                        card=Landed(x2, y2)
                        card.land(PlayerB, PlayerA)
                        if PlayerB.cash <0:
                            print(f'{PlayerB.name},you lose! You are bankrupt!')
                            print(f'Congrats on winning, {PlayerA.name}!')
                            PlayerA.isTurn = False
                            PlayerB.isTurn = False
                            continue
                        if  not PlayerB.isTurn:
                            PlayerA.isTurn = True
            
                    elif move.lower() == 'f':
                        print(f'You have ${PlayerB.cash} and own these properties:{PlayerB.properties}')
                
                    elif move.lower() == 'b':
                        if len(PlayerB.properties) > 0:
                            question = input('Do you want to build a house for $50? Enter y/n:\n')
                            if question.lower() == 'y':
                                print(f'Select the index (start counting from 1) of the property you want to build on: {PlayerB.properties}')
                                index = int(input())
                                if index > len(PlayerB.properties)or index == 0:
                                    print('Pick an index in the list')
                                    continue
                                BuildingList[PlayerB.properties[index -1]].addHouse(PlayerB)
                                BuildaHouse(BuildingList[PlayerB.properties[index -1]] )        
                            else:
                                print('You can build another time.')
                        else:
                            print('You need to own a property before you can build')
                            
                    elif move.lower() == 'q':
                        PlayerA.isTurn = False
                        PlayerB.isTurn = False
                    
                    else:
                        print('Please pick an option.')
        else: #this portion is called when both PlayerA.isTurn = False and PlayerB.isTurn = False. This happens at bankruptcy or when the user wants to quit.
            print('Thanks for playing!')
            break #end the game
                

















