from add_two_um import Solution, ListNode

def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def main():
    l1 =  list_to_linkedlist([2, 4, 3])

    print(Solution.addTwoNumbers(l1 = l1, l2 = list_to_linkedlist([5, 6, 4])))

if __name__ == '__main__':
    main()
