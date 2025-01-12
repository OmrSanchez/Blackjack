import FreeSimpleGUI as gui
import cards_dict
from functions import *

DECK_LIST = cards_dict.card_values_dict
DECK_DEST_LIST = extract_dest_and_values(DECK_LIST)[0]
CARD_VALUE_LIST = extract_dest_and_values(DECK_LIST)[1]

gui.theme('DarkAmber')

# Game layout
game_title_image = gui.Image(source="Cards Pack/BlackJack Logo.png", size=(200, 50), key="-GAME-TITLE-")
play_button_path = gui.Button("PLAY", key="-PLAY-", auto_size_button=True)
exit_button = gui.Button("EXIT", key="-EXIT-", auto_size_button=True, button_color="red")

# Player Controls
hit_button = gui.Button("HIT", key="-HIT-")
hold_button = gui.Button("HOLD", key="-HOLD-")
quit_button = gui.Button("QUIT", key="-QUIT-", button_color="red")
play_again_button = gui.Button("PLAY AGAIN", key="-PLAY-AGAIN-BUTTON-", visible=True, font="Arial, 20", auto_size_button=True, pad=(0, 10))

# Player Main Logic
player_cards = [select_cards(DECK_DEST_LIST)[0] for i in range(2)]
init_index = store_index(player_cards, DECK_DEST_LIST)
current_card_values_list = [CARD_VALUE_LIST[i] for i in init_index]
remove_cards(player_cards, DECK_DEST_LIST)
current_sum = sum(current_card_values_list)
current_score = gui.Text(current_sum, font=("Arial", 12), key="-SCORE-", pad=(10, 10))

# NPC placeholder
npc_score = gui.Text("0", font=("Arial", 12), key="-NPC-SCORE-", pad=(10, 10))

# Create window and manage layout as a graph.
layout = [
	[[gui.Column([[game_title_image]])]],
	[[gui.Column([[gui.pin(gui.Frame("Your Score",[[current_score]], key="-PLAYER-SCORE-", element_justification="center", visible=False)),
	 gui.Graph(
		canvas_size=(600, 600),
		graph_bottom_left=(-150, -150),
		graph_top_right=(150, 150),
		key="-GRAPH-",
		background_color="green",
		change_submits=True,
		drag_submits=True,
	), gui.pin(gui.Frame("Opponent Score",[[npc_score]], key="-COMPUTER-SCORE-", element_justification=("center"), visible=False))]])]],
	[gui.pin(gui.Column([[play_button_path, exit_button]], key="-MAIN-MENU-BUTTONS-", element_justification="center"))],
	[gui.pin(gui.Column([[hit_button, hold_button, quit_button]], key="-PLAYER-CONTROLS-", visible=False))],
	[gui.pin(gui.Column([[play_again_button]], key="-PLAY-AGAIN-", visible=False, element_justification="center"))],
]

window = gui.Window("Blackjack", layout, size=(950, 750), finalize=True,  element_justification='center')
graph = window["-GRAPH-"]

# MAIN GAME #
while True:
	event, values = window.read()
	print(event, values)
	card_key_number = 1
	PLAYER_X = -40
	PLAYER_Y = -50
	NPC_X = -50
	NPC_Y = 115
	if event == gui.WINDOW_CLOSED or event == '-EXIT-':
		break
	elif event == '-QUIT-':
		break

	elif event == '-PLAY-':
		# Display game
		window["-MAIN-MENU-BUTTONS-"].update(visible=False)
		window["-PLAYER-CONTROLS-"].update(visible=True)
		window["-PLAYER-SCORE-"].update(visible=True)
		window["-COMPUTER-SCORE-"].update(visible=True)

		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20

	elif event == '-HIT-':
		card_key_number += 1
		next_card = select_cards(DECK_DEST_LIST)[0]
		player_cards.append(next_card)
		next_card_value = CARD_VALUE_LIST[DECK_DEST_LIST.index(next_card)]
		current_card_values_list.append(next_card_value)
		remove_next_card(player_cards, DECK_DEST_LIST)
		for i in current_card_values_list:
			if check_ace(i):
				if (sum(current_card_values_list) - i) + 11 > 21:
					current_card_values_list.remove(i)
					current_card_values_list.append(1)
				elif (sum(current_card_values_list) < 21) and (sum(current_card_values_list) - i) + 11 <= 21:
					current_card_values_list.remove(i)
					current_card_values_list.append(11)
		current_sum = sum(current_card_values_list)
		for i in player_cards:
			graph.DrawImage(i, location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20
		window["-SCORE-"].update(current_sum)

	elif event == '-HOLD-':
		window["-PLAYER-CONTROLS-"].update(visible=False)
		window["-PLAY-AGAIN-"].update(visible=True)
		npc_cards, npc_score_number, npc_index, npc_card_values_list = npc_hit(CARD_VALUE_LIST, DECK_DEST_LIST)
		for i in npc_cards:
			graph.DrawImage(i, location=(NPC_X, NPC_Y))
			NPC_X += 20
		window["-NPC-SCORE-"].update(npc_score_number)

		declare_result(current_sum, npc_score_number)

	elif event == '-PLAY-AGAIN-BUTTON-':
		DECK_DEST_LIST = extract_dest_and_values(DECK_LIST)[0]
		window["-PLAYER-CONTROLS-"].update(visible=True)
		window["-PLAY-AGAIN-"].update(visible=False)
		window["-GRAPH-"].erase()
		player_cards = [select_cards(DECK_DEST_LIST)[0] for i in range(2)]
		init_index = store_index(player_cards, DECK_DEST_LIST)
		current_card_values_list = [CARD_VALUE_LIST[i] for i in init_index]
		remove_cards(player_cards, DECK_DEST_LIST)
		for i in current_card_values_list:
			if check_ace(i):
				if (sum(current_card_values_list) - i) + 11 > 21:
					current_card_values_list.remove(i)
					current_card_values_list.append(1)
				elif (sum(current_card_values_list) < 21) and (sum(current_card_values_list) - i) + 11 <= 21:
					current_card_values_list.remove(i)
					current_card_values_list.append(11)
		current_sum = sum(current_card_values_list)
		current_score.update(current_sum)
		window["-SCORE-"].update(current_sum)
		npc_score = "0"
		window["-NPC-SCORE-"].update(npc_score)
		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20

window.close()