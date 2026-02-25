def zigzag_traverse(matrix):
    """
    повертає масив в форматі списку значень матриці в порядку "зигзагу" 
    """
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []
    
    for s in range(m + n - 1):
        if s % 2 == 0:
            if s < m-1:
                row = s
            else:
                row = m-1
            col = s - row
            while row >= 0 and col < n:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            if s < n-1:
                row = s
            else:
                row = n-1
            row = s - col
            while col >= 0 and row < m:
                result.append(matrix[row][col])
                row += 1
                col -= 1
                
    return result
