from random import randint
board = [" "] * 9

def print_board():
    print (board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print (board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print (board[6] + "|" + board[7] + "|" + board[8])

print_board()

def check(char, spot1, spot2, spot3):
    if char == board[spot1] and char == board[spot2] and char == board[spot3]:
        return True

def check_all(char):
    if check (char, 0, 1, 2):
        return True
    if check (char, 3, 4, 5):
        return True
    if check (char, 6, 7, 8):
        return True
    if check (char, 0, 3, 6):
        return True
    if check (char, 1, 4, 7):
        return True
    if check (char, 2, 5, 8):
        return True
    if check (char, 0, 4, 8):
        return True
    if check (char, 2, 4, 6):
        return True


while True:
  player_move = input("Enter a number from 0-8: ")
  player_move = int(player_move)

  if board[player_move] != "x" and board[player_move] != "o":
    board[player_move] = "x"
    if check_all("x"):
        print("X wins")
        break


    while True:
      comp_move = randint(0,8)
      if board[comp_move] != "x" and board[comp_move] != "o":
        board[comp_move] = "o"
        if check_all("o"):
            print("O wins")
            break
        break
  else:
    print("Spot is taken, use another number: ")



  print_board()
