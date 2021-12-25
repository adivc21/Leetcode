class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary for storing an element as key and its index as value
        checked = dict()
        
        for index, value in enumerate(nums):
            complement = target - value
            
            # Add the element to the dict, if its complement is
            # not in the dict, as key and its index as value
            if complement not in checked:
                checked[value] = index
            else:
                # Return the index of the complement
                # and the index of the current element
                return [checked[complement], index]