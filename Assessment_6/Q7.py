"""
<aside>
💡 **Question 7**

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

**Input:** n = 3

**Output:** [[1,2,3],[8,9,4],[7,6,5]]
</aside>
"""
import numpy as np 
import numpy 
def spiral(n):
    try:
        i = 0
        j = 0
        k = 0
        l = 0
        a = np.zeros([n,n])
        while (i!=(n/2) and j != round(n/2)):
            while(j<n):
                k += 1
                a[i][j] = k
                j += 1
            i += 1
            while(i<n):
                k += 1
                a[i][j] = k
                i += 1
            j -= 1
            while(j>=l):
                k+=1
                a[i][j] = k
                j -= 1
            i -= 1
            while(i>=l):
                k += 1
                a[i][j] = k
                i -= 1
            l += 1
        return a
     
    except Exception as e:
        raise e
    
n = 3
print(spiral(n))