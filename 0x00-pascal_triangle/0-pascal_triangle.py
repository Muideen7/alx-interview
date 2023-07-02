def pascal_triangle(n):
    """
    Generate Pascal's Triangle of n rows.
    Returns a list of lists representing the triangle.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    for i in range(n):
        row = [1]
        
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
        
        if i > 0:
            row.append(1)
        
        triangle.append(row)
    
    return triangle
