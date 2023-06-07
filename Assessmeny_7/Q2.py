"""
<aside>
💡 **Question 2**

Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

</aside>
"""

## As we can see the only digits which can remain valid after 180 d rotation are 0,1,6,8,9 
## And posible combination would be (0,0)(1,1)(6,9)(8,8)(9,6)
## Lets use two pointer approch and verify if this is the combination they are having

def strob(s):
    try:
        checks = [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
        l =0
        r = len(s) - 1
        while(l<=r):
            if (s[l],s[r]) not in checks:
                return False
            l += 1
            r -= 1
        return True

    except Exception as e:
        raise e
    
num = "69"
print(strob(num))