"""
<aside>
💡 **Question 4**

Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

**Example 1:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

</aside>
"""

def bin(arr):
    try:
        cur_count = 0
        fin_c = 0
        c1 = 0
        c0 = 0
        for i in range(len(arr)):
            if arr[i] in [0,1]:
                if arr[i] == 0:
                    c0 += 1
                elif arr[i] == 1:
                    c1 += 1
                if c0 == c1:
                    cur_count += 2
            else:
                c0 = 0
                c1 = 0
                fin_c = cur_count

        return max(fin_c,cur_count)

    except Exception as e:
        raise e
    

nums = [0,1]
print(bin(nums))