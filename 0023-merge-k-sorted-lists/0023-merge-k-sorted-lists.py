class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # initialize heap with smallest of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)  # choose the smallest
            curr.next = node
            curr = curr.next
            if node.next:  # progress the chosen list
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next