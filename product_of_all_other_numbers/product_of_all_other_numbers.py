'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here 
    
    n = len(arr)
#     prod = 1 #initialize the products list
#     for i in range(n): 
#         prod = prod * arr[i - 1] 
#     return prod
    
  
 
  
    # Base case 
    if(n == 1): 
        print(0) 
        return
          
    # Allocate memory for temporary arrays left[] and right[]  
    left = [0]*n  
    right = [0]*n  
  
    # Allocate memory for the product array  
    prod = [0]*n  
  
    # Left most element of left array is always 1  
    left[0] = 1
  
    # Rightmost most element of right array is always 1  
    right[n - 1] = 1
  
    # Construct the left array  
    #arr index value *  same index  value which will start = 1
    #this will give arr i[0] as i[1] in left arr: [l*i0, l*i0, l*i2]
    #as we loop, products of the the left part of arr[i] fills the left array
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
  
    # Construct the right array  
    #now we increment backwards
    #do the same thing as left
    #start at -2 because we assign 1 to i[-1] and multiple 1*arr[-1]
    # this captures the last value of the array and increments inward to j+1
    #stops right before reaching j
    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]  
  
    # Construct the product array using  
    # left[] and right[] multiplied together 
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    return prod

if __name__ == '__main__':
    # Use the main function to test your implementation
     #arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    