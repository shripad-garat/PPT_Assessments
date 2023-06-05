"""
uestion 6
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""


def nonTwice(arr):
    try:
        for i in range(len(arr)):
            if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]:
                return arr[i]

    except Exception as e :
        raise e
    
nums = [2,2,1]
print(nonTwice(nums))