#Team 6: Aria Askaryar, Shriya Bannikop
"""
Algorithm 1: The Island problem
Largest Land Mass Finder

This module provides a function to determine the size of the largest land mass that can be formed by changing a single
water cell (represented by 1) to a land cell (represented by 0) in a given matrix.

The matrix can have varying sizes and consists of binary entries (0s and 1s).

Functions:
    - largest_land_mass(matrix): Returns the size of the largest possible land mass.

Usage example:
    >>> matrix = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
    >>> largest_land_mass(matrix)
    5
"""


# this is only used for visual aid and not used in the algorithm
# check the print statements below
import pandas as pd

#This function determines the size of the largest land mass after changing a single water cell to a land cell.
def largest_land_mass(matrix):
    # this checks directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    def dfs(x, y, visited):
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == 1 or visited[x][y]:
            return 0
	#if cell has been visited or not
        visited[x][y] = True
        size = 1
        for dx, dy in directions:
            size += dfs(x + dx, y + dy, visited)
        return size

    #set the max to 0
    max_size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # Change the cell from 1 to 0
                matrix[i][j] = 0
                visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
                size = dfs(i, j, visited)
                if size > max_size:
                    max_size = size
                # Reset the cell back to 1
                matrix[i][j] = 1
    return max_size

# Sample Input
# output should be 5
sample_input = [
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 0]
]

#using Pandas package to just help with better visualization
df = pd.DataFrame(sample_input)

#This will print the output and results of sample input
print("Sample output: ")
print(df.to_string(header=False, index=False))
print("output for sample:", largest_land_mass(sample_input))  # Expected Output: 5

# Input 1A 
# output should be 8
input_1A = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
]
#using Pandas package to just help with better visualization
df1 = pd.DataFrame(input_1A)

#This will print the output and results of sample input
print("input 1a:")
print(df1.to_string(header=False, index=False))
print("output for input 1a:", largest_land_mass(input_1A))  

#this is a custom matrix i made myself -Aria
# Input 2 
# output should be 6
input_2 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
#using Pandas package to just help with better visualization
df2 = pd.DataFrame(input_2)

#This will print the output and results of sample input
print("input 1a:")
print(df2.to_string(header=False, index=False))
print("output for input 2:", largest_land_mass(input_2))  



######################################################################
####################### output  ######################################
######################################################################
# adv_algorithm> python algorithm_1.py
# Sample output: 
# 0 1 1
# 0 0 1
# 1 1 0
# output for sample: 5  
# input 1a:
# 1 0 1 0 0
# 0 0 1 1 0
# 0 1 1 1 1
# 1 0 1 0 0
# output for input 1a: 8
# input 1a:
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 1 1 0
# 1 0 0 0 1
# 0 1 1 1 0
# output for input 2: 6