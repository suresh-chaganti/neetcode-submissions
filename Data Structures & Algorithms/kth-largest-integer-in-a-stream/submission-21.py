class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k 
    #     self.nums = nums
        

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     sorted_nums = sorted(self.nums)
    #     return sorted_nums[-self.k]

        
    # We want to find the Kth largest element.
    # Instead of tracking all largest elements directly, we keep the K largest elements
    # and return the smallest among them.

    # Example: nums = [1,2,4,5,8,9,56,45,67], k = 3
    # The 3rd largest element is 45.

    # Approach:
    # 1. Convert the list into a min-heap using heapq.
    #    A min-heap ensures the smallest element is always at index 0.

    # 2. Remove elements until only K elements remain in the heap.
    #    Each pop removes the smallest element in the heap.
    #    This gradually eliminates the smaller numbers.

    # 3. After removing (n - k) elements, the heap contains the K largest elements.

    # 4. The root of the heap (heap[0]) is the smallest among these K elements,
    #    which is exactly the Kth largest element.

    # In short:
    # Keep removing the smallest elements until only K elements remain.
    # The top of the heap is the answer.
    #  
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
