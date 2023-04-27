import random
LUCK_THRESHOLD_LOW = 0
LUCK_THRESHOLD_HIGH = 100
LUCK_BOUNDARY = 42
DEFAULT_ANIMAL = ['Antelop,', 'Fox,', 'Zebra,']


def main():
    introduction()
    user_input = get_user_input()
    user_input_category(user_input)
    display_menu()
    choice = input("choose alphabets in CAPS: ")
    choice2 = choice.lower()
    while choice2 != "q":
        selected_choice = get_menu_category(choice2)
        if selected_choice == "w":
            calculate_wait()
        if selected_choice == "a":
            animal = input("Animal name: ")
            animal_list = add_animal(animal)
            animal_length = len(animal_list)
            animal_sorted_list = sorted(animal_list)
            print(f"After 0 days, you have {animal_length} animals and your total income is 0")
        if selected_choice == "d":
            display_animal()
        display_menu()
        choice = input("choose alphabets in caps: ")
        choice2 = choice.lower()
    print("Finished")
    get_menu_category(choice)


def introduction():
    print("Welcome to the Animal Accumulator.")
    print("Animals cost and generate income according to their name length (e.g., a Zebra cost 5 ).")
    print("Each day, animals generate income based on luck. Sometimes they escape.")
    print("You can buy new animals with the income your animals generates.")


def get_user_input():
    user_input = input("would you like to load your animals from animals.txt (y/n)? ")
    user_input2 = user_input.lower()
    while user_input2 != "y" and user_input2 != "n":
        print("Invalid Letter")
        user_input = input("would you like to load your animals from animals.txt (y/n)? ")
        user_input2 = user_input.lower()
    return user_input2


def user_input_category(user_input):
    if user_input == "y":
        print("yy")
    else:
        print("You start with these animals:")
        print(" ".join(DEFAULT_ANIMAL))


def display_menu():
    print("(W)ait")
    print("(D)isplay animals")
    print("(A)dd new animal")
    print("(Q)uit")


def get_menu_category(choice2):
    if choice2 == "w":
        return choice2
    elif choice2 == "d":
        return choice2
    elif choice2 == "a":
        return choice2
    else:
        print("Invalid Alphabet")


def calculate_wait():
    print()


def display_animal():
    print(" ".join(DEFAULT_ANIMAL))


def add_animal(animal):
    total_animal = DEFAULT_ANIMAL
    while animal != "":
        total_animal.append(animal)
    return total_animal


main()


