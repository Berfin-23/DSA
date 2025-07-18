# 876. Middle of the Linked List (LeetCode) - Easy

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

[Link for the question](https://leetcode.com/problems/middle-of-the-linked-list/)

**Example 1:**

![Middle of Linked List Example 1](../images/middle_of_the_linked_list_1.png)

> **Input:** `head = [1,2,3,4,5]`  
> **Output:** `[3,4,5]`  
> **Explanation:** The middle node of the list is node `3`.

**Example 2:**

![Middle of Linked List Example 2](../images/middle_of_the_linked_list_2.png)

> **Input:** `head = [1,2,3,4,5,6]`  
> **Output:** `[4,5,6]`  
> **Explanation:** Since the list has two middle nodes with values `3` and `4`, we return the second one.

**Constraints:**

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

```Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
```