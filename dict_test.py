import cards_dict

print(cards_dict.deck)

for i in range(52):
	print(cards_dict.deck[i][0])
	print(cards_dict.deck[i][0].get("value"))