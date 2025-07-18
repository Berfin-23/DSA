# 21. Merge Two Sorted Lists (LeetCode) - Easy

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

[Link for the question](https://leetcode.com/problems/merge-two-sorted-lists/)

## Examples

**Example 1:**

![Merge Two Sorted Lists](../images/merge_two_sorted_lists.png)

> **Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]` > **Output:** `[1,1,2,3,4,4]`

**Example 2:**

> **Input:** `list1 = []`, `list2 = []` > **Output:** `[]`

**Example 3:**

> **Input:** `list1 = []`, `list2 = [0]` > **Output:** `[0]`

## Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

```Python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
```