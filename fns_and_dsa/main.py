from arithmetic_operations import perform_operation
from shopping_list_manager import display_menu, check_empty_list

# print("Arithmetic Operations")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
# operations = perform_operation(num1, num2, operation)
# print(operations)
shopping_list = []
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        # Prompt for and add an item
        item_name = input("Enter item name: ").lower().strip()
        shopping_list.append(item_name)
        print(item_name, "has been added to shopping list successfully.")
    elif choice == '2':
        # Prompt for and remove an item
        if check_empty_list(shopping_list):
            pass
        else:
            item_name = input("Enter item name: ").lower().strip()
            if item_name in shopping_list:
              shopping_list.remove(item_name)
              print(item_name, "has been removed from shopping list successfully.")
            else:
                print("Item not found in list!")
    elif choice == '3':
        # Display the shopping list
        if check_empty_list(shopping_list):
            pass
        else:
            for item in shopping_list:
                print(item)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")