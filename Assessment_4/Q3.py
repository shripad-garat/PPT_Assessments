"""
<aside>
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

</aside>
"""

def transpose(arr):
    try:
        n = len(arr)
        m = len(arr[0])
        for i in range(n):
            for j in range(1+i,m):
                arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
                print(arr)
        
        return arr

    except Exception as e:
        raise e
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))