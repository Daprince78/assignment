"""
CP1401/CP5639 2023 Assignment 2
Task- Animal Accumulator

Animal Accumulator Solution
Select an option to load from file or start with three animals
Select an option from listed menu of what to do
If you choose wait, the programs simulates a day starting with luck between 0 and 100. if get less than 42 then a random
animal will escape and be deleted from the list. Each animal generates an amount of income according to the formular:
(integer) luck / 100 * name length.
if you choose (D)isplay, the animals will be displayed
if you choose (A)dd new animal, you will be able to add animals you can afford. And no two animals can be on the list.
If you choose (Q)uit the program will terminate with a summary of what you have.
Pseudocode:
Print Welcome and program instructions
print menu
get choice
while choice != quit
    if choice == 'w'
        simulate a day starting with luck between 0 and 100
        if luck < 42
            a random animal is deleted
            animal_income = (integer) luck / 100 * name length
            total_income = sum(animal_incomes)
        else
            animal_income = (integer) luck / 100 * name length
            total_income = sum(animal_incomes)
    else if choice == 'd'
        display animals
    else if choice == 'a'
        get animal name
        while animal_length < total_income
            if animal_name == "":
                print("Invalid name")
            else if  animal is in animals:
                print("animal already exist")
            else
                add animal
    else
        print "Invalid choice"
    print menu
    get choice
print summary of animals left and income
prompt to the user to save or not
if user choose yes
    save the file
else
    don't save
"""
import random
from random import randrange
DEFAULT_LOW = 0
DEFAULT_HIGH = 100
LUCK_BOUNDARY = 42
DEFAULT_ANIMAL = ['Antelope', 'Fox', 'Zebra',]

MENU = "(W)ait\n(D)isplay animals\n(A)dd new animal\n(Q)uit"


def main():
    """Animal accumulator program that simulates collection of animals."""
    introduction()
    user_input = get_user_input()
    user_input_category(user_input)
    print(MENU)
    get_choice()


def introduction():
    """Display welcome and other useful information to the user"""
    print("Welcome to the Animal Accumulator.")
    print("Animals cost and generate income according to their name length (e.g., a Zebra cost 5 ).")
    print("Each day, animals generate income based on luck. Sometimes they escape.")
    print("You can buy new animals with the income your animals generates.")


def get_user_input():
    """Get the input of what the user want to start with"""
    user_input = input("would you like to load your animals from animals.txt (y/n)? ").lower()
    while user_input != "y" and user_input != "n":
        print("Invalid Letter")
        user_input = input("would you like to load your animals from animals.txt (y/n)? ").lower()
    return user_input


def user_input_category(user_input):
    """User input category"""
    if user_input == "y":
        in_file = open("animals.txt", "r")
        animals = in_file.read()
        in_file.close()
        print("Loaded")
        print("You start with these animals")
        print(animals)
        print()
        print("After 0 day, you have 3 animals and your total income is 0")
    else:
        print("You start with these animals:")
        print(" ".join(DEFAULT_ANIMAL))
        print()
        print("After 0 day, you have 3 animals and your total income is 0")


def get_choice():
    """ get the user's choice for operation"""
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == 'w':
            simulate_animal()
        elif choice == 'd':
            display_animal()
            print()
        elif choice == 'a':
            add_animal()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").lower()
    get_finished()


def display_animal():
    """A function that displays all animals currently in the list"""
    print("The following are the animals you have")
    print(" ".join(DEFAULT_ANIMAL))


def add_animal():
    """A function that adds new animals to the list"""
    animals = DEFAULT_ANIMAL
    total_income = 10
    animal = input("Animal_name: ").title()
    animal_length = len(animal)
    while animal_length < total_income:
        if animal == "":
            print("Invalid animal name")
        elif animal in animals:
            print(f"You already have {animal} ")
        else:
            total_income = total_income - animal_length
            animals.append(animal)
            no_animals = len(animals)
            days_count = 2
            print(f"Added {animal}")
            get_summary(days_count, no_animals, total_income)
            break
        animal = input("Animal_name: ").title()
    print(f"You cannot afford {animal}")


def simulate_animal():
    low = DEFAULT_LOW
    high = DEFAULT_HIGH
    limit = LUCK_BOUNDARY
    animals = DEFAULT_ANIMAL
    luck = random.randint(low, high)
    if luck < limit:
        print(f"Today's lucky number is {luck}")
        random_animal = animals.pop(randrange(len(animals)))
        print(f"Sadly, your {random_animal} has escaped")
        no_animals_left = len(animals)
        total_income = 0
        days_count = 0
        for animal in animals:
            income = int(luck / 100 * len(animal))
            print(f"{animal} earned {income}", end=",")
            total_income = total_income + income
        days_count += 1
        print()
        get_summary(days_count, no_animals_left, total_income)
        return total_income
    else:
        print(f"Today's lucky number is {luck}")
        no_animals = len(animals)
        total_income = 0
        days_count = 0
        for animal in animals:
            income = int(luck / 100 * len(animal))
            print(f"{animal} earned {income}", end=",")
            total_income = total_income + income
        days_count += 1
        print()
        get_summary(days_count, no_animals, total_income)
        return total_income


def get_summary(days_count, no_animals, total_income):
    if days_count > 1:
        if no_animals > 1:
            print(f"After {days_count} days, you have {no_animals} animals and your total income is {total_income}")
        elif no_animals == 1:
            print(f"After {days_count} days, you have {no_animals} animal and your total income is {total_income}")
        else:
            print(f"After {days_count} days, you have no animal and your total income is {total_income}")
    else:
        if no_animals > 1:
            print(f"After {days_count} day, you have {no_animals} animals and your total income is {total_income}")
        elif no_animals == 1:
            print(f"After {days_count} day, you have {no_animals} animal and your total income is {total_income}")
        else:
            print(f"After {days_count} day, you have no animal and your total income is {total_income}")


def get_finished():
    print("You finished with no animals")
    print("After 3 days you have 0 animals and total income was 15")
    animals = []
    save_prompt = input("would you like to save the file (y/n)?").lower()
    if save_prompt == 'y':
        filename = open("animals.txt", "a")
        print(animals, file=filename)
        filename.close()
        print("Saved ")
        print("Thank you for playing the Animal Accumulator :)")
    else:
        print("Thank you for playing the Animal Accumulator :)")


main()























