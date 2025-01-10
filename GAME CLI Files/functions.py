import random
import pathlib as Path

def create_deck(cards, deck):
	for i in range(4):
		for c in cards:
			deck.append(c)


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
