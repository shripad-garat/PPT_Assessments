"""
<aside>
💡 **Question 7**
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

</aside>
"""

def matrix(m , n ,ops):
    try:
        if len(ops)==0:
            return m*n
        a,b = ops[0][0],ops[0][1]
        for i in range(len(ops)):
            a = min(a,ops[i][0])
            b = min(b,ops[i][1])

        return a*b

    except Exception as e:
        raise e
    

m = 3
n = 3
ops = [[2,2],[3,3]]
print(matrix(m,n,ops))