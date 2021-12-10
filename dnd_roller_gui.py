import random
import PySimpleGUI as sg

sg.theme('DarkPurple')    # Keep things interesting for your users

layout = [[sg.Text('DND Dice Roller')],      
          [sg.Button("D100"), sg.Button("D20")],
          [sg.Button("D12"), sg.Button("D10")],
          [sg.Button("D8"), sg.Button("D6")],
          [sg.Button("D4")],
          [sg.Text('Roll Appear Here: '), sg.Text(size=(15,1), key='-OUTPUT-')],      
          [sg.Exit()]]      

window = sg.Window('DND Dice Roller', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == "D100":
        roll = random.randint(1,100)
        window['-OUTPUT-'].update(roll)
    if event == "D20":
        roll = random.randint(1,20)
        window['-OUTPUT-'].update(roll)
    if event == "D12":
        roll = random.randint(1,12)
        window['-OUTPUT-'].update(roll)
    if event == "D10":
        roll = random.randint(1,10)
        window['-OUTPUT-'].update(roll)
    if event == "D8":
        roll = random.randint(1,8)
        window['-OUTPUT-'].update(roll)
    if event == "D6":
        roll = random.randint(1,6)
        window['-OUTPUT-'].update(roll)
    if event == "D4":
        roll = random.randint(1,4)
        window['-OUTPUT-'].update(roll)
window.close()