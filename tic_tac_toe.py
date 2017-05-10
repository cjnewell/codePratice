#==============================================================================#
# Name: Christopher Newell
# Class: Computers and Society
# Section: 1
# Due Date: October 20, 2015
#==============================================================================#

#==============================================================================#
#   Function Definitions                                                       #
#==============================================================================#

#This function gets the player name and returns the name
def getPlayerName( playerNum ): 
	playerName = input("Player " + str(playerNum) + 
													" please enter your name: ")
	return playerName;

#This function gets and checks a move to see if it is a valid move
def getPlayerMove( playerName, board ):
	validMove = False
	move = []
	while not(validMove):
		playerMove = input(playerName + 
   						     " please enter in your move seperated by spaces: ")
		move = playerMove.split(' ')
		#Decriment each value since we count from zero
		move[0] = int(move[0]) - 1
		move[1] = int(move[1]) - 1
		validMove = checkMoveBounds(move)
		#The move is in bounds checking to see if the spot is taken on the board
		if(validMove):
			#Checks to see if the spot on the board is taken
			if(	board[ int(move[0]) ][ int(move[1]) ] != 0):
				validMove = False
				print("Spot is already taken! Please choose another!!")
	return move

#This function checks to see if a player has won the game
def checkWin(board):
	gameWon = checkWinRowAndCol(board)

	topLeftDiagChar = board[0][0]
	topRightDiagChar = board[0][2]
	#Checks diagonals
	if ((topLeftDiagChar == board[1][1] and topLeftDiagChar == board[2][2]) 
													 and topLeftDiagChar != 0 ):
		gameWon = True
	if( (topRightDiagChar == board[1][1] and topRightDiagChar == board[2][0]) 
													 and topRightDiagChar != 0):
		gameWon = True

	return gameWon

#This helper function checks to see if the move is within bounds
def checkMoveBounds(move):
	validMove = False
	if( move[0] > 2) :
		print("Invalid move please try a row within 1-3")
	elif( move[1] > 2) : 
		print("Invalid move please try a col within 1-3")
	else:
		validMove = True
	return validMove

#This helper function switches the token based on which move it is
def chooseToken(moveCount):
	token = ""	
	if(moveCount % 2 == 1):
		token = "X"
	else:
		token = "O"
	return token

#This helper function checks both the rows and columns for a winner
def checkWinRowAndCol(board):
	gameWon = False
	for x in range(0,3):
		firstRowChar = board[x][0]
		#Checks rows for a win
		if( (firstRowChar == board[x][1] and firstRowChar == board[x][2]) and 
															 firstRowChar != 0):
			gameWon = True
		#Checks columns for a win
		firstColChar = board[0][x]
		if( (firstColChar == board[1][x] and firstColChar == board[2][x]) 
														 and firstColChar != 0):
			gameWon = True
	return gameWon

#This function prints out the board to the screen
def printBoard(board):
	emptyLine  = "   |   |      "
	filledLine = "-----------"
	tokenLine  = " {} | {} | {} "

	for x in range(0,3):
		print(emptyLine)
		print(tokenLine.format(board[x][0], board[x][1], board[x][2]))
		print(emptyLine)
		if(x < 2):
			print(filledLine)

#This function prints out the winning player
def printWinner(playerName):
	print("Congratulations " + playerName + " you have won!")
	
	
#==============================================================================#
#   The application starts here                                                #
#==============================================================================#
welcomeMessage = "Welcome To Tic Tac Toe!"
playerOne = ""
playerTwo = ""
playAgain = ''
moveCount = 1
gameWon = False
board = [[0 for x in range(3)] for x in range(3)]
#Game Begins Here
print(welcomeMessage)
playerOne = getPlayerName( playerNum = 1)
playerTwo = getPlayerName( playerNum = 2)
print("The two players are: " + playerOne + " and " + playerTwo)
playAgain = input("Do you wish to play the game? (y/n) ")

#The main game loop starts here
while( playAgain == 'y'): 
	playerMove = []
	token = chooseToken(moveCount)
	
	#Prints out the board after the first turn
	if(moveCount > 1):
		printBoard(board)
	#Asks the appropriate player to make a move
	if(moveCount % 2 == 1):
		playerMove = getPlayerMove(playerOne, board)
	else:
		playerMove = getPlayerMove(playerTwo, board)	
	
	#Puts the token into the board
	board[int(playerMove[0])][int(playerMove[1])] = token
	#Only checks for a winner after the 5th move has been made
	if(moveCount >= 4):
		gameWon = checkWin(board)
	#If someone won the game this determines if the game is won by the first or
	#second player. It also checks for a cats game. Furthermore; since the game 
	#is over the players are asked if they want to play again
	if(gameWon):
		printBoard(board)
		if(moveCount % 2 == 1):
			printWinner(playerOne)
		else:
			printWinner(playerTwo)
		playAgain = input("Do you wish to play again? (y/n) ")
	elif(moveCount == 9):
		print("Cats Game!")
		playAgain = input("Do you wish to play again? (y/n) ")
	moveCount = moveCount + 1	
