"""
<aside>
💡 **Question 2**

Given a number n, find the sum of the first natural numbers.

**Example 1:**

Input: n = 3 

Output: 6

**Example 2:**

Input  : 5 

Output : 15

</aside>
"""

def sum_of_n(n):
    try:
        if n == 0:
            return 0
        return n + sum_of_n(n-1)
    except Exception as e:
        raise e
    

n = 5
print(sum_of_n(n))