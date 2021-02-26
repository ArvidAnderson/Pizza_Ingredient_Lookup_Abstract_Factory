import PySimpleGUI as sg
import Pizza_Ingredient_Lookup

def start_screen():
    sg.theme('DarkGrey12')

    layout = [[sg.Text('Pizza Ingredient Lookup')],
            [sg.InputText()],
            [sg.Text(''), sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Lookup'), sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Pizza Ingredient Lookup', layout, size=(600,300), font='Courier 25')

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Lookup':
            input_order = values[0]
            saved_ingredient = Pizza_Ingredient_Lookup.pizza_run_gui(input_order)
            window['-OUTPUT-'].update(saved_ingredient)
    window.close()


if __name__ == "__main__":
    start_screen()