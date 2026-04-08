# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
a list represents a number in reverse order.
ex: 321 = [1, 2, 3]

we want to sum two lists l1 and l2 and return it as a list itself.
ex: [1, 2, 3] + [4, 5, 6] = 321 + 654 = 975 = [5, 7, 9]

Solution: create a func that converts a list to a number using multiples of 10:
ex: [1, 2, 3] -> 1 * 1 + 2 * 10 + 3 * 100 = 1 + 20 + 300 = 321
ex: [4, 5, 6] -> 4 * 1 + 5 * 10 + 6 * 100 = 4 + 50 + 600 = 654

sum the two numbers, then do the opposite by converting sum into a list using division by 10 and modulus:
ex: 975 -> 975 % 10 = 5, 97 % 10 = 7, 9 % 10 = 9
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        return self.get_list(num1 + num2)

    def get_num(self, head):
        number = 0
        multiple = 1

        cur = head
        while cur:
            number += cur.val * multiple
            multiple *= 10
            cur = cur.next

        return number

    def get_list(self, num):
        dummy = ListNode()
        cur = dummy

        # edge case
        if num == 0:
            return ListNode(0)

        while num > 0:
            remainder = num % 10
            num = num // 10
            cur.next = ListNode(remainder, None)
            cur = cur.next

        return dummy.next