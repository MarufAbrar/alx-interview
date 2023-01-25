#!/usr/bin/python3
def pascal_triangle(n): 
    # Base case: return empty list for n <= 0
    if n <= 0:
        return []

    # Start with a hardcoded list of the first row
    result = [[1]]

    # Iterate from 1 to n
    for i in range(1, n): 
        row = [1] 

        # Iterate from 1 to the length of the last row
        for j in range(1, i): 
            # Calculate the value of each row item 
            # and append them to the row
            row.append(result[i-1][j] + result[i-1][j-1]) 

        # Append the last item to the row
        row.append(1) 

        # Append the new row to the result
        result.append(row) 

    return result