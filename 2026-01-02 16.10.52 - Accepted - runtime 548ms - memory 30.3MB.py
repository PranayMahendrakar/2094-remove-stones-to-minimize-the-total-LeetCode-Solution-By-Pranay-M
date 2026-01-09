class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        
        # Use max heap (negate values for Python's min heap)
        heap = [-p for p in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            # Get largest pile
            largest = -heapq.heappop(heap)
            # Remove floor(largest/2) stones
            new_pile = largest - largest // 2
            heapq.heappush(heap, -new_pile)
        
        return -sum(heap)