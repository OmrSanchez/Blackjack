import FreeSimpleGUI as gui

def change_theme():
	values = (gui.theme_list())
	themes_col = gui.Listbox(values,
							 enable_events=True,
							 font="Arial, 8",
							size=(20, 10))

	layout = [
		[gui.T("Select a theme:", font="Ariel, 12")],
		[themes_col, gui.Button("CONFIRM", key="-CONFIRM-", size=(8,1))]
	]
	theme_win = gui.Window('Themes', layout, size=(600,300), finalize=True)


	while True:
		event, values = theme_win.read()
		print(f"Theme Window: {event, values}")
		print(values[0][0])
		print(event)
		if event == gui.WINDOW_CLOSED or event == '-EXIT-':
			break
		elif event == "-CONFIRM-":
			break

	theme_win.close()
	return values[0][0]


