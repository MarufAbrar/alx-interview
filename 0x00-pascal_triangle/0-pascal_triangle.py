def pascal_triangle(n): 
    result = [] 

    # Edge case 
    if n <= 0: 
        return result 

    # Generate an empty list of lists  
    for rows in range(n): 
        row_list = []  
        for cols in range(rows + 1): 
            row_list.append(0)  
        result.append(row_list) 

    # Update the first and last elements to 1 
    result[0][0] = 1
    for rows in range(1, n): 
        result[rows][0] = 1
        result[rows][rows] = 1

    # Update the values inside the list of lists using the previous row 
    for rows in range(1, n): 
        for cols in range(1, rows): 
            result[rows][cols] = result[rows-1][cols-1] + result[rows-1][cols] 

    return result 