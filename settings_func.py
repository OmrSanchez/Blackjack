import FreeSimpleGUI as gui

def change_graph_color(event):
	match event:
		case "Black":
			return 'black'
		case "Red":
			return 'red'
		case "Green":
			return 'green'
		case "Blue":
			return 'blue'

def change_card_color(event):
	match event:
		case "Red Cards":
			return "Cards Pack/back_of_cards/Back Red 1.png"
		case "Blue Cards":
			return "Cards Pack/back_of_cards/Back Blue 1.png"
		case "Grey Cards":
			return "Cards Pack/back_of_cards/Back Grey 1.png"

# ------------------- Create the window -------------------
def make_window(theme=None):
    if theme:
        gui.theme(theme)
    # -----  Layout & Window Create  -----
    layout = [[gui.T('This is your layout')],
              [gui.Button('Ok'), gui.Button('Change Theme'), gui.Button('Exit')]]

    return gui.Window('Pattern for changing theme', layout)


# ------------------- Main Program and Event Loop -------------------
def main():
    window = make_window()

    while True:
        event, values = window.read()
        if event == gui.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Change Theme':      # Theme button clicked, so get new theme and restart window
            event, values = gui.Window('Choose Theme', [[gui.Combo(gui.theme_list(), readonly=True, k='-THEME LIST-'), gui.OK(), gui.Cancel()]]).read(close=True)
            print(event, values)
            if event == 'OK':
                window.close()
                window = make_window(values['-THEME LIST-'])

    window.close()




