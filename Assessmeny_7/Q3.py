"""
<aside>
💡 **Question 3**

Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

</aside>"""

def sumOfString(s,t):
    try:
        n,m = len(s),len(t)
        ma = max(n,m)
        carry,i = 0,-1
        sum =''
        while(abs(i)<=ma):
            sub = 0 
            if abs(i) < n+1:
                sub = sub + int(s[i])
            if abs(i) < m+1:
                 sub = sub + int(t[i])
            sum = str( sub + carry) + sum
            carry = (sub)//10
            i -= 1
     
        return sum

    except Exception as e:
        raise e
    
num1 = "11"
num2 = "123"
print(sumOfString(num1,num2))