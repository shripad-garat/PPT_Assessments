"""
<aside>
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

</aside>
"""

def ununique(arr):
    try:
        temp = {}
        for i in range(len(arr)):
            if arr[i] in temp:
                temp[arr[i]] = temp[arr[i]] + 1
            else:
                temp[arr[i]] = 1

        if max(temp.values())>=2:
            return True
        else:
            return False


    except Exception as e:
        raise e
    
nums = [1,2,3,1]
print(ununique(nums))