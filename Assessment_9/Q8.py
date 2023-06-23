"""
<aside>
💡 **Question 8**

Given an array, find a product of all array elements.

**Example 1:**

Input  : arr[] = {1, 2, 3, 4, 5}
Output : 120
**Example 2:**

Input  : arr[] = {1, 6, 3}
Output : 18

</aside>
"""

def prod(s):
    try:
        if len(s)==0:
            return 1
        return s[0]*prod(s[1:])
    except Exception as e:
        raise e
    
s = [1, 2, 3, 4, 5]
print(prod(s))