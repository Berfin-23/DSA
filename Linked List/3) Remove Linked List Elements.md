# 203. Remove Linked List Elements (LeetCode) - Easy

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return the new head.

[Link for the question](https://leetcode.com/problems/remove-linked-list-elements/)

**Example 1:**

![Remove Linked List Elements](remove_linked_list_elements.png)

> **Input:** `head = [1,2,6,3,4,5,6]`, `val = 6`  
> **Output:** `[1,2,3,4,5]`

**Example 2:**

> **Input:** `head = []`, `val = 1`  
> **Output:** `[]`

**Example 3:**

> **Input:** `head = [7,7,7,7]`, `val = 7`  
> **Output:** `[]`

**Constraints:**

- The number of nodes in the list is in the range `[0, 10^4]`.
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

```Python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        previous, current = dummy, head

        while current:
            next = current.next

            if current.val == val:
                previous.next = next
            else:
                previous = current

            current = next

        return dummy.next
```