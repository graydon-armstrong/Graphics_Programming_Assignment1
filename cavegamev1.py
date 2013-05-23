#Name: Graydon Armstrong
#Date: May 22nd, 2013
#Source File: cavegamev1.py

#import time

def main():
    displayIntro()
    
def displayIntro():
    print("You wake up to klaxons wailing on the bridge of your starship.")
    print("You look around and see that the rest of your crew have not survived the impact.")
    print("The ships computer announces that the boarding party from the unknown vessel is now onboard")
    print("You will need to escape the ship the get to safety.")
    print("Will you go left or right from the bridge? ")
    
def chooseDirection():
    direction = ''
    while direction != '1' and direction != '2':
        print("Will you go left(1) or right(2)?")
        direction = raw_input()
    return direction
    
    
if __name__ == "__main__": main()