GOAL=((1,2,3),(4,5,6),(7,8,0))
MOV=[(-1,0),(1,0),(0,-1),(0,1)]

def b(s): return next((i,j) for i,r in enumerate(s) for j,v in enumerate(r) if v==0)
def sw(s,p1,p2): l=[list(r) for r in s]; i1,j1=p1;i2,j2=p2; l[i1][j1],l[i2][j2]=l[i2][j2],l[i1][j1]; return tuple(tuple(r) for r in l)
def succ(s): i,j=b(s); return [sw(s,(i,j),(i+dx,j+dy)) for dx,dy in MOV if 0<=i+dx<3 and 0<=j+dy<3]

def dfs(s,vis,path):
    if s==GOAL: path.append(s); return True
    vis.add(s); path.append(s)
    for n in succ(s):
        if n not in vis and dfs(n,vis,path): return True
    path.pop(); return False

def p(s): [print(r) for r in s]; print("")

start=((1,2,3),(4,0,6),(7,5,8)); vis=set(); path=[]
if dfs(start,vis,path): print("Steps:",len(path)-1); [p(st) for st in path]
