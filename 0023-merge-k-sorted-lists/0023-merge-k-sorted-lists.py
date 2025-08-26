class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialize heap with smallest of each list
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)

        dummy = ListNode()
        curr = dummy

        heappush, heappop = heapq.heappush, heapq.heappop

        while heap:
            val, i, node = heappop(heap)    # choose the smallest
            curr.next = node
            curr = curr.next
            if node.next:  # progress the chosen list
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next