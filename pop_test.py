import FreeSimpleGUI as gui

layout = [
    [gui.B("Test")],
    [gui.T("Test_2")]
]

window_1 = gui.Window("Popup Test", layout)

while True:
    events, values = window_1.read()

    if events == gui.WINDOW_CLOSED:
        break
    elif events == "-Test-":
        gui.popup_menu(window_1, gui.Listbox(gui.theme_list()), ["Theme Select"], "Pop Theme Test")

window_1.close()



