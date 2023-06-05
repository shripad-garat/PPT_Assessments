"""
Question 2
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

def  Unique(arr,val):
    try:
        if len(arr)==0:
            return arr
        uniq = []
        arr = sorted(arr)
        l = 0
        r = len(arr)-1
        n = len(arr)
        for i in range(n-3):
            for j in range(i+1,n-2):
                l = j + 1
                r = n - 1
                while l<r:
                    sum = arr[i] + arr[j] + arr[l] + arr[r]
                    if sum < val:
                        l = l + 1
                    elif sum > val:
                        r = r - 1
                    else:
                        uniq.append([arr[i] , arr[j] , arr[l] , arr[r]])
                        l = l + 1
                        r = r - 1
        
        return uniq



    except Exception as e:
        raise  e
    

nums = [1,0,-1,0,-2,2]
target = 0
print(Unique(nums,target))