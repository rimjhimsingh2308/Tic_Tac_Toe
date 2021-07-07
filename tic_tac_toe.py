game_board = ["_","_","_",
     "_", "_","_",
     "_","_","_"]

# if game is still going
game_still_going = True

# who won? or tie
winner = None

# whose turn is it
current_player = "X"

# display the empty board
def display_board():
 print(" " + "_" + " " + "_" + " " + "_" + " ")
 print("|" + game_board[0] + "|" + game_board[1] + "|" + game_board[2] + "|")
 print("|" + game_board[3] + "|" + game_board[4] + "|" + game_board[5] + "|")
 print("|" + game_board[6] + "|" + game_board[7] + "|" + game_board[8] + "|")
 
# start the game 
def start_game():
 # display the initial board
 display_board()
 # while the game is still going 
 while game_still_going :

  # handle turn of an arbitary player
  manage_turn(current_player)

  # check if the game has ended
  check_if_game_over()

  # change the player
  flip_player()

 # if game ended
 if winner=="X" or winner=="O" :
  print(winner + " won.")
 elif (winner==None) or ("_" not in game_board) :
  print("It is a tie.")

# handle turn of an arbitary player
def manage_turn(player):
 print( player + "'s turn.")
 position = input(" Chooose a position from 1-9: ")

 valid = False
 while not valid:
  while position not in ["1","2","3","4","5","6","7","8","9"] :
   print(" Invalid input!try again.")
   position = input(" Chooose a position from 1-9: ")
  
  position = int(position) -1
  if game_board[position] == "_":
   valid = True
  else:
   print("You can't go there! try again.") 
 game_board[position] = player

 display_board()

# check if the game is over
def check_if_game_over():

 # check if either won or not
 check_for_winner()

 # check if it's a tie
 check_if_tie()

# check if either won or not
def check_for_winner():

 # set up global variables
 global winner

 # check rows
 row_winner = check_rows() 

 #check columns
 column_winner = check_columns()

 # check diagonals
 diagonal_winner = check_diagonals()
 if row_winner :
  winner = row_winner
 if column_winner :
  winner = column_winner
 if diagonal_winner :
  winner = diagonal_winner
 return

# check if it's a tie
def check_if_tie():

 # set up global variables
 global game_still_going
 if "_" not in game_board:
  game_still_going = False

 return

def flip_player():
 # set up global variables
 global current_player
 if current_player == "X":
  current_player = "O"
 elif current_player == "O":
  current_player = "X"

 return

def check_rows():
 # set up global variables
 global game_still_going
 # check if any of the rows have all same values and are not empty
 row1 = game_board[0] == game_board[1] == game_board[2] != "_"
 row2 = game_board[3] == game_board[4] == game_board[5] != "_"
 row3 = game_board[6] == game_board[7] == game_board[8] != "_"

 # if any of the rows does have the match , it's a win
 if row1 or row2 or row3:
  game_still_going = False
 # return the winner "X" or "O"
 if row1 :
  return game_board[0]
 elif row2 :
  return game_board[3]
 elif row3 :
  return game_board[6]

 return

def check_columns():
 # set up global variables
 global game_still_going
 # check if any of the columns have all same values and are not empty
 column1 = game_board[0] == game_board[3] == game_board[6] != "_"
 column2 = game_board[1] == game_board[4] == game_board[7] != "_"
 column3 = game_board[2] == game_board[5] == game_board[8] != "_"
 
 # if any of the columns does have the match , it's a win
 if column1 or column2 or column3:
  game_still_going = False
 # return the winner "X" or "O"
 if column1 :
  return game_board[0]
 elif column2 :
  return game_board[1]
 elif column3 :
  return game_board[2]

 return

def check_diagonals():
 # set up global variables
 global game_still_going
 # check if any of the diagonals have all same values and are not empty
 diagonal1 = game_board[0] == game_board[4] == game_board[8] != "_"
 diagonal2 = game_board[2] == game_board[4] == game_board[6] != "_"
 # if any of the diagonals does have the match , it's a win
 if diagonal1 or diagonal2:
  game_still_going = False
 # return the winner "X" or "O"
 if diagonal1 :
  return game_board[0]
 elif diagonal2 :
  return game_board[2]

 return

start_game()
