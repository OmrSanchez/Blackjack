from func_draw import *

def decide_result(player_score, computer_score):
	result = ["win", "lose", "draw", "no winner", "blackjack"]
	if player_score == computer_score and (player_score < 21 and computer_score < 21):
		return result[2]
	elif player_score > 21 and computer_score > 21:
		return result[3]
	elif player_score == 21 and computer_score != 21:
		return result[4]
	elif computer_score < player_score <= 21:
		return result[0]
	elif player_score < computer_score <= 21:
		return result[1]
	elif player_score <= 21 < computer_score:
		return result[0]
	elif computer_score <= 21 < player_score:
		return result[1]
	elif (player_score and computer_score) == 21:
		return result[2]

def declare_result(player_score, computer_score, graph):
	match decide_result(player_score, computer_score):
		case "win":
			draw_win(graph)
		case "lose":
			draw_lose(graph)
		case "draw":
			draw_draw(graph)
		case "no winner":
			draw_no_winner(graph)
		case "blackjack":
			draw_blackjack(graph)

