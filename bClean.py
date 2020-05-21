def getdpos(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                return [i,j]
def nextMove(posr, posc, board):
    di,dj = getdpos(board)
    if posr > di:
        print ('UP')
    elif posr < di:
        print ('DOWN')
    else:
        if posc > dj:
            print ('LEFT')
        elif posc < dj:
            print ('RIGHT')
        else:
            print ('CLEAN')
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
