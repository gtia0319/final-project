import random
def create_board():
    #create a list to store value
    return [' ']*9
def print_board(board):
    print()
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print()
def check_whether_win(board, symbol):
    #This is the win condition, like X=X,X=X,X=X
    win_condition=[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_condition:
        if board[a]==symbol and board[b]==symbol and board[c]==symbol:
            return True
    return False
def board_whether_full(board):
    return ' ' not in board
def Your_movement(board, symbol):
    while True:
        position=input('please input a number between 1 and 9: ')
        if position.isdigit():
            index=int(position)-1
            if 0<=index<=8 and board[index]==' ':
                board[index]=symbol
                break
            else:
                print('The position has been occupied!')
        else:
            print('Please input a integer!')
def Your_childhood_self_movement(board, symbol):
    empty_positions=[]
    #create a empty list to store the index which value is empty
    for i, j in enumerate(board):
        if j==' ':
            empty_positions.append(i)
    index=random.choice(empty_positions)
    #random choice a index which value is empty
    board[index]=symbol
    print(f'Your childhood self put {symbol} in {index+1}')
def play_the_game():
    while True:
        Your_symbol=input('Please select your symbol(X or O): ').upper()
        if Your_symbol in ['X', 'O']:
            break
        else:
            print('Please input valid symbol!')
    if Your_symbol=='X':
        Your_childhood_symbol='O'
    else:
        Your_childhood_symbol='X'
    print(f'You now: {Your_symbol} You twenty years ago: {Your_childhood_symbol}')
    board=create_board()
    print_board(board)
    while True:
        Your_movement(board, Your_symbol)
        print_board(board)
        if check_whether_win(board, Your_symbol):
            print('Congratulation! You win!')
            return True
        if board_whether_full(board):
            print('It\'s a draw! Let\'s start a new game.')
            return False
        Your_childhood_self_movement(board, Your_childhood_symbol)
        print_board(board)
        if check_whether_win(board, Your_childhood_symbol):
            print('You were more awesome when you were a kid.')
            return True
        if board_whether_full(board):
            print('It\'s a draw! Let\'s start a new game.')
            return False
def main():
    while True:
    #to make sure there is a winner
        print('Let\'s play the game!')
        if play_the_game():
            break
        print('Game over!')
if __name__=='__main__':
    main()