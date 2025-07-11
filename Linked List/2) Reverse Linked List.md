# 206. Reverse Linked List (LeetCode) - Easy

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

[Link for the question](https://leetcode.com/problems/reverse-linked-list/)

**Example 1:**

![Reverse Linked List Example 1](../images/reverse_linked_list_1.png)

> **Input:** `head = [1,2,3,4,5]`  
> **Output:** `[5,4,3,2,1]`

**Example 2:**

![Reverse Linked List Example 2](../images/reverse_linked_list_2.png)

> **Input:** `head = [1,2]`  
> **Output:** `[2,1]`

**Example 3:**

> **Input:** `head = []`  
> **Output:** `[]`

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

#### Answer 1
```Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node
```

#### Answer 2

```Python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
```