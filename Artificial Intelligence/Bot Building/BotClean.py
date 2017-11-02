#!/usr/bin/python
import sys
# Head ends here
def next_move(posr, posc, board):
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        for i in range(len(board)):
            if 'd' in board[i]:
                dcol = board[i].index('d')
                drow = i
                break
        if dcol>posc: print("RIGHT")
        elif dcol<posc: print("LEFT")
        elif drow<posr: print("UP")
        else: print("DOWN")

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)