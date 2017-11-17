#!/bin/python3

import sys

def surfaceArea(A,H,W):
    # Complete this function
    surface = H*W*2

    for i in range(H):
        surface += A[i][0]
        surface += A[i][W-1]
        for j in range(1,W):
            surface += abs(A[i][j-1]-A[i][j])
    for j in range(W):
        surface += A[0][j]
        surface += A[H-1][j]
        for i in range(1,H):
            surface += abs(A[i-1][j]-A[i][j])

    return surface
if __name__ == "__main__":
    H, W = [int(i) for i in input().split(' ')]
    toy = []
    for _ in range(H):
        toy.append([int(i) for i in input().split(' ')])
    result = surfaceArea(toy,H,W)
    print(result)
