class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = []
        for item in nums:
            if item not in duplicates:
                duplicates.append(item)
            else:
                return True
        return False

   