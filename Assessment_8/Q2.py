"""
<aside>
💡 **Question 2**

Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

**Example 1:**

**Input:** s = "()"

**Output:**

true

</aside>
"""


def valid(s):
    try:
        a = 0
        b = 0
        c = 0

        for i in s:
            if i == '(':
                a += 1
            elif i == ')':
                b += 1
            else:
                c += 1
        if (abs(a-b) - c) == 0:
            return True
        else:
            return False
    except Exception as e:
        raise e
    

s = "()"
print(valid(s))