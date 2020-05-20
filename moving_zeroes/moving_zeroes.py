'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    ind = len(arr)-1
    for x, i in enumerate(arr):
        if ind == x:
            break
        if i == 0:
            arr[ind], arr[x] = arr[x], arr[ind]
            ind -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")