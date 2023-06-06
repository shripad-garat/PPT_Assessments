"""
<aside>
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

</aside>
"""

def starecase(num):
    try:
        i = 0
        while(i<num):
            i = i + 1
            num = num - i
        return i

    except Exception as e:
        raise e
        
n = 5
print(starecase(n))