# 11. Container With Most Water (LeetCode) - Medium

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

[Link for the question](https://leetcode.com/problems/container-with-most-water/)

## Examples

**Example 1:**

![Container With Most Water](../images/container_with_most_water.png)

> **Input:** `height = [1,8,6,2,5,4,8,3,7]` > **Output:** `49` > **Explanation:** The above vertical lines are represented by array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is `49`.

**Example 2:**

> **Input:** `height = [1,1]` > **Output:** `1`

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea
```