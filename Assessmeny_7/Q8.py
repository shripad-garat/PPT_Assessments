"""
<aside>
💡 **Question 8**

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

</aside>
"""

## slope = (x1-x2)/(y1-y2) == 1 for stright line

def strightLine(arr):
    try:
        for i in range(len(arr)-1):
            slope = (arr[i][0]-arr[i+1][0])/(arr[i][1]-arr[i+1][1])
            if slope != 1:
                return False
            
        return True

    except Exception as e:
        raise e
    
cor = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(strightLine(cor))