import PySimpleGUI as psg
from modules import zip_creator

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
chose_button1 = psg.FilesBrowse("Choose", key="choose_files")

label2 = psg.Text("Select destination folder:")
input2 = psg.Input()
chose_button2 = psg.FolderBrowse("Choose", key="choose_destination")

compress_button = psg.Button("Compress")
output = psg.Text("", key="status")

window = psg.Window("File Compressor 3000",
                    layout=[[label1, input1, chose_button1],
                            [label2, input2, chose_button2],
                            [compress_button, output]
                            ],
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    print("Event:", event)
    print("Values:", values)

    filepaths = values['choose_files'].split(';')
    destination = values['choose_destination']
    print(filepaths)
    print(destination)

    if event == "Compress":
        zip_creator.make_archive(filepaths, destination)
        window['status'].update(value="Compression sucessful")

    elif event == psg.WIN_CLOSED:
        break
window.close()