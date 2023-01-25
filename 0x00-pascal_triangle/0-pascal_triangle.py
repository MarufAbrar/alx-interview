#!/usr/bin/python3
def pascal_triangle(n): if n <= 0: return []

triangle = []
for row_num in range(n):
    row = [1]
    for k in range(1, row_num):
        prev_row = triangle[row_num-1]
        row.append(prev_row[k-1] + prev_row[k])
    if row_num != 0:
        row.append(1)
    triangle.append(row)

return triangle
