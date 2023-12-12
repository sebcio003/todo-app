from modules import functions_for_app1
import PySimpleGUI as psg

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="todo_key") #output when ADD pressed: ('Add', {'todo_key': 'hello'})
add_button = psg.Button("Add")

window = psg.Window("My To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == "Add":
        todos = functions_for_app1.get_todos()
        todo = values['todo_key'] + "\n"
        todos.append(todo)

        functions_for_app1.write_todos(todos)

    elif event == psg.WIN_CLOSED:
        break

window.close()