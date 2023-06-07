"""
<aside>
💡 **Question 7**

Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".

</aside>
"""

def back(s,t):
    try:
        n,m = len(s),len(t)
        p,l = 0,0
        while(p<n or l<m):
            if s[p+1] =="#":
                p = p + 2
            if t[l+1] == "#":
                l = l + 2
            if s[p] != t[l]:
                return False
            l += 1
            p += 1
        
        return True


    except Exception as e:
        raise e
    
s = "ab#c"
t = "ad#c"
print(back(s,t))