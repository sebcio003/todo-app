import streamlit as stl
from modules import functions_for_app1

todos = functions_for_app1.get_todos()

def add_todo():
    new_todo = stl.session_state["input_box_key"] + "\n"
    todos.append(new_todo)
    functions_for_app1.write_todos(todos)


stl.title("My todo app")
stl.subheader("This is my todo app.")
stl.write("This app is to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = stl.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(index)
        functions_for_app1.write_todos(todos)
        del stl.session_state[todo]
        stl.experimental_rerun()


stl.text_input(label="Enter a todo", label_visibility="collapsed", placeholder="Add a new todo...",
               on_change=add_todo, key="input_box_key")

print(stl.session_state)