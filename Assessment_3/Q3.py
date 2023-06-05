"""
<aside>
💡 **Question 3**
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]

</aside>
"""


def perm(arr):
    try:
        ind0 = 0
        ind1 = 0
        for i in range(len(arr)-1,0,-1):
            if arr[i-1]<arr[i]:
                ind0 = i
        for i in range (len(arr)-1,0,-1):
            if arr[ind0]<arr[i]:
                ind1 = i
        arr[ind0], arr[ind1]= arr[ind1],arr[ind0]
        ind0+=1
        r = len(arr)-1
        while ind0<r:
            arr[ind0], arr[r]= arr[r],arr[ind0]
            r-=1
            ind0+=1
        return arr


    except Exception as e:
        raise e
    

nums = [1,2,3]
print(perm(nums))