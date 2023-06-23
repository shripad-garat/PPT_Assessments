"""
<aside>
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**
Input: n = 1 

Output: true

**Example 2:**
Input: n = 16 

Output: true

**Example 3:**
Input: n = 3 

Output: false

</aside>
"""

def ispower(n):
    try:
        if n == 1:
            return True
        elif n%2== 0:
            return ispower(n/2)
        else:
            return False
        
    except Exception as e:
        raise e
    
n = 16    
print(ispower(n))