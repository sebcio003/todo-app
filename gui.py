from modules import functions_for_app1
import PySimpleGUI as psg

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter todo", key="input_key") #output when ADD pressed: ('Add', {'todo_key': 'hello'})
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions_for_app1.get_todos(), key='list_box_key', enable_events=True, size=[44,10])
edit_button = psg.Button("Edit")
delete_button = psg.Button("Delete")
exit_button = psg.Button("Exit")

window = psg.Window("My To-Do App",
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]
                            ],
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    print('Event is:',event)
    print(values)

    if event == "Add":
        todos = functions_for_app1.get_todos()

        new_todo = values['input_key'] + "\n"
        todos.append(new_todo)

        functions_for_app1.write_todos(todos)
        window['list_box_key'].update(values=todos)

    elif event == "Edit":
        todos = functions_for_app1.get_todos()

        new_todo = values['input_key']
        index = todos.index(values['list_box_key'][0])
        todos.__setitem__(index, new_todo)

        functions_for_app1.write_todos(todos)
        window['list_box_key'].update(values=todos)

    elif event == "list_box_key":
        # Update the INPUT box to the value selected from the listbox
        window['input_key'].update(value=values['list_box_key'][0])

    elif event == "Delete":
        todos = functions_for_app1.get_todos()
        todo_to_delete = values['list_box_key'][0]
        todos.remove(todo_to_delete)

        functions_for_app1.write_todos(todos)
        window['list_box_key'].update(values=todos)
        window['input_key'].update(value="")

    elif event == "Exit":
        break
    elif event == psg.WIN_CLOSED:
        break
        #exit()

window.close()