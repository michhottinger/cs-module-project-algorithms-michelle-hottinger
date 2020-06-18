'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, ate=0):
    # Your code here
    #acc is the numb of cookies eaten thus far
    #n==cookies needed to be eaten in total
    #max of 3
    #base is when ate cookies is equal to n
    if ate == n:
        return 1
    result = 0
    for cookies in [1, 2, 3]:
        if ate + cookies <= n:
            result += eating_cookies(n, ate+cookies) 
    return result

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
