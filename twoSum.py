class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        # create a dictionary to store index for a number in the list
        store = {}

        for i, n in enumerate(nums):
            diff = target -n
            if diff in store:
                # since we know one answer defintely exists. 
                return [store[diff], i]
            store[n] = i 
