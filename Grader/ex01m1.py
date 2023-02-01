ans = list()
def solve(x1,y1,x2,y2,pos):
    [posx,posy] = pos
    placex = (x2-x1-1)//2 + x1
    placey = (y2-y1-1)//2 + y1
    # base case
    if x2-x1 ==0 or y2-y1 == 0:
        return
    # pos is in the upper left quadrant
    if posx <= placex and posy <= placey:
        ans.append([placex,placey,0])
        # recur left up
        solve(x1,y1,placex,placey,[posx,posy])
        # recur right up
        solve(placex+1,y1,x2,placey,[placex+1,placey])
        # recur left down
        solve(x1,placey+1,placex,y2,[placex,placey+1])
        # recur right down
        solve(placex+1,placey+1,x2,y2,[placex+1,placey+1])
    # pos is in the upper right quadrant
    elif posx > placex and posy <= placey:
        ans.append([placex,placey,1])
        # recur left up
        solve(x1,y1,placex,placey,[placex,placey])
        # recur right up
        solve(placex+1,y1,x2,placey,[posx,posy])
        # recur left down
        solve(x1,placey+1,placex,y2,[placex,placey+1])
        # recur right down
        solve(placex+1,placey+1,x2,y2,[placex+1,placey+1])
    # pos is in the lower left quadrant
    elif posx <= placex and posy > placey:
        ans.append([placex,placey,2])
        # recur left up
        solve(x1,y1,placex,placey,[placex,placey])
        # recur right up
        solve(placex+1,y1,x2,placey,[placex+1,placey])
        # recur left down
        solve(x1,placey+1,placex,y2,[posx,posy])
        # recur right down
        solve(placex+1,placey+1,x2,y2,[placex+1,placey+1])
    # pos is in the lower right quadrant
    else:
        ans.append([placex,placey,3])
        # recur left up
        solve(x1,y1,placex,placey,[placex,placey])
        # recur right up
        solve(placex+1,y1,x2,placey,[placex+1,placey])
        # recur left down
        solve(x1,placey+1,placex,y2,[placex,placey+1])
        # recur right down
        solve(placex+1,placey+1,x2,y2,[posx,posy])

def gen_map(L):
    m = [[0 for x in range(L)] for y in range(L)]
    for i in ans:
        [x,y,orientation] = i
        # 0     1       2       3
        # 0 1   1 0     1 1     1 1
        # 1 1   1 1     0 1     1 0
        if orientation == 0:
            m[x][y] |= 0
            m[x+1][y] |= 1
            m[x][y+1] |= 1
            m[x+1][y+1] |= 1
        elif orientation == 1:
            m[x][y] |= 1
            m[x+1][y] |= 0
            m[x][y+1] |= 1
            m[x+1][y+1] |= 1
        elif orientation == 2:
            m[x][y] |= 1
            m[x+1][y] |= 1
            m[x][y+1] |= 0
            m[x+1][y+1] |= 1
        else:
            m[x][y] |= 1
            m[x+1][y] |= 1
            m[x][y+1] |= 1
            m[x+1][y+1] |= 0
    
    for x in range(L):
        for y in range(L):
            print(m[y][x],end=" ")
        print()

        
if __name__ == "__main__":
    [L,x,y] = [int(x) for x in input().split()]
    solve(0,0,L-1,L-1,[x,y])
    print(len(ans))
    for i in ans:
        print(i[2],i[0],i[1])
    # gen_map(L)