'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    tracker = 0
    i= 0
    while tracker < len(arr):
        tracker += 1 
        if arr[i] == 0:
            value = arr.pop(i)
            arr.append(value)
        else:
            i += 1
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")