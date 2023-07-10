"""
<aside>
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

**Example 1:**

```
Input: n = 27
Output: true
Explanation: 27 = 33
```

**Example 2:**

```
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

```

**Example 3:**

</aside>
"""

def ispower_3(n):
    try:
        if n==1:
            return True
        if n%3 != 0:
            return False
        return ispower_3(abs(n/3))

    except Exception as e:
        raise e
    
n = 27
print(ispower_3(n))