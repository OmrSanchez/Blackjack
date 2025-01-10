import random
import art
import functions

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
DECK = []
functions.create_deck(CARDS, DECK)

blackjack = True
while True:
	player_cards = []
	computer_cards = []
	play = input("Do you want to play a game of Blackjack? (yes/no)")
	if play == 'y':
		print(art.logo)
		ace = [1, 11]
		for i in range(2):
			player_cards.append(random.choice(DECK))
			computer_cards.append(random.choice(DECK))
		functions.check_A_init(player_cards)
		functions.check_A_init(computer_cards)
		player_score = sum(player_cards)
		print(
			f"    Your cards: {player_cards}, current score: {player_score}\n    Computer's first "
			f"card: {computer_cards[0]}")
		hit = True
		while hit:
			hit_choice = input("Type 'y' to get another card, type 'n' to pass: ")
			if hit_choice == 'y':
				player_cards.append(random.choice(DECK))
				functions.check_A_hit(player_cards)
				player_score = sum(player_cards)
				print(
					f"Your cards: {player_cards}, current score:{player_score}\n    Computer's first"
					f" card: {computer_cards[0]}")
			elif hit_choice == 'n':
				computer_score = sum(computer_cards)
				for count in range(3):
					if computer_score < 21 and 21 - computer_score > 4:
						computer_cards.append(random.choice(DECK))
						functions.check_A_hit(computer_cards)
						computer_score = sum(computer_cards)
				hit = False
		print(f"    Your final hand: {player_cards}, final score: {player_score}")
		print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
		functions.decide_winner(player_score, computer_score)
	else:
		print("Goodbye.")
		blackjack = False