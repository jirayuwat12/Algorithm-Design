# O(n^3) with out prefix sum
# O(n^2) with prefix sum
def mss_brute_force(arr,prefix_sum = False):
    max_sum = 0
    ps_l = [arr[0]]
    if prefix_sum:
        for i in range(1,len(arr)):
            ps_l.append(ps_l[-1]+arr[i])

    for i in range(len(arr)):
        for j in range(i, len(arr)):

            if prefix_sum:
                summ = ps_l[j] - ps_l[i-1]
            else:
                summ = sum(arr[i:j+1])
            
            max_sum = max(max_sum, sum(arr[i:j+1]))
    return max_sum

if __name__ == "__main__":
    print("Max subarray sum brute force")
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print("brute force- - - - - - - - - -",mss_brute_force(arr))
    print("brute force with prefix sum- -",mss_brute_force(arr,True))
