import random
from art import logo


def create_deck():
	for i in range(4):
		for c in cards:
			deck.append(c)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = []
create_deck()


def decide_winner(player_score, computer_score):
	if player_score == computer_score and (
			player_score < 21 and computer_score < 21):
		print("Draw")
	elif player_score <= 21 and computer_score > 21:
		print("Opponent went over. You win.")
	elif player_score > 21 and computer_score <= 21:
		print("You went over. You Lose!")
	elif player_score > 21 and computer_score > 21:
		print("No Winner!")
	elif player_score == 21 and computer_score != 21:
		print("Blackjack! You win!")
	elif player_score > computer_score and player_score <= 21:
		print("You were closer! You Win!")
	else:
		print("You Lose!")


def check_A_init(cards):
	for number in range(0, 1):
		if cards[number] == 11:
			cards[number] = (random.choice(ace))


def check_A_hit(cards):
	for card in cards:
		if cards[len(cards) - 1] == 11:
			cards[len(cards) - 1] = (random.choice(ace))


blackjack = True
while blackjack:
	player_cards = []
	computer_cards = []
	play = input("Do you want to play a game of Blackjack? ")
	if play == 'y':
		print(logo)
		ace = [1, 11]
		for i in range(2):
			player_cards.append(random.choice(deck))
			computer_cards.append(random.choice(deck))
		check_A_init(player_cards)
		check_A_init(computer_cards)
		player_score = sum(player_cards)
		print(
			f"    Your cards: {player_cards}, current score: {player_score}\n    Computer's first card: {computer_cards[0]}")
		hit = True
		while hit:
			hit_choice = input("Type 'y' to get another card, type 'n' to pass: ")
			if hit_choice == 'y':
				player_cards.append(random.choice(deck))
				check_A_hit(player_cards)
				player_score = sum(player_cards)
				print(
					f"Your cards: {player_cards}, current score:{player_score}\n    Computer's first card: {computer_cards[0]}")
			elif hit_choice == 'n':
				computer_score = sum(computer_cards)
				for count in range(3):
					if computer_score < 21 and 21 - computer_score > 4:
						computer_cards.append(random.choice(deck))
						check_A_hit(computer_cards)
						computer_score = sum(computer_cards)
				hit = False
		print(f"    Your final hand: {player_cards}, final score: {player_score}")
		print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
		decide_winner(player_score, computer_score)
	else:
		print("Goodbye.")
		blackjack = False