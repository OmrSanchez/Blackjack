import random

import FreeSimpleGUI as gui
import cards_dict
from functions import *

DECK_LIST = cards_dict.deck
# CARD_DEST_LIST = extract_dest_and_values(DECK_LIST)[0]
# CARD_VALUE_LIST = extract_dest_and_values(DECK_LIST)[1]

deck = extract_dest_and_values(DECK_LIST)
print(deck)
print(deck[0])

#Game display configs

BACKGROUND_COLOR = "teal"
GRAPH_COLOR = "green"
SCOREBOARD_COLOR = "darkgrey"

gui.set_options(font="Arial, 16", element_padding=(0,0), text_color="gold", border_width=0)
gui.theme("DarkGrey12")

# Game layout
game_title_image = gui.Image(source="Cards Pack/BlackJack Logo.png", size=(200, 50), key="-GAME-TITLE-IMG-", pad=(0,0))
start_button = gui.Button("START", key="-START-", mouseover_colors="gold")
# exit_button = gui.Button("EXIT", key="-EXIT-", button_color="red")
menu_ace = gui.Image(source="Cards Pack/Deck/Spades 1.png", size=(100, 150), key="-MENU-ACE-", pad=(5,30))
menu_jack = gui.Image(source="Cards Pack/Deck/Spades 11.png", size=(100, 150), key="-MENU-JACK-", pad=(5,30))

# Player Controls
hit_button = gui.Button("HIT", key="-HIT-", size=(10, 1), pad=(20, 10))
hold_button = gui.Button("HOLD", key="-HOLD-", size=(10, 1), pad=(20, 10))
# quit_button = gui.Button("QUIT", key="-QUIT-", button_color="red")
play_again_button = gui.Button("PLAY AGAIN", key="-PLAY-AGAIN-BUTTON-", size=(10,1), pad=(0, 95))

# Display both scores
start_score = 0
game_title_image_start = gui.Image(source="Cards Pack/BlackJack Logo.png", size=(196, 50), key="-GAME-TITLE-IMG-START-", pad=(0,0))
player_score = gui.Text(str(f"Your Score:\n\n        {start_score}"), text_color="white", key="-PLAYER-SCORE-", pad=(0,90))
npc_score = gui.Text(str(f"Opponent Score:\n\n            {start_score}"), text_color="white", key="-NPC-SCORE-", pad=(0,80))

# Create window and manage layout as a graph.
play_again_col = gui.Column([[play_again_button]],
							key="-PLAY-AGAIN-",
							visible=False,
							pad=(0,0))

scoreboard_col = gui.pin(gui.Column([[game_title_image_start], [npc_score], [player_score], [play_again_col]],
							size=(198, 625),
							element_justification="center",
							key="-SCOREBOARD-",
							visible=False,
							pad=(10,0)))

hit_hold_col = gui.Column([[hit_button, hold_button]],
						  	element_justification="center",
							key="-PLAYER-CONTROLS-",
						    size=(500,50),
						  	pad=(300, 0),
						  	visible=False)

layout = [
	[[gui.VPush()]],

	[gui.Push(), game_title_image, gui.Push()],

	[scoreboard_col,
	 gui.Graph(
		canvas_size=(800, 625),
		graph_bottom_left=(-250, -250),
		graph_top_right=(250, 250),
		key="-GRAPH-",
		background_color=GRAPH_COLOR,
		change_submits=True,
		drag_submits=True,
		visible=False,
	)],

	[hit_hold_col],

	[gui.Push(), gui.Column([[menu_jack, menu_ace]], key="-MENU-CARDS-", visible=True, element_justification="center"),
	 gui.Push()],

	[gui.Push(), gui.Column([[start_button]]), gui.Push()],

	[[gui.VPush()]],
]

window = gui.Window("Blackjack", layout, size=(1100, 800), finalize=True, location=(100, 100))
# size=(1022, 690)
graph = window["-GRAPH-"]
graph.draw_line((-250, 250), (250, 250), color="black", width=4)
graph.draw_line((-250, -250), (250, -250), color="black", width=4)
graph.draw_line((-250, 250), (-250, -250), color="black", width=4)
graph.draw_line((250, -250), (250, 250), color="black", width=4)

