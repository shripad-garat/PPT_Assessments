"""
<aside>
💡 **Question 6**

Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true

</aside>
"""

def shiftCheck(s,g):
    try:
        n = len(s)
        s = list(s)
        for i in range(n):
            s = s[1:] + s[:1]
            if "".join(s) == g:
                return True
            
        return False

    except Exception as e:
        raise e
    

s = "abcde"
goal = "cdeab"
print(shiftCheck(s,goal))