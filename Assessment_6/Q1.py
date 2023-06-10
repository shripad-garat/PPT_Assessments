"""
<aside>
💡 **Question 1**

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

**Input:** s = "IDID"

**Output:**

[0,4,1,3,2]

</aside>
"""

def perm(s):
    try:
        mins = 0
        maxs = len(s)
        l = []
        for i in range(len(s)):
            if s[i] == 'D':
                l.append(maxs)
                maxs -= 1
            else:
                l.append(mins)
                mins += 1

        return l
    except Exception as e:
        raise e
    
s = "IDID"
print(perm(s))
