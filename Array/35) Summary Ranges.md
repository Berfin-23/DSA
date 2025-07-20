# 228. Summary Ranges (LeetCode) - Easy

You are given a sorted unique integer array `nums`.

A range `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

[Link for the question](https://leetcode.com/problems/summary-ranges/)

## Examples

**Example 1:**

> **Input:** `nums = [0,1,2,4,5,7]` > **Output:** `["0->2","4->5","7"]` > **Explanation:** The ranges are:
>
> - `[0,2]` --> `"0->2"`
> - `[4,5]` --> `"4->5"`
> - `[7,7]` --> `"7"`

**Example 2:**

> **Input:** `nums = [0,2,3,4,6,8,9]` > **Output:** `["0","2->4","6","8->9"]` > **Explanation:** The ranges are:
>
> - `[0,0]` --> `"0"`
> - `[2,4]` --> `"2->4"`
> - `[6,6]` --> `"6"`
> - `[8,9]` --> `"8->9"`

## Constraints

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

## Solution

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        result = []

        start = nums[0]
        i = 0

        while i < len(nums):
            end = nums[i]
            if i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
                end = nums[i+1]
            else:
                end = nums[i]
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                start = nums[i+1] if i+1 < len(nums) else None
            i += 1

        return result
```
