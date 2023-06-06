"""
<aside>
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

</aside>
"""

def distinct(arr1,arr2):
    try:
        ans0 = []
        ans1 = []
        n = len(arr1)
        m = len(arr2)
        index = max(n,m)
        for i in range(index):
            if i<n and (arr1[i] not in arr2):
                if arr1[i] not in ans0:
                    ans0.append(arr1[i])
            if i<m and (arr2[i] not in arr1):
                if arr2[i] not in ans1:
                    ans1.append(arr2[i])
        return [ans0,ans1]
    except Exception as e:
        raise e
    
nums1 = [1,2,3]
nums2 = [2,4,6]
print(distinct(nums1,nums2))