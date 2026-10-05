import heapq

# heapq siempre tiene acceso rapido al menor/mayor valor. Sólo se garantiza qu el mas pequeño está arriba

# min-Heap: [ ,  , ]
# minHeap[0] -> the minor element
# If we store the k-largest elements minHeap[0] must be the k-larest element.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) 
        

    def add(self, val: int) -> int:
        # for each add operation we should pop the minor one.
        # minHeap allow has in O(1) to find the minor element.
        heapq.heappush(self.minHeap, val) # {3, 2, 1} -> {3, 2, 1, 5}
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # {5,2,3 }
        
        return self.minHeap[0]