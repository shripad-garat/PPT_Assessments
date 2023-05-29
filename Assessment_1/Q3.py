"""
<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

</aside>
"""

def searchg(arr,val):
    try:
        l = 0
        r = len(arr)-1
        while(l<r):
            mid = (l+r)//2
            if arr[mid] == val:
                return mid
            elif (arr[mid+1]>val) and (arr[mid-1]<val):
                return mid
            elif arr[mid]<val:
                l = mid +1
            else:
                r = mid - 1

    except Exception as e:
        raise e
    

nums = [1,3,5,6]
target = 5
print(searchg(nums,target))