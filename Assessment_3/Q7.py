"""
Question 7
You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
"""

def missRange(arr,l,u):
    try:
        miss = []
        if arr[0]!=l:
            miss.append([l,arr[0]])
        for i in range(len(arr)-1):
            if arr[i]+1!=arr[i+1]:
                miss.append([arr[i]+1,arr[i+1]-1])
        if arr[len(arr)-1]!=u:
                miss.append([arr[len(arr)-1]+1,u])

        return miss

    except Exception as e:
        raise e
    
nums = [0,1,3,50,75]
lower = 0
upper = 99
print(missRange(nums,lower,upper))