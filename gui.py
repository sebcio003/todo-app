from modules import functions_for_app1
import PySimpleGUI as psg

label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter todo")
add_button = psg.Button("Add")

window = psg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()