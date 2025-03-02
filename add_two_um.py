from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_copy = l1
        l2_copy = l2

        my_num1 = []
        next_num = 0

        while l1_copy and l2_copy:

            summ_val_number = l1_copy.val + l2_copy.val + next_num
            val_number = summ_val_number % 10
            next_num = summ_val_number // 10

            my_num1.append(val_number)

            l1_copy = l1_copy.next
            l2_copy = l2_copy.next

        while l1_copy:
            next_num_2 = next_num + l1_copy.val
            val_number = next_num_2 % 10
            next_num = next_num_2 // 10

            my_num1.append(val_number)
            l1_copy = l1_copy.next

        while l2_copy:
            next_num_2 = next_num + l2_copy.val
            val_number = next_num_2 % 10
            next_num = next_num_2 // 10

            my_num1.append(val_number)
            l2_copy = l2_copy.next

        init_list_node = ListNode(my_num1[0])
        curr_node = init_list_node
        i = 1

        while my_num1 and i < len(my_num1):
            curr_node.next = ListNode(my_num1[i])
            curr_node = curr_node.next
            i += 1

        if next_num != 0:
            curr_node.next = ListNode(next_num)
        return init_list_node