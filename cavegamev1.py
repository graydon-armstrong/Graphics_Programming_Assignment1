#Name: Graydon Armstrong
#Date: May 22nd, 2013
#Source File: cavegamev1.py

#import time

#location on the decision tree
location = -1

#The main method controls the game loop
def main():
    playAgain = 'y'
    global location
    while playAgain == 'y':
        displayIntro()
        location = -1;
        while location != -2:
            direction = chooseDirection()
            changeLocation(direction)
            checkLocation();
        
        print("Do you want to play again? (y or n)")
        playAgain = raw_input()
    
#The intro method displays intro story messages
def displayIntro():
    print("You wake up to klaxons wailing on the bridge of your starship.")
    print("You look around and see that the rest of your crew have not survived the impact.")
    print("The ships computer announces that the boarding party from the unknown vessel is now onboard")
    print("You will need to escape the ship the get to safety.")
    print("It is time to leave the bridge.")
    
#The chooseDirection method lets you choose if you are going left or right
#from your current location
def chooseDirection():
    direction = ''
    while direction != '1' and direction != '2':
        print("Will you go left(1) or right(2)?")
        direction = raw_input()
    return direction

#the changeLocation method changes your location on the decision tree
def changeLocation(chosenDirection):
    global location
    if location == -1:
        location = int(chosenDirection)
    else:
        location = int(location)*2 + int(chosenDirection)
        print(location)

#the checkLocation method displays the story for your new location
def checkLocation():
    global location
    
    if location == 1:
        print("A")
    elif location == 2:
        print("B")
    elif location == 3:
        print("AA")
    elif location == 4:
        print("AB")
    elif location == 5:
        print("BA")
    elif location == 6:
        print("BB")
    elif location == 7:
        print("Lose AAA")
        location = -2
    elif location == 8:
        print("Lose AAB")
        location = -2
    elif location == 9:
        print("Lose ABA")
        location = -2
    elif location == 10:
        print("Lose ABB")
        location = -2
    elif location == 11:
        print("Win BAA")
        location = -2
    elif location == 12:
        print("Lose BAB")
        location = -2
    elif location == 13:
        print("Lose BBA")
        location = -2
    elif location == 14:
        print("Lose BBB")
        location = -2
        
if __name__ == "__main__": main()