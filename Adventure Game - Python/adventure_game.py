import time
import random

villano = ""
arma = ""
poder_ganar = False


def start_game():
    global poder_ganar
    poder_ganar = False
    global villano
    villano = random.choice(['dragon', 'monster', 'giant'])
    global arma
    arma = random.choice(['magic rock', 'sword', 'teaser'])
    # change
    print_pause("\nYou find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    # change
    print_pause("Rumor has it that a wicked fairie is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("You are holding your trusty (but not effective) dagger.")
    run()


def print_pause(s):
    print(s)
    time.sleep(2)


def cave():
    global poder_ganar
    print_pause("\nYou peer cautiously into the cave.")
    # change
    if poder_ganar:
        print_pause("Oh! There is nothing new in the cave.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("You have found the " + arma + "!")
        # change
        print_pause("You discard your silly old dagger "
                    "and take the " + arma + " with you.")
    print_pause("You walk back out to the field.")
    poder_ganar = True
    run()


def house():
    print_pause("\nAfter a few seconds a " + villano + " appears.")
    print_pause("You need to decide:")
    print_pause("1) Fight the " + villano + ".")
    print_pause("2) Run away.")
    h = ""
    while h != "1" and h != "2":
        h = input("Please enter 1) or 2)): ")
        if h == "1":
            fight()
        elif h == "2":
            run()
        else:
            print("Try again selecting a valid option.")


def fight():
    print("")
    if poder_ganar:
        print_pause("CONGRATS, YOU WON!")
    else:
        print_pause("GAME OVER")
    restart = ""
    while restart != "n" and restart != "y":
        # change
        restart = input("Would you like to play again? (y/n)").lower()
        if restart == "y":
            start_game()
        elif restart == "n":
            print("Hope to see you again soon")
        else:
            print("Try again selecting a valid option.")


def run():
    print_pause("\nYou have a choice to make:")
    print_pause("1) Knock on the door of the house.")
    print_pause("2) Peer into the cave.")
    r = ""
    while r != "1" and r != "2":
        r = input("What would you do? (Please enter 1) or 2)): ")
        if r == "1":
            house()
        elif r == "2":
            cave()
        else:
            print("Try again selecting a valid option.")


# change
if __name__ == "__main__":
    start_game()
