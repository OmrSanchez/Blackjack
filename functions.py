import random

def extract_dest_and_values(deck_list):
	deck_dest_list = []
	values_list_local = []
	for cards in deck_list:
		deck_dest_list.append(cards[0]["dest"])
		values_list_local.append(cards[0]["value"])
	return deck_dest_list, values_list_local

def select_cards(deck_dest_list):
	card_select_local = []
	for i in range(2):
		card_select_local.append(random.choice(deck_dest_list))
	return card_select_local

#Grab index of selected cards
def store_index(card_list, deck_dest_list_local):
	index_list = []
	for item in range(len(card_list)):
		index_list.append(deck_dest_list_local.index(card_list[item]))
	return index_list

def check_if_blackjack(score):
	if score == 21:
		return True

def check_if_bust(player_score, npc_score):
	if player_score > 21 or npc_score > 21:
		return True
	return False

def decide_result(player_score, computer_score):
	result = ["win", "lose", "draw", "no winner"]
	if player_score == computer_score and (player_score < 21 and computer_score < 21):
		return result[2]
	elif player_score <= 21 < computer_score:
		return result[0]
	elif player_score > 21 >= computer_score:
		return result[1]
	elif player_score > 21 and computer_score > 21:
		return result[3]
	elif player_score == 21 and computer_score != 21:
		return result[0]
	elif computer_score < player_score <= 21:
		return result[0]
	elif player_score > computer_score and player_score <= 21:
		return result[0]
	else:
		return result[3]

# popup_ok(
# 				keep_on_top = True,
# 				title = "YOU LOSE!",
# 				image="Popup Images/lose.png",
# 				no_titlebar=False,
# 			)
#
# if player_lose(player_score=current_sum):
# 	popup_ok(
# 		keep_on_top = True,
# 		title = "YOU LOSE!",
# 		image="Popup Images/lose.png",
# 		no_titlebar=False,
# 	)
# 	window["-GRAPH-"].erase()
# 	window["-PLAYER-CONTROLS-"].update(visible=False)
# 	window["-PLAY-AGAIN-"].update(visible=True)
# 	current_sum = 0
# 	current_score.update(current_sum)

def check_ace(card_value):
	if card_value == 11 or card_value == 1:
		return True

def npc_hit(card_value_list, deck_dest_list, ):
	npc_cards = []
	npc_index = []
	npc_card_values_list = []
	npc_score_number = 0
	for second_count in range(4):
		if npc_score_number < 21 and 21 - npc_score_number > 4:
			npc_cards.append(select_cards(deck_dest_list)[0])
			npc_index = store_index(npc_cards, deck_dest_list)
			npc_card_values_list = [card_value_list[i] for i in npc_index]
			for i in npc_card_values_list:
				if check_ace(i):
					if (sum(npc_card_values_list) - i) + 11 > 21:
						npc_card_values_list.remove(i)
						npc_card_values_list.append(1)
					elif (sum(npc_card_values_list) < 21) and (sum(npc_card_values_list) - i) + 11 <= 21:
						npc_card_values_list.remove(i)
						npc_card_values_list.append(11)
			npc_score_number = sum(npc_card_values_list)
	return npc_cards, npc_score_number, npc_index, npc_card_values_list


# (sum(npc_card_values_list) < 21) and
