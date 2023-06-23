"""
<aside>
💡 **Question 3**

****Given a positive integer, N. Find the factorial of N. 

**Example 1:**

Input: N = 5 

Output: 120

**Example 2:**

Input: N = 4

Output: 24

</aside>
"""

def fact(n):
    try:
        if n == 0:
            return 1
        return n * fact(n-1)
    except Exception as e:
        raise e
    
n = 5
print(fact(n))