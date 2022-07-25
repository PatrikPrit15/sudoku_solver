import random,time,copy

board=[[[0,set(range(1,10))] for c in range(9)] for _ in range(9)]

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
board_old=copy.deepcopy(board)
dead_count=0
mpoc=0
while 1:
    mi=10
    xmi=-1
    ymi=-1
    poc=0
    counter+=81
    for y in range(9):
        for x in range(9):
            l=len(board[y][x][1])
            if l<1:
                dead_count+=1
                # print(f"dead {dead_count} times")
                board=copy.deepcopy(board_old)
            elif l>1 and l<mi:
                mi=l
                ymi=y
                xmi=x
            if l==1:
                poc+=1
    if poc>=mpoc:
        mpoc=poc
        print(mpoc,mi,xmi,ymi,dead_count)
    if poc==81:
        break
    if mi<10:
        counter+=20
        colapse(ymi,xmi,random.choice(list(board[ymi][xmi][1])))


for r in board:
    print(*[e[1] for e in r])
    
print(f"cas bol {time.perf_counter()-start}s a vykonalo sa +- {counter} operacii")


