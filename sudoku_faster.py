import random,time,copy

board=[[[0,set(range(1,10))] for c in range(9)] for _ in range(9)]

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

def get_block(y,x):
    yr=[0,0]
    xr=[0,0]
    if y<3:
        yr[1]=3
    elif y<6:
        yr[0]=3
        yr[1]=6
    else:
        yr[0]=6
        yr[1]=9
    if x<3:
        xr[1]=3
    elif x<6:
        xr[0]=3
        xr[1]=6
    else:
        xr[0]=6
        xr[1]=9

    for ny in range(yr[0],yr[1]):
        for nx in range(xr[0],xr[1]):
            if ny!=y and nx!=x:
                yield ny,nx

def colapse(y,x,v):
    board[y][x][0]=v
    board[y][x][1]=set([v])
    for nc in range(9):
        if nc!=x:
            board[y][nc][1].discard(v)
        if nc!=y:
            board[nc][x][1].discard(v)

    for yb,xb in get_block(y,x):
        board[yb][xb][1].discard(v)


print("zadaj vstupy")
for y in range(9):
    vstup=tuple(map(int,list(input())))
    if vstup=="koniec":
        break
    for x,v in enumerate(vstup):
        if v!=0:
            colapse(y,x,v)
start=time.perf_counter()
print("riesenie je v procese\n")

counter=0    

en=1
while en:
    en=0
    for y in range(9):
        for x in range(9):
            if board[y][x][0]==0 and len(board[y][x][1])==1:
                en=1
                counter+=20
                colapse(y,x,list(board[y][x][1])[0])

print()
def solve(c):
    global counter
    y=c//9
    x=c%9
    if c==81:
        print("\n\n+ ----------- + ----------- + ----------- +",end="")
        for row in range(9):
            print("\n",end="\n|  ")
            for col in range(9):
                num_end = "  |  " if ((col+1)%3 == 0) else "   "
                print(board[row][col][0],end=num_end)
    
            if ((row+1)%3 == 0):
                print("\n+ ----------- + ----------- + ----------- +",end="")
        print(f"\n\ncas bol {time.perf_counter()-start}s a vykonalo sa +- {counter} operacii")
        exit()
    if len(board[y][x][1])!=1:
        for i in board[y][x][1]:
            board[y][x][0]=i
            counter+=31
            if is_pos(y,x,i):
                solve(c+1)
        board[y][x][0]=0
    else:
        solve(c+1)


solve(0)


