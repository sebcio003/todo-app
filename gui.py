from modules import functions_for_app1
import PySimpleGUI as psg
import time
import os

if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file:
        pass

psg.theme("Black")

clock = psg.Text("", key="clock")
label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="input_key") #output when ADD pressed: ('Add', {'todo_key': 'hello'})
add_button = psg.Button(key="Add", image_source="files/add.png", size=5, mouseover_colors="Yellow", tooltip="Add todo")
list_box = psg.Listbox(values=functions_for_app1.get_todos(), key='list_box_key', enable_events=True, size=[44,10])
edit_button = psg.Button("Edit")
delete_button = psg.Button("Delete")
exit_button = psg.Button("Exit")

window = psg.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]
                            ],
                    font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    print('Event is:',event)
    print(values)

    if event == "Add":
        todos = functions_for_app1.get_todos()

        new_todo = values['input_key'] + "\n"
        todos.append(new_todo)

        functions_for_app1.write_todos(todos)
        window['list_box_key'].update(values=todos)

    elif event == "Edit":
        try:
            todos = functions_for_app1.get_todos()

            new_todo = values['input_key'] + "\n"
            index = todos.index(values['list_box_key'][0])
            todos.__setitem__(index, new_todo)

            functions_for_app1.write_todos(todos)
            window['list_box_key'].update(values=todos)

        except IndexError:
            psg.popup("Please select an item first to edit")
            continue

    elif event == "list_box_key":
        # Update the INPUT box to the value selected from the listbox
        window['input_key'].update(value=values['list_box_key'][0].strip("\n"))

    elif event == "Delete":
        try:
            todos = functions_for_app1.get_todos()
            todo_to_delete = values['list_box_key'][0]
            todos.remove(todo_to_delete)

            functions_for_app1.write_todos(todos)
            window['list_box_key'].update(values=todos)
            window['input_key'].update(value="")

        except IndexError:
            psg.popup("Please select an item first to edit")
            continue
    elif event == "Exit":
        break
    elif event == psg.WIN_CLOSED:
        break
        #exit()

    else:
        continue

window.close()