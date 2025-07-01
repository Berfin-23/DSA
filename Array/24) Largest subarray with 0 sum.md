## Largest Subarray with 0 Sum (GeeksforGeeks) - Medium

Given an array `arr[]` containing both positive and negative integers, the task is to find the length of the largest subarray with a sum equal to 0.

[Link for the question](https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1)

**Example 1:**

> **Input:** `arr[] = [15, -2, 2, -8, 1, 7, 10, 23]`  
> **Output:** `5`  
> **Explanation:**  
> The largest subarray with a sum of 0 is `[-2, 2, -8, 1, 7]`.

**Example 2:**

> **Input:** `arr[] = [2, 10, 4]`  
> **Output:** `0`  
> **Explanation:**  
> There is no subarray with a sum of 0.

**Example 3:**

> **Input:** `arr[] = [1, 0, -4, 3, 1, 0]`  
> **Output:** `5`  
> **Explanation:**  
> The subarray is `[0, -4, 3, 1, 0]`.

**Constraints:**

- `1 ≤ arr.size() ≤ 10^6`
- `-10^3 ≤ arr[i] ≤ 10^3`

```Python
class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        max_len = 0
        prefix_map = {}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_len = i + 1
                
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
                
        return max_len
```
