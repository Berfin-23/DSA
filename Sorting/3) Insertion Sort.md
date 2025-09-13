# 3. Insertion Sort (GeeksforGeeks) - Easy

Given an array `arr[]` of positive integers. The task is to complete the insertsort() function which is used to implement Insertion Sort.

[Link for the question](https://www.geeksforgeeks.org/problems/insertion-sort/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

## Examples

**Example 1:**

> **Input:** `arr = [4, 1, 3, 9, 7]`  
> **Output:** `[1, 3, 4, 7, 9]`

**Example 2:**

> **Input:** `arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`  
> **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Example 3:**

> **Input:** `arr = [4, 1, 9]`  
> **Output:** `[1, 4, 9]`

## Constraints

- `1 <= len(arr) <= 1000`
- `1 <= arr[i] <= 1000`


```python
def insertionSort(arr):
class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i] 
            j = i - 1


            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key 
        return arr
```
