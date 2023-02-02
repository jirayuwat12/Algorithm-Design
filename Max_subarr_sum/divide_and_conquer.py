# O(T(n)) = 2T(n/2) + O(n) = O(nlogn)
def mss_divide_and_conquer(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    # T(n/2)
    left = mss_divide_and_conquer(arr[:mid])
    # T(n/2)
    right = mss_divide_and_conquer(arr[mid:])

    # O(n)
    left_sum = 0
    left_max = 0
    for i in range(mid-1,-1,-1):
        left_sum += arr[i]
        left_max = max(left_max, left_sum)

    # O(n)
    right_sum = 0
    right_max = 0
    for i in range(mid,len(arr)):
        right_sum += arr[i]
        right_max = max(right_max, right_sum)

    return max(left, right, left_max+right_max)

if __name__ == "__main__":
    print("Max subarray sum divide and conquer")
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print("divide and conquer- - - - - - -",mss_divide_and_conquer(arr)) 