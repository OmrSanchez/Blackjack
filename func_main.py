import random

# def extract_dest_and_values(deck):
# 	deck_dict = []
# 	for deck_count in range(6):
# 		for card in range(52):
# 			deck_dict.append(deck[card][0])
# 	print(f"Deck length: {len(deck_dict)}")
# 	print(deck_dict)
# 	return deck_dict


def extract_dest_and_values(deck, number_of_decks):
	deck_dict = []
	for deck_count in range(number_of_decks):
		for card in range(52):
			deck_dict.append(deck[card][0])
	print(f"Deck length: {len(deck_dict)}")
	print(deck_dict)
	return deck_dict

def get_card(deck):
	selected_card = random.choice(deck)
	deck.remove(selected_card)
	return selected_card

def get_score(cards):
	list_of_card_values = get_card_value(cards)
	score = sum(check_ace_list_card_values(list_of_card_values))
	return score

def get_card_value(cards):
	card_value_list = [cards[val]['value'] for val in range(len(cards))]
	print(f"Cards Values: {card_value_list}")
	return card_value_list

def get_card_dest(cards):
	dest = [cards[des]['dest'] for des in range(len(cards))]
	return dest

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

			if score_without_ace + 11 <= 21 and (score_without_ace + 11) > (score_without_ace + 1):
				list_of_card_values.insert(card_index_local, ace_local[1])
				print(f"Ace = 11: {list_of_card_values}")
				return list_of_card_values
			elif score_without_ace + 11 <= 21:
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


