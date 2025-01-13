import random
from FreeSimpleGUI import popup_ok

def extract_dest_and_values(deck):
	deck_dict = [deck[i][0] for i in range(52)]
	return deck_dict

def check_ace(c_value):
	if c_value == 1 or c_value == 11:
		return True

def check_ace_list_card_values(list_of_card_values):
	ace_local = [1, 11]
	for card_val_local in list_of_card_values:
		if check_ace(card_val_local):
			card_index_local = list_of_card_values.index(card_val_local)
			list_of_card_values.remove(card_val_local)
			score_without_ace = sum(list_of_card_values)

			if score_without_ace + 11 <= 21:
				list_of_card_values.insert(card_index_local, ace_local[1])
				print(f"Ace = 11: {list_of_card_values}")
				return list_of_card_values
			elif score_without_ace + 11 > 21:
				list_of_card_values.insert(card_index_local, ace_local[0])
				print(f"Ace = 1: {list_of_card_values}")
				return list_of_card_values
		else:
			print(f"No Ace: {list_of_card_values}")
			return list_of_card_values



def get_card(deck):
	selected_card = random.choice(deck)
	deck.remove(selected_card)
	return selected_card

def get_card_value(cards):
	card_value_list = [cards[val]['value'] for val in range(len(cards))]
	print(f"Cards Values: {card_value_list}")
	return card_value_list

def get_card_dest(cards):
	dest = [cards[des]['dest'] for des in range(len(cards))]
	return dest

def get_score(cards):
	list_of_card_values = get_card_value(cards)
	score = sum(check_ace_list_card_values(list_of_card_values))
	return score





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
