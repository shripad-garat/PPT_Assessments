"""
Question 5
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6
"""

## we will sort and return the last 3 element product 

def product(arr):
    try:
        arr = sorted(arr)
        prod = arr[-3]*arr[-2]*arr[-1]
        return prod
    except Exception as e:
        raise e
    
nums = [1,2,3]
print(product(nums))