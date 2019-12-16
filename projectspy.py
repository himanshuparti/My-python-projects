import random


def player_choice():
	choice=''
	while choice!='O' and choice!='X':
		choice=input("Player 1, Pick X or O")
	if choice=='X':
		return('X','O')
	else:
		return('O','X')

def place_choice(board,choice,position):
	board[position]=choice

def player_input(board):
    pos =0
    while pos not in range(1,10) or not check_space(board,pos):
    	pos=int(input("Enter your position bw 1-9"))
    return pos


def draw_board(board):
	print('\n')
	print('\t\t\t',board[1],'|',board[2],'|',board[3])
	print('\t\t\t','------------')
	print('\t\t\t',board[4],'|',board[5],'|',board[6])
	print('\t\t\t','------------')
	print('\t\t\t',board[7],'|',board[8],'|',board[9])

def check_space(board,position):
    return board[position]==' '

def board_full(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

def winner(board,choice):
    return ((board[1]==board[2]==board[3]==choice) or 
    (board[4]==board[5]==board[6]==choice) or
    (board[7]==board[8]==board[9]==choice) or
    (board[1]==board[4]==board[7]==choice) or
    (board[2]==board[5]==board[8]==choice) or
    (board[3]==board[6]==board[9]==choice) or
    (board[2]==board[5]==board[9]==choice) or
    (board[7]==board[5]==board[3]==choice))
        
    
def turn():
	flip=random.randint(0,1)
	if flip==0:
		return "Player 1"
	else:
		return "Player 2"

def play_again():
	choose=input("Do you want to play again ? y or n").lower()
	return choose


print("\t \t \tWelcome to the game !\t \t \t")
print('\n'*3)
while True:
	board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	player1_choice,player2_choice=player_choice()
	turns= turn()
	print(turns + ' will go 1st')
	game_on=input("You want to continue ? y or n").lower()
	while game_on=='y':
		if turns=='Player 1':
			draw_board(board)
			pos=player_input(board)
			place_choice(board,player1_choice,pos)
			if winner(board,player1_choice):
				draw_board(board)
				print('Hurrah! Player 1 has won')
				game_on='n'
			else:
				if board_full(board):
					draw_board(board)
					print('Its a tie!')
					game_on='n'
				else:
					print("Player 2's turn")
					turns='Player 2'
		if turns=='Player 2':
			draw_board(board)
			pos=player_input(board)
			place_choice(board,player2_choice,pos)
			if winner(board,player2_choice):
				draw_board(board)
				print('Hurrah! Player 2 has won')
				game_on='n'
			else:
				if board_full(board):
					draw_board(board)
					print('Its a tie!')
					game_on='n'
				else:
					print("Player 1's turn")
					turns='Player 1'
	pa= play_again()
	if pa=='y':
		continue
	else:
		break


                    
