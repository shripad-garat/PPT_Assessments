"""
Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""

def meet(arr):
    try:
        for i in range(len(arr)-1):
            if arr[i][1]>arr[i+1][0]:
                return False
        return True


    except Exception as e:
        raise e

intervals = [[0,30],[5,10],[15,20]]
print(meet(intervals))