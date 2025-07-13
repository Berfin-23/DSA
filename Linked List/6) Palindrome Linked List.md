# 234. Palindrome Linked List (LeetCode) - Easy

Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.

[Link for the question](https://leetcode.com/problems/palindrome-linked-list/)

**Example 1:**

![Palindrome Linked List Example 1](../images/palindrome_linked_list_1.png)

> **Input:** `head = [1,2,2,1]`  
> **Output:** `true`

**Example 2:**

![Palindrome Linked List Example 2](../images/palindrome_linked_list_2.png)

> **Input:** `head = [1,2]`  
> **Output:** `false`

**Constraints:**

- The number of nodes in the list is in the range `[1, 10^5]`.
- `0 <= Node.val <= 9`

```Python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
```