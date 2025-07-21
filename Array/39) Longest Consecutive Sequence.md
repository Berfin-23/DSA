# 128. Longest Consecutive Sequence (LeetCode) - Medium

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

[Link for the question](https://leetcode.com/problems/longest-consecutive-sequence/)

## Examples

**Example 1:**

> **Input:** `nums = [100,4,200,1,3,2]` > **Output:** `4` > **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is `4`.

**Example 2:**

> **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]` > **Output:** `9`

**Example 3:**

> **Input:** `nums = [1,0,1,2]` > **Output:** `3`

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashSet = set(nums)

        max_length = 1

        for num in hashSet:
            if num - 1 not in hashSet and num + 1 in hashSet:
                current_length = 1
                while num + 1 in hashSet:
                    current_length += 1
                    num += 1
                max_length = max(max_length, current_length)

        return max_length
```