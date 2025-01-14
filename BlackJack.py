import FreeSimpleGUI as gui
import cards_dict
from functions import *

DECK_LIST = cards_dict.deck
DECK = extract_dest_and_values(DECK_LIST)

#Game display configs
BACKGROUND_COLOR = "teal"
GRAPH_COLOR = "green"
SCOREBOARD_COLOR = "darkgrey"
START_SCORE = 0
gui.set_options(font="Arial, 18", element_padding=(0,0), text_color="gold", border_width=0)
gui.theme("DarkGrey12")


game_title_image = gui.Image(source="Cards Pack/BlackJack Logo.png", size=(200, 50), key="-GAME-TITLE-IMG-", pad=(0,0))
blackjack_button = gui.Button("BLACKJACK", key="-BLACKJACK-", mouseover_colors="gold")
play_button = gui.Button("PLAY", key="-PLAY-", size=(10, 1), pad=(20, 10))
menu_ace = gui.Image(source="Cards Pack/Deck/Spades 1.png", size=(100, 150), key="-MENU-ACE-", pad=(5,30))
menu_jack = gui.Image(source="Cards Pack/Deck/Spades 11.png", size=(100, 150), key="-MENU-JACK-", pad=(5,30))
hit_button = gui.Button("HIT", key="-HIT-", size=(10, 1), pad=(20, 10), visible=False)
hold_button = gui.Button("HOLD", key="-HOLD-", size=(10, 1), pad=(20, 10), visible=False)
play_again_button = gui.Button("PLAY AGAIN", key="-PLAY-AGAIN-BUTTON-", size=(10, 1), pad=(20, 10), visible=False)
game_title_image_start = gui.Image(source="Cards Pack/BlackJack Logo.png", size=(196, 50), key="-GAME-TITLE-IMG-START-", pad=(0,0))
player_score = gui.Text(str(f"Your Score:\n\n        {START_SCORE}"), text_color="white", key="-PLAYER-SCORE-", pad=(0,90))
npc_score = gui.Text(str(f"Opponent Score:\n\n            {START_SCORE}"), text_color="white", key="-NPC-SCORE-", pad=(0,80))

# Create window and manage layout as a graph.

scoreboard_col = gui.Column([[game_title_image_start], [npc_score], [player_score], [play_button]],
							size=(198, 625),
							element_justification="center",
							key="-SCOREBOARD-",
							visible=False,
							pad=(10,0))

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

	[[gui.Push(), gui.Column([[hit_button, hold_button, play_again_button]]), gui.Push()]],

	[gui.Push(), gui.Column([[menu_jack, menu_ace]], key="-MENU-CARDS-", visible=True, element_justification="center"),
	 gui.Push()],

	[gui.Push(), gui.Column([[blackjack_button]]), gui.Push()],

	[[gui.VPush()]],
]

window = gui.Window("Blackjack", layout, size=(1000, 750), finalize=True, location=(100, 100))
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
print(DECK)
while True:
	event, values = window.read()
	print(event, values)

	if event == gui.WINDOW_CLOSED or event == '-EXIT-':
		break
	elif event == '-QUIT-':
		break

	elif event == '-BLACKJACK-':
		# Display game
		window["-GAME-TITLE-IMG-"].update(visible=False)
		window["-MENU-CARDS-"].update(visible=False)
		window["-BLACKJACK-"].update(visible=False)
		window["-PLAYER-SCORE-"].update(visible=True)
		window["-NPC-SCORE-"].update(visible=True)
		window["-SCOREBOARD-"].update(visible=True)
		window["-GRAPH-"].update(visible=True)

	elif event == '-PLAY-':
		window["-HIT-"].update(visible=True)
		window["-HOLD-"].update(visible=True)
		window["-PLAY-"].update(visible=False)

		for i in range(2):
			player_cards.append(get_card(DECK))
			npc_cards.append(get_card(DECK))

		print(f"Player Cards: {player_cards}")
		print(f"NPC Cards: {npc_cards}")

		player_score = get_score(player_cards)
		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))

		npc_score = npc_cards[1]['value']
		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))

		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i]['dest'], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20
			PLAYER_Y += 20

		graph.DrawImage("Cards Pack/card_colors/Back Blue 1.png", location=(NPC_X, NPC_Y))
		graph.DrawImage(npc_cards[1]['dest'], location=(NPC_X + 20, NPC_Y + 20))

	elif event == '-HIT-':
		player_cards.append(get_card(DECK))
		player_score = get_score(player_cards)
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
		window["-HIT-"].update(visible=False)
		window["-HOLD-"].update(visible=False)
		window["-PLAY-AGAIN-BUTTON-"].update(visible=True)

		graph.erase()

		print(npc_cards)
		npc_score = get_score(npc_cards)
		print(f"NPC Score: {npc_score}")


		if npc_score < 21 and 21 - npc_score > 4:
			npc_cards.append(get_card(DECK))
		elif npc_score < 21 and 21 - npc_score <= 4:
			pass

		npc_score = get_score(npc_cards)
		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))

		print(f"Player Cards: {player_cards}")
		print(f"NPC Cards: {npc_cards}")

		PLAYER_X = -40
		PLAYER_Y = -60
		NPC_X = -50
		NPC_Y = 150
		for i in range(len(player_cards)):
			graph.DrawImage(player_cards[i]['dest'], location=(PLAYER_X, PLAYER_Y))
			PLAYER_X += 20
			PLAYER_Y += 20
		for i in range(len(npc_cards)):
			graph.DrawImage(npc_cards[i]['dest'], location=(NPC_X, NPC_Y))
			NPC_X += 20
			NPC_Y += 20

		declare_result(player_score, npc_score)

	elif event == '-PLAY-AGAIN-BUTTON-':
		window["-PLAY-"].update(visible=True)
		window["-PLAY-AGAIN-BUTTON-"].update(visible=False)
		graph.erase()
		DECK = extract_dest_and_values(DECK_LIST)
		player_cards = []
		player_score = 0
		npc_cards = []
		npc_score = 0
		PLAYER_X = -40
		PLAYER_Y = -60
		NPC_X = -50
		NPC_Y = 150

		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))
		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))

window.close()