# MAIN GAME #
card_key_number = 1
PLAYER_X = -40
PLAYER_Y = -60
NPC_X = -50
NPC_Y = 150

player_score = 0
player_cards = []
npc_score = 0
npc_cards = []

while True:
	event, values = window.read()
	print(event, values)

	if event == gui.WINDOW_CLOSED or event == '-EXIT-':
		break
	elif event == '-QUIT-':
		break

	elif event == '-START-':
		# Display game
		window["-GAME-TITLE-IMG-"].update(visible=False)
		window["-MENU-CARDS-"].update(visible=False)
		window["-START-"].update(visible=False)

		window["-PLAYER-CONTROLS-"].update(visible=True)
		window["-PLAYER-SCORE-"].update(visible=True)
		window["-NPC-SCORE-"].update(visible=True)
		window["-SCOREBOARD-"].update(visible=True)
		window["-GRAPH-"].update(visible=True)

		# Track Cards
		player_cards = [get_card(deck) for count in range(2)]
		print(f"Player Cards: {player_cards}")

		npc_cards = [get_card(deck) for count in range(2)]
		print(f"NPC Cards: {npc_cards}")

		# Track Scores
		player_score = get_score(player_cards)
		print(f"Player Score: {player_score}")
		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))

		npc_score = get_score(npc_cards)
		print(f"NPC Score: {npc_score}")
		window["-NPC-SCORE-"].update(str(f"Your Score:\n\n        {npc_score}"))

		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i]['dest'], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20
			PLAYER_Y += 20

		graph.DrawImage("Cards Pack/card_colors/Back Blue 1.png", location=(NPC_X, NPC_Y))
		graph.DrawImage(npc_cards[1]['dest'], location=(NPC_X + 20, NPC_Y + 20))

	elif event == '-HIT-':
		next_card = get_card(deck)
		player_cards.append(next_card)

		player_score += next_card['value']
		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))

		graph.erase()

		PLAYER_X = -40
		PLAYER_Y = -60
		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i]['dest'], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20
			PLAYER_Y += 20

		graph.DrawImage("Cards Pack/card_colors/Back Blue 1.png", location=(NPC_X, NPC_Y))
		graph.DrawImage(npc_cards[1]['dest'], location=(NPC_X + 20, NPC_Y + 20))

	elif event == '-HOLD-':
		window["-PLAYER-CONTROLS-"].update(visible=False)
		window["-PLAY-AGAIN-"].update(visible=True)
		npc_cards, npc_score_number, npc_index, npc_card_values_list = npc_hit(CARD_VALUE_LIST, DECK_DEST_LIST)
		for i in npc_cards:
			graph.DrawImage(i, location=(NPC_X, NPC_Y))
			NPC_X += 20
		window["-NPC-SCORE-"].update(npc_score_number)

		declare_result(current_sum, npc_score_number)

	# elif event == '-PLAY-AGAIN-BUTTON-':
	# 	DECK_DEST_LIST = extract_dest_and_values(DECK_LIST)[0]
	# 	window["-PLAYER-CONTROLS-"].update(visible=True)
	# 	window["-PLAY-AGAIN-"].update(visible=False)
	# 	window["-GRAPH-"].erase()
	# 	player_cards = [select_cards(DECK_DEST_LIST)[0] for i in range(2)]
	# 	init_index = store_index(player_cards, DECK_DEST_LIST)
	# 	current_card_values_list = [CARD_VALUE_LIST[i] for i in init_index]
	# 	for i in current_card_values_list:
	# 		if check_ace(i):
	# 			if (sum(current_card_values_list) - i) + 11 > 21:
	# 				current_card_values_list.remove(i)
	# 				current_card_values_list.append(1)
	# 			elif (sum(current_card_values_list) < 21) and (sum(current_card_values_list) - i) + 11 <= 21:
	# 				current_card_values_list.remove(i)
	# 				current_card_values_list.append(11)
	# 	current_sum = sum(current_card_values_list)
	# 	player_score.update(current_sum)
	# 	window["-SCORE-"].update(current_sum)
	# 	npc_score = "0"
	# 	window["-NPC-SCORE-"].update(npc_score)
	# 	for i in range(len(player_cards)):
	# 		graph.DrawImage(player_cards[i], location=(PLAYER_X, PLAYER_Y))
	# 		PLAYER_X += 20

window.close()