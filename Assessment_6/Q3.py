"""
<aside>
💡 **Question 3**

Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    **Example 1:**

**Input:** arr = [2,1]

**Output:**

false
</aside>
"""

def isMount(arr):
    try:
        start = 0
        if len(arr) < 3:
            return False
        while start < len(arr)-1:
            if arr[start]>arr[start+1]:
                break
            start += 1
        while start < len(arr)-1:
            if arr[start] <arr[start+1]:
                return False
            start += 1
            
        return True

    except Exception as e:
        raise e
    
arr = [0,1,2,3,2,1]
print(isMount(arr))