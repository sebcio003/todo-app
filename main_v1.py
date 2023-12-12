# VERSION 1

filepath = "files/todos.txt"

while True:
    user_action = input("Enter ADD | SHOW | EDIT | | DELETE | EXIT: ")
    match user_action:
        case 'add' | 'a':
            with open(filepath, 'r') as file:
                todos = file.readlines()

            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            with open(filepath, 'w') as file:
                file.writelines(todos)

        case 'show' | 's':
            with open(filepath, 'r') as file:
                todos = file.readlines()

            todos = [i.strip('\n') for i in todos]

            for index, value in enumerate(todos):
                index += 1
                print(f"{index} - {value.title()}")

        case 'edit' | 'e':
            with open(filepath, 'r') as file:
                todos = file.readlines()

            index = int(input("Which todo to edit?: ")) - 1
            edited_todo = input("Enter a new todo: ") + '\n'
            todos.__setitem__(index, edited_todo)

            with open(filepath, 'w') as file:
                file.writelines(todos)

        case 'delete' | 'd':
            with open(filepath, 'r') as file:
                todos = file.readlines()

            index = int(input("Which todo to delete?: ")) - 1
            removed_todo = todos.pop(index)
            print(f"{removed_todo} was removed.")

            with open(filepath, 'w') as file:
                file.writelines(todos)

        case 'exit' | 'x':
            break

        case whatever:
            print("You entered invalid command")

print(todos)
print("Bye!")