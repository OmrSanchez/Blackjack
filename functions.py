import random
from FreeSimpleGUI import popup_ok

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
	result = ["win", "lose", "draw", "no winner", "blackjack"]
	if player_score == computer_score and (player_score < 21 and computer_score < 21):
		return result[2]
	elif player_score <= 21 < computer_score:
		return result[0]
	elif player_score > 21:
		return result[1]
	elif player_score > 21 and computer_score > 21:
		return result[3]
	elif player_score == 21 and computer_score != 21:
		return result[0]
	elif computer_score < player_score <= 21:
		return result[0]
	elif computer_score < player_score <= 21:
		return result[0]
	elif player_score < computer_score <= 21:
		return result[1]
	else:
		return result[3]

def declare_result(player_score, computer_score):
	match decide_result(player_score, computer_score):
		case "win":
			popup_ok(
			title = "Blackjack - Win",
			auto_close = False,
			non_blocking = False,
			no_titlebar = False,
			grab_anywhere = False,
			keep_on_top = True,
			image = "Popup Images/win.png",
			modal = True
			)
		case "lose":
			popup_ok(
				title="Blackjack - Win",
				auto_close=False,
				non_blocking=False,
				no_titlebar=False,
				grab_anywhere=False,
				keep_on_top=True,
				image="Popup Images/lose.png",
				modal=True
			)
		case "draw":
			popup_ok(
				title="Blackjack - Win",
				auto_close=False,
				non_blocking=False,
				no_titlebar=False,
				grab_anywhere=False,
				keep_on_top=True,
				image="Popup Images/no_winner.png",
				modal=True
			)
		case "no winner":
			popup_ok(
				title="Blackjack - Win",
				auto_close=False,
				non_blocking=False,
				no_titlebar=False,
				grab_anywhere=False,
				keep_on_top=True,
				image="Popup Images/no_winner.png",
				modal=True
			)
		case "blackjack":
			popup_ok(
				title="Blackjack - Win",
				auto_close=False,
				non_blocking=False,
				no_titlebar=False,
				grab_anywhere=False,
				keep_on_top=True,
				image="Popup Images/blackjack.png",
				modal=True
			)

def check_ace(card_value):
	if card_value == 11 or card_value == 1:
		return True

def npc_hit(card_value_list, deck_dest_list):
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





def remove_cards(card_list, deck):
	for card in card_list:
		deck.remove(card)

def remove_next_card(card_list, deck):
	for i in range(1):
		deck.remove(card_list[-1])
