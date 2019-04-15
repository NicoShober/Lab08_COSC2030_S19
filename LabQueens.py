global N
N = float(input("what is the dimensions for the square chess board")

def printSolution(board):
	print('')
	for i in range(N):
		for j in range(N):
			print (board[i][j], end=' ')
		print('')
		
def verifyDiagonal(board, row, col):
	j = col
	i = row
	while (j>=0 and i>=0):
		if board[i][j] == 1:
			return False
		i-=1
		j-=1
		
	j = col
	i = row
	while (i<N and j>=0):
		if board[i][j] == 1:
			return False
		j-=1
		i+=1
		
def isSafe(board, row, col):
	j = col
	i = row
	qCount=0
	for j in range(N):
		if board[row][j] == 1
			qCount += 1
		j+=1
	if qCount == 2
		return True
	return False	
	#counts how many queens are in a row and if its 1 or 0 it ends false, if its 2 it ends true

	DiagonalCheck = verifyDiagonal(board, row, col)

	if DiagonalCheck == False:
		return False
	return True
	
def solveNQUtil(board, col):
	if col >= N:
		return True
		
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQUtil(board, col + 1) == True:
				return True
			board[i][col] = 0
	return False
	
def solveNQ():
	board = [ 	[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0]
			]
	if solveNQUtil(board, 0) == True:
		printSolution(board)
solveNQ()