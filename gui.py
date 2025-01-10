import FreeSimpleGUI as gui
from FreeSimpleGUI import easy_print
import cards_dict
import random

# Game layout
game_title_image = gui.Image("Cards Pack/BlackJack Logo.png", size=(220,45), key="title_image")
play_button = gui.Button("PLAY", key="play", auto_size_button=True)
exit_button = gui.Button("EXIT", key="exit", auto_size_button=True)
menu_card_ace = gui.Image("Cards Pack/Deck/Spades 1.png", key="ace")
menu_card_king = gui.Image("Cards Pack/Deck/Diamond 12.png", key="king")

#Hidden Deck
# Pull deck of cards
DECK_LIST = cards_dict.card_values_dict
print(DECK_LIST)
print(DECK_LIST[1][0]['dest'])

DECK_DEST = []
for i in range(52):
	for cards in DECK_LIST:
		DECK_DEST.append(cards[0]["dest"])
print(DECK_DEST)
#
# card_png_list = []
# for dest in DECK_DEST:
# 	card_image = gui.Image(source=dest, visible=False)
# 	card_png_list.append(card_image)

# Player Controls
hit_button = gui.Button("HIT", key="hit", visible=False)
hold_button = gui.Button("HOLD", key="hold", visible=False)
quit_button = gui.Button("QUIT", key="quit", visible=False)

#Player Cards


# Create window and manage layout.
row1 = [gui.Push(), gui.pin(gui.vtop(game_title_image)), gui.Push()]
row2 = [gui.Push(), menu_card_ace, menu_card_king, gui.Push()]
row3 = [gui.Push(), play_button, exit_button, gui.Push()]
# deck_row = [gui.Push(), gui.pin(card_png_list),gui.Push()]
row4 = [gui.Push(), gui.pin(hit_button), gui.pin(hold_button), gui.Push()]
row6 = [gui.Push(), gui.pin(quit_button), gui.Push()]

layout = [[gui.Text('*'*100)],
		  row1,
		  [gui.Text('*' * 100)],
		  row2,
		  row3,
		  row4,
		  # deck_row,
		  row6,
		  [gui.Text('*'*100)]]

window = gui.Window("Blackjack", layout)



#Display game window and interact with the game
while True:
	event, values = window.read()
	player_cards = []
	computer_cards = []
	match event:
		case 'play':
			#Display main menu images
			menu_card_ace(visible=False)
			menu_card_king(visible=False)

			# Display main menu buttons
			play_button(visible=False)
			exit_button(visible=False)

			#Display player controls
			hit_button(visible=True)
			hold_button(visible=True)
			quit_button(visible=True)

			# Assign player cards
			# for card in range(2):
			# 	player_cards.append(random.choice(DECK))
			# easy_print(f"PLAYER: {player_cards}")


		case 'exit':
			break

window.close()