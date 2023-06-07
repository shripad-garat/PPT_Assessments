"""
<aside>
💡 **Question 5**

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"

</aside>
"""


def reverse(s,k):
    try:
        n = len(s)
        s = list(s)
        if n <= k:
            return s[::-1]
        l,l2 = 0,2*k
        r,r2 = k -1,3*k - 1

        while(l<=r):
            s[l],s[r] = s[r],s[l]
            if n>=3*k:
                s[l2],s[r2] = s[r2],s[l2]
                l2 +=1
                r2 -= 1
            l += 1
            r -= 1

        return "".join(s)

    except Exception as e:
        raise e
    
s = "abcdefg"
k = 2
print(reverse(s,k))