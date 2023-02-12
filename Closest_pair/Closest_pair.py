def minimum_distance(points):
    #write your code here
    min_dist = 0

    #  Haha i am too lazy to write the code for this problem

    return min_dist


if __name__ == "__main__":
    # Read input
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])

    # Sort points by x coordinate
    points.sort()

    # Compute distance
    print("{0:.9f}".format(minimum_distance(points)))