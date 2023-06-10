"""
<aside>
💡 **Question 2**

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

You must write a solution in O(log(m * n)) time complexity.
**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output:** true
</aside>
"""

def isthere(mat,val):
    try:
        start = 0
        end = len(mat)-1
        while start<= end:
            mid = (start+end)//2
            if (mat[mid][0]<=val) and (mat[mid][-1]>=val):
                start1 = 0
                end1 = len(mat[0])
                while start1 <= end1:
                    mid1 =  (start1+end1)//2
                    if mat[mid][mid1] == val:
                        return True
                    elif mat[mid][mid1] < val:
                        start1 = mid1
                    elif mat[mid][mid1] > val:
                        end1 = mid1 + 1
            elif mat[mid][0]>val and mat[mid][-1]>val:
                end = mid 
            elif mat[mid][0]<val and mat[mid][-1]<val:
                start = mid + 1

    except Exception as e:
        raise e
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(isthere(matrix,target))