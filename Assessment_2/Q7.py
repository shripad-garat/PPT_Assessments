"""
Question 7
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true
"""

def monotonic(arr):
    try:
        counter = None
        mono = None
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1] and (counter==True or counter == None):
                counter = True
            elif arr[i]<=arr[i+1] and (counter==False or counter == None):
                counter = False
            else:
                return False
        
        return True

    except Exception as e:
        raise e 
    

nums = [1,2,2,3]
print(monotonic(nums))