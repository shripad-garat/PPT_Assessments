"""
Question 4
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""


def flowerpot(arr,n):
    try:
        counter = 0
        for i in range(len(arr)-1):
            if arr[i-1]==0 and arr[i+1]==0:
                counter += 1
        
        if counter >= n:
            return True
        else:
            return False

    except Exception as e:
        raise e
    
flowerbed = [1,0,0,0,1]
n = 1
print(flowerpot(flowerbed,n=n))