"""
<aside>
💡 **Question 1**

Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"

**Output:** 231

**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

Deleting "t" from "eat" adds 116 to the sum.

At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

</aside>"""

def sequal(word1,word2):
    try:
        arr1 = list(word1)
        arr2 = list(word2)
        len1 = len(arr1)
        len2 = len(arr2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        for i in range(1, len1 + 1):
            dp[i][0] = i
        
        for i in range(1, len2 + 1):
            dp[0][i] = i
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        
        return dp[len1][len2]

    except Exception as e:
        raise e
    

word2 = "eat"
word1 = "sea"

print(sequal(word1,word2))