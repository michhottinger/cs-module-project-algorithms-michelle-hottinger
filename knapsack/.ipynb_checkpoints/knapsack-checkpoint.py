#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    #cost <= capacity
    #cost = sum(Item.size)
    #payoff = sum(Item.value)
    
    if Item.size >= capacity or capacity ==0: #base case item is too big or bag has no capacity
            return 0
    result = 0 #list the results here
    for items in ['index', 'size', 'value']:
        if Item.size <= capacity:
            result += knapsack_solver(items, capacity+Item.size) #recursively go through options
    return result and sum(Item.value)
    


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')