"""

💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][
"""


def indices(arr,target):
    try:
        arr = arr
        target = target
        for i in range(len(arr)):
            sec_point = target - arr[i]
            if sec_point in arr:
                return [i,arr.index(sec_point)]

    except Exception as e:
        raise e
    
ip = [2,7,11,15]
target = 9
print(indices(ip,target))