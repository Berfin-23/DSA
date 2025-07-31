# 110. Balanced Binary Tree (LeetCode) - Easy

Given a binary tree, determine if it is height-balanced.

[Link for the question](https://leetcode.com/problems/balanced-binary-tree/)

## Examples

**Example 1:**

![Balanced Binary Tree](../images/balanced_binary_tree.png)

> **Input:** `root = [3,9,20,null,null,15,7]` > **Output:** `true`

**Example 2:**

![Balanced Binary Tree 1](../images/balanced_binary_tree_1.png)

> **Input:** `root = [1,2,2,3,3,null,null,4,4]` > **Output:** `false`

**Example 3:**

> **Input:** `root = []` > **Output:** `true`

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            balanced = (left [0] and right[0]) and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
```
