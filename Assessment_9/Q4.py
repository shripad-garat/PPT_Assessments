"""
<aside>
💡 **Question 4**

Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

**Example 1 :** 

Input: N = 5, P = 2

Output: 25

**Example 2 :**
Input: N = 2, P = 5

Output: 32

</aside>
"""

def power(x,n):
    try:
        if abs(n) == 1:
            return x
        if n < 0:
            r = round(x * power(x,n+1))
            return 1/r
        else:
            return x * power(x,n-1)

    except Exception as e:
        raise e
    
n = -2
x = 2

print(power(x,n))