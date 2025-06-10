def solve(r=0, p=[-1]*8):
    if r == 8:
        for i in p: print(" ".join("Q" if j == i else "." for j in range(8)))
        return True
    for c in range(8):
        if all(p[i] != c and abs(p[i] - c) != r - i for i in range(r)):
            p[r] = c
            if solve(r + 1, p): return True

solve()
