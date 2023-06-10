"""
<aside>
💡 **Question 5**

The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

**Example 1:**

**Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

**Output:** 40

**Explanation:**

We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

</aside>
"""

def poduct(arr1,arr2):
    try:
        sum = 0
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        n = len(arr1) 
        l = 0
        r = len(arr1) - 1
        while(l<n):
            sum += arr1[l]*arr2[r]
            l += 1
            r -= 1
        return sum
    except Exception as e:
        raise e
    
nums1 = [5,3,4,2]
nums2 = [4,2,2,5]
print(poduct(nums1,nums2))