# 2095. Delete the Middle Node of a Linked List (LeetCode) - Medium

You are given the `head` of a linked list. Delete the middle node, and return the `head` of the modified linked list.

The middle node of a linked list of size `n` is the `⌊n / 2⌋`th node from the start using 0-based indexing, where `⌊x⌋` denotes the largest integer less than or equal to `x`.

For `n = 1, 2, 3, 4, and 5`, the middle nodes are `0, 1, 1, 2, and 2`, respectively.

[Link for the question](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

**Example 1:**

![Delete Middle Node Example 1](../images/delete_the_middle_node_of_a_linked_list_1.png)

> **Input:** `head = [1,3,4,7,1,2,6]`  
> **Output:** `[1,3,4,1,2,6]`  
> **Explanation:** The above figure represents the given linked list. The indices of the nodes are written below. Since `n = 7`, node `3` with value `7` is the middle node, which is marked in red. We return the new list after removing this node.

**Example 2:**

![Delete Middle Node Example 2](../images/delete_the_middle_node_of_a_linked_list.png)

> **Input:** `head = [1,2,3,4]`  
> **Output:** `[1,2,4]`  
> **Explanation:** The above figure represents the given linked list. For `n = 4`, node `2` with value `3` is the middle node, which is marked in red.

**Example 3:**

![Delete Middle Node Example 3](../images/delete_the_middle_node_of_a_linked_list_3.png)

> **Input:** `head = [2,1]`  
> **Output:** `[2]`  
> **Explanation:** The above figure represents the given linked list. For `n = 2`, node `1` with value `1` is the middle node, which is marked in red. Node `0` with value `2` is the only node remaining after removing node `1`.

**Constraints:**

- The number of nodes in the list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`

```Python
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next

        return head
```