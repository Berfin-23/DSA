# Count Subarrays With Given Sum (Custom) - Medium

Given an array of positive integers `nums` and an integer `target`, return the number of contiguous subarrays whose sum equals `target`.

## Examples

**Example 1:**

> **Input:** `nums = [1,2,1]`, `target = 3` > **Output:** `2` > **Explanation:** The subarrays `[1,2]` and `[2,1]` both sum to `3`.

**Example 2:**

> **Input:** `nums = [1,1,1]`, `target = 2` > **Output:** `2` > **Explanation:** The subarrays `[1,1]` at indices `(0,1)` and `(1,2)` both sum to `2`.

## Constraints

- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 1000`
- `1 <= target <= 10^9`

```python
n = int(input())
target = int(input())
nums = list(map(int, input().split()))

count = 0
left = 0
current_sum = 0

for right in range(n):
    current_sum += nums[right]

    while current_sum > target and left <= right:
        current_sum -= nums[left]
        left += 1

    if current_sum == target:
        count += 1

print(count)
```