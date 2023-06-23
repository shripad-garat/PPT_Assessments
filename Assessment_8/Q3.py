"""
<aside>
💡 **Question 3**

Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.

**Example 1:**

**Input:** word1 = "sea", word2 = "eat"

**Output:** 2

**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

</aside>
"""

def steps(word1,word2):
    try:
        m, n = len(word1), len(word2)
        if m < n: 
            word1, word2, m, n = word2, word1, n, m
        Last, Curr = [0] * (n + 1), [0] * (n + 1)
        for c1 in word1:
            for j in range(n):
                Curr[j+1] = Last[j] + 1 if c1 == word2[j] else max(Curr[j], Last[j+1])
            Last, Curr = Curr, Last
        return m + n - 2 * Last[n]
            

    except Exception as e:
        raise e
    
word1 = "sea"
word2 = "eat"
print(steps(word1,word2))