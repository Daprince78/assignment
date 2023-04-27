def main():
    name = input("Enter your name: ")
    display_menu()
    choice = input("Enter your choice ")
    while choice != "Q":
        choice_category = get_category(choice)
        print(f"{choice_category} {name}")
        display_menu()
        choice = input("Enter your choice ")
    print("Finished")


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def get_category(choice):
    if choice == "H":
        return "hello"
    elif choice == "G":
        return "goodbye"
    else:
        return "Invalid Choice"


main()

