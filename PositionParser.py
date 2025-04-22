import numpy as np
import ast
import math
positions  = []
def read_positions(filename: str,):
    """positions from the position list turned into a usable list"""
    positions = open(f"{filename}", "r")
    return [line.strip() for line in positions if line.strip()][1:]


result = read_positions("pos_history.log")
# Initialize an empty dictionary to hold the positions
dictPoses = {}

# Iterate over the result to populate dictPoses
for i in range(len(result)):
    # Parse the string representation of the list
    position = ast.literal_eval(result[i])  # Converts '[XXX, YYY, ZZZ]' to [XXX, YYY, ZZZ]
    
    # Round each number to the nearest whole number
    rounded_position = [math.floor(num) for num in position]
    
    dictPoses[f'position{i}'] = rounded_position

    
print(dictPoses)