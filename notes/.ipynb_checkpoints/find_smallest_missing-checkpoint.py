    
def find_smallest_missing(arr):
    # Your code here
    if arr[0] != 0:
        return 0
    #edge case: where 0 is missing
    #in nothing is missing?
    #loop through the arr
    #check the element adjacent to current
    #make sure that the adjacent element == current +1
    #if adjacent element != current + 1
    #them we know that current + 1_should_ be there
    #but it wasn't so return current + 1
    #need to loop until len(arr)-1 since we are checking the i+1 element
    for i in range(len(arr)-1):
        if arr[i+1] != arr[i] + 1:
            return arr[i] + 1
    #if we get out of loop, then we did not find a missing element
    return arr[-1] + 1

#find the middle node of a linked list
#idea 1
#loop through linked list and return len
#divide len by 2: mid = len(arr) // 2
#return mid point
#traverse to mid to get value: start from head and jump
#until we reach the mid node

#idea2
#use two pointer that start at the head
#two pointers run as n and n2 speeds
#n = i+1
#n2 = i+2
#set faster = fast.next.next it can be on none, prev, or tail node
#when pointer n2 finishes, n will be at midpoint
#return node slower pointer points at

def find_mid_node():
    
    fast = ll
    slow = ll
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next