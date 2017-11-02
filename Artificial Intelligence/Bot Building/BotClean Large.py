def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy]=='d':
        print("CLEAN")
    else:
        for i in range(len(board)):
            if 'd' in board[i]:
                dcol = board[i].index('d')
                drow = i
                break
        if dcol>posy: print("RIGHT")
        elif dcol<posy: print("LEFT")
        elif drow<posx: print("UP")
        else: print("DOWN")
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)