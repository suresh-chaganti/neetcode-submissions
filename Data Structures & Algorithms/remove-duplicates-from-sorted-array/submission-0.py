class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        write_index = 0
        for i in nums:
            if i not in seen:
                seen.add(i)
                nums[write_index]=i
                write_index += 1
        #print(nums[:write_index])
        return write_index


