# 2. Selection Sort (GeeksforGeeks) - Easy

Given an array `arr`, use selection sort to sort `arr[]` in increasing order.

[Link for the question](https://www.geeksforgeeks.org/problems/selection-sort/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article)

## Examples

**Example 1:**

> **Input:** `arr = [4, 1, 3, 9, 7]`  
> **Output:** `[1, 3, 4, 7, 9]`

**Example 2:**

> **Input:** `arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`  
> **Output:** `[1,2,3,4,5,6,7,8,9,10]`

**Example 3:**

> **Input:** `arr = [38, 31, 20, 14, 30]`  
> **Output:** `[14, 20, 30, 31, 38]`

## Constraints

- `1 <= len(arr) <= 10^3`
- `1 <= arr[i] <= 10^6`


```python
class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n):
            min_ind = i
            
            for j in range(i+1, n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
                    
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
            
        return arr
```
