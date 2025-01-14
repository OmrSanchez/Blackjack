def draw_graph_border(graph):
	graph.draw_line((-250, 250), (250, 250), color="black", width=8)
	graph.draw_line((-250, -250), (250, -250), color="black", width=8)
	graph.draw_line((-250, 250), (-250, -250), color="black", width=8)
	graph.draw_line((250, -250), (250, 250), color="black", width=8)
	graph.draw_line((-146, 14), (247, 14), color="white", width=4)
	graph.draw_line((-146, -247), (-146, 247), color="white", width=4)
	graph.draw_text(
		"Discard",
		(-200, 220),
		color = "white",
		font = "Ariel",
		text_location='center'
	)
	graph.draw_text(
		"Your Hand",
		(195, -220),
		color="white",
		font="Ariel",
		text_location='center'
	)
	graph.draw_text(
		"Opponent Hand",
		(190, 220),
		color="white",
		font="Ariel",
		text_location='center'
	)

def draw_win(graph):
	win_image = graph.DrawImage('Popup Images/win.png', location=(-120, 110))
	return win_image

def draw_lose(graph):
	lost_image = graph.DrawImage('Popup Images/lose.png', location=(-120, 70))
	return lost_image

def draw_draw(graph):
	draw_image = graph.DrawImage('Popup Images/draw.png', location=(-120, 70))
	return draw_image

def draw_no_winner(graph):
	no_winner_image = graph.DrawImage('Popup Images/no_winner.png', location=(-120, 80))
	return no_winner_image

def draw_blackjack(graph):
	blackjack_image = graph.DrawImage('Popup Images/blackjack.png', location=(-120, 70))
	return blackjack_image

def draw_player_hand(cards, graph):
	X = -40
	Y = -80
	for i in range(len(cards)):
		graph.DrawImage(cards[i]['dest'], location=(X, Y))
		X += 20

def draw_npc_hand(cards, graph):
	X = -50
	Y = 175
	for i in range(len(cards)):
		graph.DrawImage(cards[i]['dest'], location=(X, Y))
		X += 20

def draw_discard(discard, X, Y, graph):
	for i in range(len(discard)):
		graph.DrawImage(discard[i]['dest'], location=(X, Y))
		Y += 25