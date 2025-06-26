## Count Swaps to Group Even Numbers - Easy

You are given an integer array `nums` of length `n` containing both even and odd numbers.

Your task is to calculate the minimum number of adjacent swaps required to move all even numbers to the front of the array and all odd numbers to the end without changing the relative order among even and odd numbers themselves.

You must return the total number of swaps needed, without modifying the original array.

**Example 1:**

> **Input:** `nums = [1, 2, 3, 4, 5, 6]`  
> **Output:** `6`  
> **Explanation:**  
> We want to move even numbers (2, 4, 6) to the front while preserving their order.  
> Their current indices: 1, 3, 5  
> Their target indices: 0, 1, 2
>
> Swaps needed:
>
> - 2 moves from index 1 to 0 → 1 swap
> - 4 moves from index 3 to 1 → 2 swaps
> - 6 moves from index 5 to 2 → 3 swaps
>
> Total = 1 + 2 + 3 = 6

**Example 2:**

> **Input:** `nums = [2, 4, 6, 1, 3, 5]`  
> **Output:** `0`  
> **Explanation:**  
> Even numbers are already at the front. No swaps are needed.

**Constraints:**

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

```Python
def count_swaps_to_group_evens_front(arr):
    even_pos = 0
    swaps = 0
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0: 
            swaps += i - even_pos
            even_pos += 1
    
    return swaps

# Example
arr = [1, 2, 3, 4, 5, 6]
print(count_swaps_to_group_evens_front(arr))

```