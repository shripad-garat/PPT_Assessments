"""
<aside>
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

</aside>
"""

def common(arr1,arr2,arr3):
    try:
        n = len(arr1)
        m = len(arr2)
        o = len(arr3)
        i,j,k = 0,0,0
        com = []

        while( i<n and j<m and k<o):
            if (arr1[i]==arr2[j])and(arr2[j]==arr3[k]):
                com.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif (arr1[i]<arr2[j]):
                i += 1
            elif (arr2[j]<arr3[k]):
                j += 1
            else:
                k += 1
        return com
    
    except Exception as e:
        raise e
    
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
print(common(arr1,arr2,arr3))