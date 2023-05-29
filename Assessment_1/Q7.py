"""
<aside>
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

</aside>
"""

def move0(arr):
    try:
        pointer = 0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[pointer]= arr[i]
                pointer = pointer + 1

        while(pointer<len(arr)):
            arr[pointer]=0
            pointer = pointer + 1
            
        return arr

    except Exception as e:
        raise e
    


nums = [0,1,0,3,12]
print(move0(nums))
