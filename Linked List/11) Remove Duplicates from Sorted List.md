# 83. Remove Duplicates from Sorted List (LeetCode) - Easy

Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

[Link for the question](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Examples

**Example 1:**

![Remove Duplicates Example 1](../images/remove_duplicates_from_sorted_list_1.png)

> **Input:** `head = [1,1,2]` > **Output:** `[1,2]`

**Example 2:**

![Remove Duplicates Example 2](../images/remove_duplicates_from_sorted_list_2.png)

> **Input:** `head = [1,1,2,3,3]` > **Output:** `[1,2,3]`

## Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be sorted in ascending order.

```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
```