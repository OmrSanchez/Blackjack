import FreeSimpleGUI as gui
import cards_dict
from func_main import *
from func_outcome import *
from menu_items import menu_def
from settings_func import change_theme

NUMBER_OF_DECKS = 3
DECK_LIST = cards_dict.deck
DECK = extract_dest_and_values(DECK_LIST, NUMBER_OF_DECKS)
theme = gui.theme("DarkGrey12")
GRAPH_COLOR = "green"
START_SCORE = 0
gui.set_options(font="Arial, 18", element_padding=(0,0), text_color="gold", border_width=0)

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

scoreboard_col = gui.Column([[game_title_image_start], [npc_score], [player_score], [play_button]],
							size=(198, 625),
							element_justification="center",
							key="-SCOREBOARD-",
							visible=False,
							pad=(10,0))

blackjack_menu = gui.MenuBar(menu_def, font='Ariel, 10')


layout = [
	[blackjack_menu],
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

window = gui.Window("Blackjack", layout, size=(1050, 750), finalize=True, location=(350,150))
graph = window["-GRAPH-"]
draw_graph_border(graph)


DISCARD_X = -230
DISCARD_Y = -50
player_score = 0
player_cards = []
npc_score = 0
npc_cards = []
discard_pile = []

while True:
	event, values = window.read()
	print(event, values)
	user_theme = gui.theme_list()
	print(event[:12])

	if event == gui.WINDOW_CLOSED or event == '-EXIT-':
		break
	elif event == '-QUIT-':
		break

	elif event == "Change Theme":
		theme = gui.theme(change_theme())

	elif (event == '1' or event == '2' or event == '3' or event == '4' or event == '5' or event
		  == '6'):
		NUMBER_OF_DECKS = int(event)
		DECK_LIST = cards_dict.deck
		DECK = extract_dest_and_values(DECK_LIST, NUMBER_OF_DECKS)

	elif event == '-BLACKJACK-':
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

		DECK = extract_dest_and_values(DECK_LIST, NUMBER_OF_DECKS)

		for i in range(2):
			discard_pile.append(get_card(DECK))
			player_cards.append(get_card(DECK))
			npc_cards.append(get_card(DECK))

		player_score = get_score(player_cards)
		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))

		draw_player_hand(player_cards, graph)

		npc_score = get_score(npc_cards)
		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           "
										 f"{npc_score - npc_cards[0]['value']}"))
		NPC_X = -50
		NPC_Y = 175
		graph.DrawImage("Cards Pack/back_of_cards/Back Red 1.png", location=(NPC_X, NPC_Y))
		graph.DrawImage(npc_cards[1]['dest'], location=(NPC_X + 20, NPC_Y))

		for i in range(len(discard_pile)):
			graph.DrawImage("Cards Pack/back_of_cards/Back Red 1.png", location=(DISCARD_X,
																			   DISCARD_Y))
			DISCARD_Y += 25

		draw_graph_border(graph)

	elif event == '-HIT-':
		discard_pile.append(get_card(DECK))

		player_cards.append(get_card(DECK))
		player_score = get_score(player_cards)
		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))

		graph.erase()

		DISCARD_X = -230
		DISCARD_Y = -50
		for i in range(len(discard_pile)):
			graph.DrawImage("Cards Pack/back_of_cards/Back Red 1.png", location=(DISCARD_X, DISCARD_Y))
			DISCARD_Y += 25

		draw_player_hand(player_cards, graph)

		graph.DrawImage("Cards Pack/back_of_cards/Back Red 1.png", location=(NPC_X, NPC_Y))
		graph.DrawImage(npc_cards[1]['dest'], location=(NPC_X + 20, NPC_Y))
		draw_graph_border(graph)

		if player_score > 21:
			window["-HIT-"].update(visible=False)
			window["-HOLD-"].update(visible=False)
			window["-PLAY-AGAIN-BUTTON-"].update(visible=True)

			for hit in range(3):
				if npc_score < 21 and 21 - npc_score > 4:
					npc_cards.append(get_card(DECK))
					npc_score = get_score(npc_cards)

			graph.erase()

			window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))

			DISCARD_X = -230
			DISCARD_Y = -50
			draw_discard(discard_pile, DISCARD_X, DISCARD_Y, graph)

			draw_player_hand(player_cards, graph)
			draw_npc_hand(npc_cards, graph)
			draw_graph_border(graph)
			declare_result(player_score, npc_score, graph)

	elif event == '-HOLD-':
		window["-HIT-"].update(visible=False)
		window["-HOLD-"].update(visible=False)
		window["-PLAY-AGAIN-BUTTON-"].update(visible=True)

		for hit in range(3):
			if npc_score < 21 and 21 - npc_score > 4:
				npc_cards.append(get_card(DECK))
				npc_score = get_score(npc_cards)

		graph.erase()

		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))

		DISCARD_X = -230
		DISCARD_Y = -50
		draw_discard(discard_pile, DISCARD_X, DISCARD_Y, graph)

		draw_player_hand(player_cards, graph)
		draw_npc_hand(npc_cards, graph)
		draw_graph_border(graph)
		declare_result(player_score, npc_score, graph)

	elif event == '-PLAY-AGAIN-BUTTON-':
		window["-PLAY-"].update(visible=True)
		window["-PLAY-AGAIN-BUTTON-"].update(visible=False)
		graph.erase()
		DECK = extract_dest_and_values(DECK_LIST, NUMBER_OF_DECKS)
		# DECK = extract_dest_and_values(DECK_LIST)
		print(len(DECK))
		player_cards = []
		player_score = 0
		npc_cards = []
		npc_score = 0
		discard_pile = []
		PLAYER_X = -40
		PLAYER_Y = -80
		NPC_X = -50
		NPC_Y = 175
		DISCARD_X = -230
		DISCARD_Y = -50

		window["-PLAYER-SCORE-"].update(str(f"Your Score:\n\n        {player_score}"))
		window["-NPC-SCORE-"].update(str(f"Opponent Score:\n\n           {npc_score}"))
		draw_graph_border(graph)

window.close()