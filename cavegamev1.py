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
    if location == 1:
        print("Test 1")
    elif location == 2:
        print("Test 2")
    elif location == 3:
        print("Test 3")
    elif location == 4:
        print("Test 4")
    elif location == 5:
        print("Test 5")
    elif location == 6:
        print("Test 6")
    elif location == 7:
        print("Test 7")
    elif location == 8:
        print("Test 8")
    elif location == 9:
        print("Test 9")
    elif location == 10:
        print("Test 10")
    elif location == 11:
        print("Test 11")
    elif location == 12:
        print("Test 12")
    elif location == 13:
        print("Test 13")
    elif location == 14:
        print("Test 14")
    elif location == 15:
        print("Test 15")
    elif location == 16:
        print("Test 16")
        
if __name__ == "__main__": main()