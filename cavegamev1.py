#Name: Graydon Armstrong
#Date: May 22nd, 2013
#Source File: cavegamev1.py

#import time

#location on the decision tree
location = -1

#The main method controls the game loop
def main():
    playAgain = 'y'
    while playAgain == 'y':
        displayIntro()
        location = -1;
        direction = chooseDirection()
        
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

#the checkLocation method changes your location on the decision tree
def checkLocation(chosenDirection):
    if location == -1:
        location = chosenDirection
    else:
        location = location*2 + chosenDirection
        
    
    
    
if __name__ == "__main__": main()