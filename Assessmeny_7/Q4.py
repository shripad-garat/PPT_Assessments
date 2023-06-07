"""
<aside>
💡 **Question 4**

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

</aside>
"""

def reverse(s):
    try:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        
        s = " ".join(s)
        return s


    except Exception as e:
        raise e
    
s = "Let's take LeetCode contest"
print(reverse(s))