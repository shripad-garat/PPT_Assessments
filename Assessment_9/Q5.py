"""
<aside>
💡 **Question 5**

Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

**Example 1:**

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: 8

**Example 2:**

Input: arr = {1, 4, 45, 6, 10, -8};
Output: 45

</aside>
"""

def maxx(x):
    try:
        if len(x) == 1:
            return  x[0]
        return max(x[0],maxx(x[1:]))
    

    except Exception as e:
        raise e
    
arr = [1, 4, 45, 6, 10, -8]
print(maxx(arr))