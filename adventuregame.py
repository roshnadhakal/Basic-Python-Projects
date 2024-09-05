#Narayanhiti Palace Adventure Game

def start_game():
    print("Welcome to the Narayanhiti Palace Haunted Adventure!")
    print("The Golden Gate is in front of you, its shadows whispering secrets.")

    choice = input("Do you dare to (A) Enter or (B) Flee? ").lower()
    if choice == "a":
        enter_palace()
    else:
        print("You flee, but the palace's whispers haunt you forever. Game over.")

def enter_palace():
    print("You step inside. It's dark and creepy. A chill runs down your spine.")
    choice = input("Do you (A) Explore the State Hall or (B) Proceed to the private quarters? ").lower()
    if choice == "a":
        print("In the State Hall, you see the ghostly king on his chair, eyes hollow and sad.")
        choice = input("Do you (A) Approach him or (B) Escape back? ").lower()
        if choice == "a":
            print("The king's ghost whispers, 'Find the truth behind the massacre...'")
            choice = input("Do you (A) Ask more or (B) Escape back? ").lower()
            if choice == "a":
                print("He vanishes, leaving only a whisper: 'Seek the crown prince's diary...'")
                find_diary()
            else:
                enter_palace()
        else:
            enter_palace()
    else:
        private_quarters()

def find_diary():
    print("You find the diary hidden in shadows, revealing a dark truth...")
    choice = input("Do you (A) Confront the truth or (B) Keep it secret? ").lower()
    if choice == "a":
        print("You reveal a sinister conspiracy of massacre, sealing your fate in the palace's dark history.")
        print("Congratulations, you have unrevealed the mystery... or have you? Game over.")
    else:
        print("You leave, burdened by the secret. The palace's curse follows you. Game over.")

def private_quarters():
    print("You enter the private quarters, where the air is thick with sorrow.")
    choice = input("Do you (A) Investigate the bedroom or (B) Search the study? ").lower()
    if choice == "a":
        print("You find a locket with a picture of the crown prince and a note: 'Help me...'")
        choice = input("Do you (A) Search for the prince's spirit or (B) Leave the palace? ").lower()
        if choice == "a":
            find_prince()
        else:
            print("You leave, but the prince's cry echoes in your mind. Game over.")
    else:
        print("You enter the study, filled with dusty books and ancient artifacts.")
        choice = input("Do you (A) Read a book or (B) Examine an artifact? ").lower()
        if choice == "a" or choice == "b":
            print("A dark truth unfolds before you...")
            find_diary()

def find_prince():
    print("The prince's ghost says, 'You must uncover the truth to free my soul.'")
    choice = input("Do you (A) Help him or (B) Run away? ").lower()
    if choice == "a":
        find_diary()
    else:
        print("You flee, leaving the prince trapped forever. Game over.")

start_game()
