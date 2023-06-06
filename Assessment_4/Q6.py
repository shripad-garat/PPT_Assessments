"""
<aside>
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

</aside>
"""

def sortedSqr(arr):
    try:
        l = 0 
        r = len(arr)-1
        while l<=r:
            if abs(arr[l])<=abs(arr[r]):
                arr[r] = arr[r]**2
                r-=1
            elif abs(arr[l])>abs(arr[r]):
                arr[l],arr[r]=arr[r],arr[l]
        
        return arr

    except Exception as e:
        raise e
    
nums = [-4,-1,0,3,10]
print(sortedSqr(nums))