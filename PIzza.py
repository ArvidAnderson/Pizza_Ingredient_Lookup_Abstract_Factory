import PySimpleGUI as sg
import Pizza_Ingredient_Lookup


def menu():
    sg.theme('DarkGrey12')

    layout = [[sg.Text('Menu:')],
              [sg.Text("""Vesuvio
Cacciatore
Pescatore
Marinara
Tomaso
Peperone
Margherita
Capricciosa
Calzone
Riviera
La maffia
Mama Mia
Pranzo
Dennisso
Hawaii
Vegetariana
Bambino
Bari
Africana""", size=(20, 15), font='Courier 20')],
              [sg.Submit('OK')]]

    window = sg.Window('Pizzeria Los Arvid', layout, finalize=True, no_titlebar=True, grab_anywhere=True,
                       border_depth=4,
                       size=(300, 600), font='Courier 20')
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'OK':
            window.close()
            main()

    window.close()


def main():
    sg.theme('DarkGrey12')

    layout = [[sg.Text('Pizza Ingredient Lookup')],
              [sg.InputText()],
              [sg.Text(size=(40, 1), font='Courier 20', key='-OUTPUT-')],
              [sg.Submit('Lookup'), sg.Button('Show Menu'), sg.Button('Exit')]]

    window = sg.Window('Pizzeria Los Arvid', layout, finalize=True, no_titlebar=True, grab_anywhere=True,
                       border_depth=4,
                       size=(600, 200), font='Courier 25')
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Lookup':
            input_order = values[0]
            saved_ingredient = Pizza_Ingredient_Lookup.pizza_run_gui(input_order.lower().replace(" ", ""))
            if saved_ingredient[0]:
                window['-OUTPUT-'].update(text_color='green')
                window['-OUTPUT-'].update(saved_ingredient[1])
            else:
                window['-OUTPUT-'].update(text_color='Red')
                window['-OUTPUT-'].update(saved_ingredient[1])
        if event == 'Show Menu':
            menu()
    window.close()


if __name__ == "__main__":
    main()
