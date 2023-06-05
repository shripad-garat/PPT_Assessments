"""
Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

def extract3sum(arr,val):
    try:
        
        arr = sorted(arr)
        nearest = None

        for i in range(len(arr)-2):
            pt1= i+1
            pt2=i+2
            while(pt1<pt2):
                current = arr[i]+arr[pt1]+arr[pt2]
                if (nearest==None):
                    nearest = current
                elif abs(current-val)<abs(nearest-val):
                    nearest = current

                if current >val:
                    pt2 -= 1

                else:
                    pt1 += 1

        return nearest
        

    except Exception as e:
        raise e
    

nums = [-1,2,1,-4]
target = 1
print(extract3sum(nums,target))