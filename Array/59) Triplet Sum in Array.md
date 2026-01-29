# 59. Triplet Sum in Array (GeeksforGeeks) - Medium

Given an array `arr[]` and an integer `target`, determine if there exists a triplet in the array whose sum equals the given target.

Return `true` if such a triplet exists, otherwise, return `false`.

[Link for the question](https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1)

## Examples

**Example 1:**

> **Input:** `arr = [1, 4, 45, 6, 10, 8], target = 13`  
> **Output:** `true`  
> **Explanation:** The triplet {1, 4, 8} sums up to 13.

**Example 2:**

> **Input:** `arr = [1, 2, 4, 3, 6, 7], target = 10`  
> **Output:** `true`  
> **Explanation:** The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.

**Example 3:**

> **Input:** `arr = [40, 20, 10, 3, 6, 7], target = 24`  
> **Output:** `false`  
> **Explanation:** No triplet in the array sums to 24.

## Constraints

- `3 <= len(arr) <= 5 * 10^3`
- `0 <= arr[i], target <= 10^5`

## Solution (Python)

This solution uses a two-pointer approach after sorting. For each element, we use two pointers to find if there's a pair that sums with the current element to reach the target.

```python
class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)
        
        # Edge Case: Not enough elements to form a triplet
        if n < 3:
            return False
            
        for i in range(n - 2):
            # Optimization 1: Skip duplicate values for the first element
            if i > 0 and arr[i] == arr[i - 1]:
                continue
                
            # Optimization 2: Smallest possible sum from this point
            # If the current smallest triplet is already > target, no need to look further
            if arr[i] + arr[i+1] + arr[i+2] > target:
                break
                
            # Optimization 3: Largest possible sum from this point
            # If current element + two largest elements < target, i is too small
            if arr[i] + arr[n-2] + arr[n-1] < target:
                continue

            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return False


if __name__ == "__main__":
    # Quick sanity checks
    print(tripletSum([1, 4, 45, 6, 10, 8], 13))  # True
    print(tripletSum([1, 2, 4, 3, 6, 7], 10))    # True
    print(tripletSum([40, 20, 10, 3, 6, 7], 24)) # False
```
