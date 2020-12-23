# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        previous = None
        firstNode = None
        carryOver = 0
        while l1 is not None or l2 is not None:
            firstNum = l1.val if l1 is not None else 0
            secondNum = l2.val if l2 is not None else 0
            sum = firstNum + secondNum + carryOver
            carryOver = sum // 10
            sum = sum % 10
            if previous is None:
                previous = ListNode(sum)
                firstNode = previous
            else:
                previous.next = ListNode(sum)
                previous = previous.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carryOver > 0:
            previous.next = ListNode(carryOver)

        return firstNode


if __name__ == '__main__':
    solution = Solution()
    firstList = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    secondList = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    sum = solution.addTwoNumbers(firstList, secondList)
    print(sum.val)
    while sum.next is not None:
        sum = sum.next
        print(sum.val)
