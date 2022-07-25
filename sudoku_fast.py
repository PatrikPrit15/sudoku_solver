import random,time,copy

board=[[[0,0] for c in range(9)] for _ in range(9)]

def get_block(y,x):
    yr=[0,0]
    xr=[0,0]
    if y<=2:
        yr[1]=3
    elif y<=5:
        yr[0]=3
        yr[1]=6
    else:
        yr[0]=6
        yr[1]=9
    if x<=2:
        xr[1]=3
    elif x<=5:
        xr[0]=3
        xr[1]=6
    else:
        xr[0]=6
        xr[1]=9

    for ny in range(yr[0],yr[1]):
        for nx in range(xr[0],xr[1]):
            if not (ny==y and nx==x):
                yield ny,nx

def is_pos(y,x,v):
    for nc in range(9):
        if board[y][nc][0]==v and nc!=x:
            return 0 
        if board[nc][x][0]==v and nc!=y:
            return 0

    for yb,xb in get_block(y,x):
        if board[yb][xb][0] == v and not(yb==y and xb==x):
            return 0
    return 1


print("zadaj vstupy")
for y in range(9):
    vstup=tuple(map(int,list(input())))
    for x,v in enumerate(vstup):
        board[y][x]=[v,v]

start=time.perf_counter()
print("riesenie je v procese\n")
counter=0
def solve(c):
    global counter
    y=c//9
    x=c%9
    if c==81:
        for yv in range(9):
            if yv in [3,6]:
                print("~"*11)
            for xv in range(9):
                if xv in [3,6]:
                    print("|",end="")
                print(board[yv][xv][0],end="")
            print()
        print(f"cas bol {time.perf_counter()-start}s a vykonalo sa +- {counter} operacii")
        exit()
    if board[y][x][1]==0:
        for i in range(1,10):
            board[y][x][0]=i
            counter+=31
            if is_pos(y,x,i):
                solve(c+1)
        board[y][x][0]=0
    else:
        solve(c+1)


solve(0)