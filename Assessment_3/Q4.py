"""
Question 4
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def bin(arr,val):
    try:
        start = 0
        end = len(arr)-1
        while start<end:
            mid = (start+end)//2
            if (arr[mid]<val and arr[mid+1]<val) or arr[mid]==val:
                return mid
            elif arr[mid]<val:
                start = mid + 1
            else:
                end = mid



    except Exception as e:
        raise e
    

nums = [1,3,5,6]
target = 5
print(bin(nums,target))