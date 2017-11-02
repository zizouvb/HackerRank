#!/usr/bin/python3
import json
import os

def update_board(board):
    if os.path.isfile("board"):
        old_board = json.load(open("board"))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "o":
                    board[i][j] = old_board[i][j]
    json.dump(board, open("board", "w"))

def next_move(posx, posy, board):

   
    if board[posx][posy] == 'd':
        print('CLEAN')
    else:
        dcol = -1
        for i in range(len(board)):
            if 'd' in board[i]:
                dcol = board[i].index('d')
                drow = i
            if 'o' in board[i]:
                ocol = board[i].index('o')
                orow = i
        if dcol != -1:
            if dcol>posy: print("RIGHT")
            elif dcol<posy: print("LEFT")
            elif drow<posx: print("UP")
            else: print("DOWN")
        else:
            if ocol>posy: print("RIGHT")
            elif ocol<posy: print("LEFT")
            elif orow<posx: print("UP")
            else: print("DOWN")
    
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]
    update_board(board)
next_move(pos[0], pos[1], board)