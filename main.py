# Definition for singly-linked list.
class Node:

  def __init__(self, x, next=None):
    self.val = x
    self.next = next


class Solution:

  def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
    aH = headA
    bH = headB
    # A     1 - 2 - 3
    #                \
    #                 77 - 88
    #                /
    # B  12 - 22 - 33

    # Flags for checking cycling in the while =)
    flagA = 0
    flagB = 0

    def checkFlags(flagA, flagB):
      return flagA < 2 or flagB < 2

    while aH != bH and checkFlags(flagA, flagB):
      # print(' %d %d / %d %d' % (aH.val, bH.val, flagA, flagB))
      if aH and aH.next is not None:
        aH = aH.next
      else:
        # and the end of aH, go to headB !!! B !!!
        aH = headB
        flagA += 1

      if bH and bH.next is not None:
        bH = bH.next
      else:
        # and the end of bH, go to headA !!! A !!!
        bH = headA
        flagB += 1

    return aH if checkFlags(flagA, flagB) else None


my = Solution()

tail = Node(777, Node(88, Node(999)))
l0 = Node(1, Node(2, Node(3, Node(4, tail))))
# l0 = None
l00 = Node(12, Node(22, Node(33, tail)))

ans = my.getIntersectionNode(l0, l00)

print(ans)
