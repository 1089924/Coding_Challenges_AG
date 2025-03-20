todo_list = ['write email', 'finish homework', 'call mom', 'clean room']
print(todo_list)

item_to_remove = input("Enter the item to remove from the list: ")
if item_to_remove in todo_list:
    todo_list.remove(item_to_remove)
    print(todo_list)
else:
    print(f"'{item_to_remove}' is not in the list.")

inp = input("Would you like to remove more items? (yes/no): ").strip().lower()
if inp == 'yes':
    item_to_remove = input("Enter another item to remove from the list: ")
    if item_to_remove in todo_list:
        todo_list.remove(item_to_remove)
        print(todo_list)
    else:
        print(f"'{item_to_remove}' is not in the list.")
else:
    print("Thank you for using our service.")