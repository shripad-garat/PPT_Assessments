"""
<aside>
💡 **Question 1**

Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

</aside>
"""


def isomorphic(s,t):
    try:
        if len(s)!=len(t):
            return False
        h = {}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = t[i]
            else:
                if h[s[i]]!=t[i]:
                    return False
                
        return True


    except Exception as e:
        raise e
    

#s = "egg"
#t = "add"
s = "foo"
t = "bar"
print(isomorphic(s,t))