# Longest Subarray with Sum K (GeeksforGeeks) - Medium

[GeeksforGeeks - Longest Sub-Array with Sum K](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)

Given an array `arr[]` containing integers and an integer `k`, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value `k`. If there is no subarray with sum equal to `k`, return `0`.

## Examples

> **Example 1:**
>
> **Input:** `arr[] = [10, 5, 2, 7, 1, -10]`, `k = 15`
>
> **Output:** `6`
>
> **Explanation:** Subarrays with sum = 15 are `[5, 2, 7, 1]`, `[10, 5]` and `[10, 5, 2, 7, 1, -10]`. The length of the longest subarray with a sum of 15 is 6.

> **Example 2:**
>
> **Input:** `arr[] = [-5, 8, -14, 2, 4, 12]`, `k = -5`
>
> **Output:** `5`
>
> **Explanation:** Subarrays with sum = -5 are `[-5]` and `[-5, 8, -14, 2, 4]`. The length of the longest subarray with a sum of -5 is 5.

> **Example 3:**
>
> **Input:** `arr[] = [10, -10, 20, 30]`, `k = 5`
>
> **Output:** `0`
>
> **Explanation:** No subarray with sum = 5 is present in `arr[]`.

## Constraints

- `1 ≤ arr.size() ≤ 10^5`
- `-10^4 ≤ arr[i] ≤ 10^4`
- `-10^9 ≤ k ≤ 10^9`

```python
class Solution:
    def lenOfLongSubarr(self, arr, k):
        # Dictionary to store (prefix_sum: earliest_index)
        sum_dict = {}

        max_len = 0     # Will hold our final answer
        curr_sum = 0    # Running total

        n = len(arr)

        for i in range(n):
            curr_sum += arr[i]  # Add current element to the running total

            # Case 1: The prefix sum from the very beginning exactly matches K.
            # This is the longest possible subarray up to index i.
            if curr_sum == k:
                max_len = i + 1

            # Case 2: Check if we have seen (curr_sum - k) before.
            # If yes, we found a subarray that adds up to K!
            if (curr_sum - k) in sum_dict:
                # Calculate the length of this subarray
                # length = current index - index where we saw (curr_sum - k)
                current_subarray_len = i - sum_dict[curr_sum - k]

                # Update max_len if this subarray is longer than previous ones
                max_len = max(max_len, current_subarray_len)

            # Finally, record the curr_sum and its index in the dictionary.
            # CRITICAL: We only add it if it's NOT already in the dictionary.
            # If it's already there, keeping the older index is better because
            # an older (smaller) index will result in a longer subarray later!
            if curr_sum not in sum_dict:
                sum_dict[curr_sum] = i

        return max_len
```
