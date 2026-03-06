import math

b = [" "] * 9

def win(b):
    w=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i,j,k in w:
        if b[i]==b[j]==b[k]!=" ": return b[i]
    if " " not in b: return "Tie"
    return None

def minimax(b, m):
    r = win(b)
    if r=="O": return 1
    if r=="X": return -1
    if r=="Tie": return 0

    best = -math.inf if m else math.inf
    for i in range(9):
        if b[i]==" ":
            b[i] = "O" if m else "X"
            s = minimax(b, not m)
            b[i] = " "
            best = max(best,s) if m else min(best,s)
    return best

def best():
    move, bestScore = -1, -math.inf
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            s=minimax(b,False)
            b[i]=" "
            if s>bestScore:
                bestScore, move = s, i
    return move

def show():
    for i in range(0,9,3):
        print(b[i],b[i+1],b[i+2])

while True:
    show()
    p=int(input("Enter position (0-8): "))
    if b[p]==" ":
        b[p]="X"
    if win(b): break

    c=best()
    b[c]="O"
    if win(b): break

show()
print("Result:",win(b))
