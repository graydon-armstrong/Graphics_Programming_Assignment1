# Name: Graydon Armstrong
# Date: May 23nd, 2013
# Source File: assignment1v2.py

# import time

# The main method controls the game loop
def main():
    playAgain = 'y'
    while playAgain == 'y':
        displayIntro()
        location = 0;
        while location != -1:
            direction = chooseDirection()
            location = changeLocation(direction,location)
            location = checkLocation(location);
        
        print("Do you want to play again? (y or n)")
        playAgain = raw_input()
    
# The intro method displays intro story messages
def displayIntro():
    print("You wake up to klaxons wailing on the bridge of your starship.")
    print("You look around and see that the rest of your crew have not survived the impact.")
    print("The ships computer announces that the boarding party from the unknown vessel is now onboard")
    print("You will need to escape the ship the get to safety.")
    print("It is time to leave the bridge. The Medbay is to the left and Engineering is to the right.")
    
# The chooseDirection method lets you choose if you are going left or right
# from your current location
def chooseDirection():
    direction = ''
    while direction != '1' and direction != '2':
        print("Will you go left or right? (1 or 2)")
        direction = raw_input()
    return direction

# the changeLocation method changes your location on the decision tree
def changeLocation(chosenDirection,location):
    location = int(location) * 2 + int(chosenDirection)
    return location

# the checkLocation method displays the story for your new location
def checkLocation(location):
    if location == 1:
        print("A")
        print("You leave the bridge and head left down the hallway to the Medbay.")
        print("You hear scurrying in the distance and quickly duck inside the Medbay.")
        print("The room is dark, the syringes and surgical tools look manacing.")
        print("You sneak into the room and out of the corner of your eye see an alien with its back to you.")
        print("The alien is feasting on one of the comotose patients, and you slowly back away distgusted.")
        print("You try to escape without making a sound but knock a bedpan with your foot because of the darkness.")
        print("You decide to run as you hear the alien turn from its meal.")
        print("The closest compartments to hide are the barracks on the left and the gym on the right.")
    elif location == 2:
        print("B")
        print("You leave the bridge and head right down the hallway to engineering.")
        print("As you walk into engineering the lights flicker and you can hear the engine whining.")
        print("The ship has taken alot of damage from the alien boarding party.")
        print("You hear feral screams of the alien language come from the hallway behind you and hurry your pace.")
        print("You reach a juncture where you can head towards the Cargo Bay on the left or towards the Escape Pods on your right.")
    elif location == 3:
        print("AA")
        print("You reach the barracks and close the door behind you.")
        print("Just as you lock the door the alien that was chasing you slams into and dents the door.")
        print("With fear on your face you turn to view the barracks and are releived to see 10 marines sitting on their bunks.")
        print("You see weapons to the left side of the room and a large closet to hide in on the right.")
    elif location == 4:
        print("AB")
    elif location == 5:
        print("BA")
    elif location == 6:
        print("BB")
    elif location == 7:
        print("Lose AAA")
        print("You choose to rally the marines on their bunks to grab weapons from the locker on the left.")
        print("You and the marines setup with your weapons aimed at the door.")
        print("You hear more aliens arrive outside the door and start trying to break in.")
        print("The door crashes open and a mass of aliens rush through the opening.")
        print("You and the marines start to open fire on the aliens.")
        print("A few aliens drop from your fire but they have weaposn themselves and start to return fire.")
        print("You are quickly overwhelmed by the number of aliens and are massacred in minutes.")
    elif location == 8:
        print("Lose AAB")
    elif location == 9:
        print("Lose ABA")
    elif location == 10:
        print("Lose ABB")
    elif location == 11:
        print("Win BAA")
    elif location == 12:
        print("Lose BAB")
    elif location == 13:
        print("Lose BBA")
    elif location == 14:
        print("Lose BBB")
    
    # if the location is 7 or greater the player has reached one of the 8 outcomes
    if location >= 7:
        return -1
    else:
        return location
        
if __name__ == "__main__": main()
