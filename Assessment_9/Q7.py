"""
<aside>
💡 **Question 7**

Given a string S, the task is to write a program to print all permutations of a given string.

**Example 1:**

***Input:***

*S = “ABC”*

***Output:***

*“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

**Example 2:**

***Input:***

*S = “XY”*

***Output:***

*“XY”, “YX”*

</aside>
"""

def permi(s,l):
    try:
        r = len(s)
        if l == r:
            print("".join(s))
        else:
            for i in range(l, r):
                s[l], s[i] = s[i], s[l]
                permi(s, l+1)
                s[l], s[i] = s[i], s[l] 
    except Exception as e:
        raise e
    

s = "ABC"
permi(permi(list(s),0))