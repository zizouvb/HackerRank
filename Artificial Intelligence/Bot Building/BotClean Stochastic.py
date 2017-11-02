#!/bin/python3
def nextMove(posr, posc, board):
    if board[posr][posc]=='d':
        print("CLEAN")
    else:
        for i in range(len(board)):
            if 'd' in board[i]:
                dcol = board[i].index('d')
                drow = i
        if dcol-posc>0:print("RIGHT")
        elif drow-posr>0:print("DOWN")
        elif drow-posr<0:print("UP")
        else:print("LEFT")
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)