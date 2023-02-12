def distance(pos1,pos2):
    return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2

def closest_pair(coor_x,coor_y):
    if len(coor_x) <= 4:
        min_dist = 1e10
        for i in coor_x:
            for j in coor_x:
                if distance(i,j) != 0:
                    min_dist = min(distance(i,j),min_dist)
        return min_dist
    else :
        mid = len(coor_x)//2
        left_x = coor_x[:mid]
        right_x = coor_x[mid:]
        mid_x = coor_x[mid][0]
        left_y = []
        right_y = []
        for i in coor_y:
            if i[0] <= mid_x:
                left_y.append(i)
            else:
                right_y.append(i)
        min_dist = min(closest_pair(left_x,left_y),closest_pair(right_x,right_y))
        strip = []
        for i in coor_y:
            if abs(i[0]-mid_x) < min_dist**0.5:
                strip.append(i)
        for i in range(len(strip)):
            for j in range(i+1,len(strip)):
                if abs(strip[i][1] - strip[j][1]) > min_dist:
                    break
                min_dist = min(distance(strip[i],strip[j]),min_dist)
        return min_dist

coor = []
# input
n = int(input())
while n:
    pos = [int(i) for i in input().split()]
    coor.append(pos)
    n-=1

sort_by_x = sorted(coor)
sort_by_y = sorted(coor,key=lambda x : x[1])


print(closest_pair(sort_by_x,sort_by_y))