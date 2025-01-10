shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def check_empty_list(shopping_list_menu):
    if shopping_list_menu == []:
        print("Shopping list is empty!")
        return True
    return False
