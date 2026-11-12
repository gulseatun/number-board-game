import sys

#Checking if the row and column numbers are within the range of the board
def checking_choice(row_choice_index, column_choice_index, board):

    if 0<=row_choice_index<=len(board)-1 and 0<=column_choice_index<=len(board[0])-1:
        return True
    
    else: 
        return False

#Checking and removing cells that have the same value with chosen element recursively
def controlling_choice(row, column, board, choice):

    global remove_number
    last_column_index = len(board[0])-1
    last_row_index = len(board)-1

    if row>0 and board[row-1][column] != " ":  #Checking for upward
        if board[row-1][column] == choice:
            board[row-1][column] = " "
            remove_number += 1
            controlling_choice(row-1, column, board, choice)

    if row<last_row_index and board[row+1][column] != " ": #Checking for downward
        if board[row+1][column] == choice:
            board[row+1][column] = " "
            remove_number += 1
            controlling_choice(row+1, column, board, choice)
           
    if column>0 and board[row][column-1] != " ": #Checking for left
        if board[row][column-1] == choice:
            board[row][column-1] = " "
            remove_number += 1
            controlling_choice(row, column-1, board, choice)
            
    if column<last_column_index and board[row][column+1] != " ": #Checking for right
        if board[row][column+1] == choice:
            board[row][column+1] = " "
            remove_number += 1
            controlling_choice(row, column+1, board, choice)
            
#Moving cells downwards to fill empty spaces
def falling(board):

    for m in range(len(board)-1):    
        for i in range(len(board)-1):
          
            index = -1
            spaces_index = []
            for k in board[len(board)-1-i]:
                index += 1
                if k == " ":
                    spaces_index.append(index) 
                    
            for j in spaces_index:
                row_change = i
            
                while board[len(board)-row_change-2][j] != " " and len(board)-row_change-2>=0:
         
                    board[len(board)-1-row_change][j] = board[len(board)-row_change-2][j]
                    board[len(board)-row_change-2][j] = " "
                    row_change += 1 

#Erasing empty columns and rows
def erasing(board):

    for i in board: #Removing empty rows
        space_number = 0
        for j in i:
            if j == " ":
                space_number += 1

        if space_number == len(board[0]):
            board.pop(i)

    a = 0 #Variable to control column index if erasing happens
    for i in range(len(board[0])): #Removing empty columns
        space_number = 0
        for j in range(len(board)):
            if board[j][i-a] == " ":
                space_number += 1
       
        if space_number == len(board):
            a += 1
            for j in range(len(board)):
                board[j].pop(i)
        
#Checking if there is a possible move
def checking_board(board):

    row_lenght = len(board[0])
    column_lenght = len(board)
    last_column_index = len(board[0])-1
    last_row_index = len(board)-1

    for i in range(column_lenght):
        for j in range(row_lenght):

            choice = board[i][j]
            if i>0 and board[i-1][j] != " ":  #Checking upward
                if board[i-1][j] == choice:
                    return True

            if i<last_row_index and board[i+1][j] != " ": #Checking downward
                if board[i+1][j] == choice:
                    return True
                
            if j>0 and board[i][j-1] != " ": #Checking left
                if board[i][j-1] == choice:
                    return True
           
            if j<last_column_index and board[i][j+1] != " ": #Checking right
                if board[i][j+1] == choice:
                    return True
    
    return False

#Printing board with removing brackets
def printing_board(board):
    for i in board:
        print(" ".join(i))

#Function to call gameplay
def game_func():
        
        global score
        global remove_number

        user_input= input("Please enter a row and a column number: ")
        print("")
        row_choice_index = int(user_input[0]) -1
        column_choice_index = int(user_input[2]) -1

        while not checking_choice(row_choice_index, column_choice_index, board): #Checking if the entered cell is valid
            print("Please enter a correct size!\n") 
            user_input = input("Please enter a row and a column number: ")
            print("")
            row_choice_index = int(user_input[0])-1
            column_choice_index = int(user_input[2])-1

        choice = board[row_choice_index][column_choice_index]
        controlling_choice(row_choice_index,column_choice_index, board, choice) #Making changes on the board

        if remove_number == 0: #Checking if any change happened
            print("No movement happened try again\n")
            printing_board(board)
            print("")
            print("Your score is: " + str(score) + "\n")
            game_func() 

        else: #Making column and row changes, calculating and printing new score if movement happened
            falling(board)
            erasing(board)
            printing_board(board)
            print("")
            score += int(choice)*remove_number
            print("Your score is: " + str(score) + "\n")


game_in = sys.argv[1]  #Getting input file
game = (open(game_in, "r")).read()
#Converting game to array
board = game.split("\n")
for i in range(len(board)): 
    board[i] = board[i].split(" ")

score = 0
#Controlling if there are any possible moves 
printing_board(board)
print("")
print("Your score is: " + str(score) + "\n")
while checking_board(board): #Checking if there is a possible move
    remove_number = 0 #Resetting remove_number to zero for every call
    game_func()

print("Game over") #Printing game over when there is no possible move






