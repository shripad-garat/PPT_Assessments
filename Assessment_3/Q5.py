"""
<aside>
💡 **Question 5**
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

</aside>
"""


def inc(arr):
    try:
        for i in range(len(arr)-1,0,-1):
            arr[i] += 1
            if arr[i]+1 != 10:
                return arr
            
        return [1].extend(arr)


    except Exception as e:
        raise e
    
digits = [1,2,3]
print(inc(digits))