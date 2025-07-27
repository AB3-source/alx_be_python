# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. View list")
    print("3. Exit")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    elif choice == 2:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select from the menu.")