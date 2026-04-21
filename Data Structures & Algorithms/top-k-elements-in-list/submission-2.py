class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        
        heap = []
        for num,c in count.items():
            heapq.heappush(heap, (c, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res