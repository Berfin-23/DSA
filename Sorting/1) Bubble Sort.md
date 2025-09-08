# 1. Bubble Sort (GeeksforGeeks) - Easy

Given an array `arr[]`, sort the array using the bubble sort algorithm.

[Link for the question](https://www.geeksforgeeks.org/problems/bubble-sort/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

## Examples

**Example 1:**

> **Input:** `arr = [4, 1, 3, 9, 7]`  
> **Output:** `[1, 3, 4, 7, 9]`

**Example 2:**

> **Input:** `arr = [10,9,8,7,6,5,4,3,2,1]`  
> **Output:** `[1,2,3,4,5,6,7,8,9,10]`

**Example 3:**

> **Input:** `arr = [1,2,3,4,5]`  
> **Output:** `[1,2,3,4,5]`

## Constraints

- `1 <= len(arr) <= 10^3`
- `1 <= arr[i] <= 10^3`


```python
class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
```
