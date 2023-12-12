# VERSION 2
# MATCH CASE changed to IF conditions
# values/indexes provided together with the key command

#from functions_for_app1 import get_todos, write_todos
from modules import functions_for_app1

while True:
    user_action = input("Enter ADD | SHOW | EDIT | | DELETE | EXIT: ").lower()

    if user_action.startswith("add"):
        todos = functions_for_app1.get_todos()

        todo = user_action[4:] + "\n"
        todos.append(todo)

        functions_for_app1.write_todos(todos)

    elif user_action.startswith("show") or 's' in user_action[0:1]:
        todos = functions_for_app1.get_todos()

        todos = [i.strip('\n') for i in todos]

        for index, value in enumerate(todos):
            index += 1
            print(f"{index} - {value.title()}")

    elif user_action.startswith("edit"):
        try:
            todos = functions_for_app1.get_todos()

            index = int(user_action[5:]) - 1
            edited_todo = input("Enter a new todo: ") + '\n'
            todos.__setitem__(index, edited_todo)

            functions_for_app1.write_todos(todos)
        except ValueError:
            print("Incorrect value")
            continue

    elif user_action.startswith("delete"):
        try:
            todos = functions_for_app1.get_todos()

            index = int(user_action[7:]) - 1
            removed_todo = todos.pop(index).strip('\n')
            print(f"{removed_todo} was removed.")

            functions_for_app1.write_todos(todos)
        except IndexError:
            print("Index out of range")
            continue
    elif user_action.startswith("exit") or 'x' in user_action[0:1]:
        break

    else:
        print("You entered invalid command")

print("Bye!")