"""
We want to find pair of indexes that subtracted gave us a desired difference. 
Create a function that given an array of integers and a desired difference returns the pair of indexes that met the condition.
 
Restrictions 
First element of tuple should always be lesser than second element 
Valid tuple examples: (0,1), (0, 10), (1, 3) 
Invalid tuple examples: (1,0), (3,2) 
While traversing numbers list, order of elements evaluated should not be inverted to test for desired difference (Difference should be calculated as i – j where i is the element first located in list) 
Desired difference may be negative 
Desired difference may be 0 
Numbers list may contain negative numbers 
List will only contain integers 
"""


def main(array: list, target: int):
    results = []
    for i in range(len(array)):
        for j in range(len(array[array[i]:])):
            if array[i] - array[j] == target:
                results.append((array[i], array[j]))

    return results


if __name__ == "__main__":
    l = [2,4,6,10,8,6,3,7,5]
    target = 2
    ans = main(l, target)
    print(ans)
