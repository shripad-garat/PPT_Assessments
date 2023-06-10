"""
<aside>
💡 **Question 8**

Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

**Example 1:**
**Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

**Output:**

[[7,0,0],[-7,0,3]]
</aside>
"""
import numpy as np

def matProd(mat1,mat2):
    try:
        n = len(mat1)
        m = len(mat2)
        a = np.zeros([n,m])
        for i in range(n):
            sum = 0
            for j in range(m):
                sum += mat1[i][j]*mat2[j][i]
            a[i][j] = sum

        return a     

    except Exception as e:
        raise e
    
mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(matProd(mat1,mat2))