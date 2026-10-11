#Variables and other jazz
import time
import sys
windowstate = "closed"
light = "off"
escape = False
doorlock = "locked"
playerinventory = []
#Definitions
def window():
    global windowstate
    if windowstate == "closed":
        print ("It is closed.")
        print ("Type A to open it, Type B to leave")
        choice = input()
        if choice == "A":
            print("You open the window. A gust of wind rushes in. It smells better now.")
            windowstate = "open"
            return windowstate
        elif choice == "B":
            print("You leave the window")
        else:
            print("You did not type A or B. Make sure to do it in capitals.")
    elif windowstate == "open":
        print("An open window. It's dark and you cannot fit through.")
def lightswitch():
    global light
    if light == "off":
        print("A light switch. Type A to turn on, Type B to leave")
        choice = input()
        if choice == "A" and windowstate == "closed":
            print("You slowly reach towards the switch.")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("*click*")
            time.sleep(0.5)
            print("""KABOOM
            A blinding explosion of light and heat engulfs the room and you die
            instantly. Gas.""")
            print("The game will now be aborted. Please restart the program to try again")
            sys.exit(0)
        elif choice == "A" and windowstate == "open":
            print("You slowly reach towards the switch.")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(1)
            print("*click*")
            time.sleep(0.5)
            print("A flash of light engulfs the room and you can see clearly now.")
            light = "on"
            return light
        elif choice == "B":
            print ("You leave the switch")
        else:
            print("You did not type A or B. Make sure to do it in capitals.")
    elif light == "on":
        print("It is switched on. You don't see a reason to turn it off.")
def poster(playerinventory):
    global light
    if light =="on":
        print("It is of a band you do not know. You see a crack snaking from out behind the poster")
        print("Take poster down? Type A for yes, type B for no.")
        choice = input()
        if choice == "A":
            print("You rip the poster down")
            time.sleep(2)
            print("A hole. It is small, barely larger than your fist, but it contains a key")
            print("This could be useful. You take the key.")
            playerinventory.append("key")
            time.sleep(3)
            print("===KEY ADDED TO INVENTORY===")
            time.sleep(2)
            return playerinventory
        elif choice == "B":
            print("You leave the poster. The band probably sucks anyway.")
        else:
            print("You did not type A or B. Make sure to do it in capitals.")     
    elif light == "off":
        print("It is too dark to make anything out on the poster. Probably useless.")
def keyuse(playerinventory):
    global doorlock
    print("The key is small and golden.")
    print("""Please type what you would like to use it on, or type nevermind if you want
    to put it back in your inventory (lowercase only)""")
    choice = input()
    if choice == "door":
        print ("""There is a lock. You inset the key and twist it.""")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print("*click*")
        time.sleep(0.5) 
        print("The door is now unlocked. Your key was used up.")
        doorlock = "unlocked"
        playerinventory.remove("key")
        return doorlock , playerinventory
    elif choice == "nevermind":
        print("Probably useless anyways")
    else:
        print("You cannot use your key on the", choice)    

def door():
    global doorlock
    global escape
    if doorlock == "locked":
        print ("""It is a door. Quite tall, and has a lock.""")
    elif doorlock == "unlocked":
        print ("""The door is unlocked. Open it? Type A for yes, type B for no.""")
        choice = input()
        if choice == "A":
            print("You push open the door...")
            time.sleep(3)
            escape = True
            return escape
        elif choice == "B":
            print("You step away from the door")
        else:
            print("You did not type A or B. Make sure to do it in capitals.")
        
        



#Main loop
print ("This is the prison escape room")
time.sleep(3)
print("""You wake up in a room and its dark. It smells like fish, and the floor is
hard. You can't see well but you notice a rectangular outline in the corner of the room.
A door. Before approaching it you catch a glimpse of a poster on the wall. You ignore it.
Adjacent to it is a small window, but it seems dark outside. Last you see a white box
next to the door. It must be a lightswitch.""")
time.sleep(1)
while escape == False:
    print("Choose something to inspect around you or in your inventory (Please type in lowercase)")
    playerinspect = input()
    if playerinspect == "window":
        window()
    elif playerinspect == "lightswitch":
        lightswitch()
    elif playerinspect == "poster":
        poster(playerinventory)
    elif playerinspect == "key" and "key" in playerinventory:
        keyuse(playerinventory)
    elif playerinspect == "door":
        door()
    else:
        print("""Whatever you typed either is not an option or is spelled wrong.
        Make sure to type only the word. It may be phrased differently. Try to type it
        as it is spelled to you in game and make sure you type in lowercase.""")
time.sleep(2)
print("Congratulations! You escaped.")

    
