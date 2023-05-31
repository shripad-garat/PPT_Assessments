"""
Question 3
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].
"""

def harmonioun(arr):
    try:
        min_e = 0
        max_e = 0
        harmon = [] 
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==1:
                max_e = max(arr[i],arr[i+1])
                min_e = min(arr[i],arr[i+1])
                harmon.append(arr[i])
            elif arr[i]==max_e or arr[i]==min_e:
                harmon.append(arr[i])

        return len(harmon)



    except Exception as e:
        raise e
    

nums = [1,3,2,2,5,2,3,7]
print(harmonioun(nums))