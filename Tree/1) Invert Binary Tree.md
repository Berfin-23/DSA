invert_binary_tree_1.png
invert_binary_tree_2.png

# 226. Invert Binary Tree (LeetCode) - Easy

Given the root of a binary tree, invert the tree, and return its root.

[Link for the question](https://leetcode.com/problems/invert-binary-tree/)

## Examples

**Example 1:**

![Invert Binary Tree 1](../images/invert_binary_tree_1.png)

> **Input:** `root = [4,2,7,1,3,6,9]` > **Output:** `[4,7,2,9,6,3,1]`

**Example 2:**

![Invert Binary Tree 2](../images/invert_binary_tree_2.png)

> **Input:** `root = [2,1,3]` > **Output:** `[2,3,1]`

**Example 3:**

> **Input:** `root = []` > **Output:** `[]`

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
```