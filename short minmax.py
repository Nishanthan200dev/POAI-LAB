X, O, E = 1, -1, 0

def evaluate(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != E: return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != E: return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != E: return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != E: return b[0][2]
    return 0

def movesLeft(b):
    return any(E in row for row in b)

def minimax(b, isMax):
    score = evaluate(b)
    if score or not movesLeft(b): return score
    best = -float('inf') if isMax else float('inf')
    for i in range(3):
        for j in range(3):
            if b[i][j] == E:
                b[i][j] = X if isMax else O
                val = minimax(b, not isMax)
                b[i][j] = E
                best = max(best, val) if isMax else min(best, val)
    return best

def bestMove(b):
    move, bestVal = (-1, -1), -float('inf')
    for i in range(3):
        for j in range(3):
            if b[i][j] == E:
                b[i][j] = X
                val = minimax(b, False)
                b[i][j] = E
                if val > bestVal:
                    move, bestVal = (i, j), val
    return move

def show(b):
    for r in b:
        print(' '.join('X' if x == X else 'O' if x == O else '.' for x in r))

# Example game
board = [
    [X, O, X],
    [O, X, E],
    [E, O, X]
]

print("Current Board:")
show(board)
move = bestMove(board)
print(f"\nBest Move: {move}")
board[move[0]][move[1]] = X
print("\nBoard after best move:")
show(board)
