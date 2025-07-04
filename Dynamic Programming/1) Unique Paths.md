# 62. Unique Paths (LeetCode) - Medium

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

[Link for the question](https://leetcode.com/problems/unique-paths/)

**Example 1:**

![Unique Paths Grid](../images/unique_paths.png)

> **Input:** `m = 3`, `n = 7`  
> **Output:** `28`

**Example 2:**

> **Input:** `m = 3`, `n = 2`  
> **Output:** `3`  
> **Explanation:** From the top-left corner, there are a total of `3` ways to reach the bottom-right corner:
>
> 1. Right → Down → Down
> 2. Down → Down → Right
> 3. Down → Right → Down

**Constraints:**

- `1 <= m, n <= 100`

#### Answer 1
```Python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        below_row = [1] * n

        for i in range(m - 1):
            new_row = [1] * n
            
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + below_row[j]

            below_row = new_row

        return below_row[0]
```

#### Answer 2
```Python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
```