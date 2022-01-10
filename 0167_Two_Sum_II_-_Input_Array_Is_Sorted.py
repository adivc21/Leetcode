class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # # -----x-----x-----
        # # Solution 1 - Two Pointers
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        # left = 0
        # right = len(numbers) - 1
        
        # while left < right:
        #     if (numbers[left]+numbers[right] < target):
        #         left += 1
        #     elif (numbers[left]+numbers[right] > target):
        #         right -= 1
        #     else:
        #         break
                
        # return [left+1, right+1]
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - Two Pointers with Binary Search
        # # Time complexity = O(log(n))
        # # Space complexity = O(1)
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            mid = left + ((right-left)//2)
            if (numbers[left]+numbers[right] == target):
                break
            elif (numbers[left]+numbers[right] < target):
                left = mid if (numbers[mid]+numbers[right] <= target) else (left+1)
            else:
                right = mid if (numbers[left]+numbers[mid] >= target) else (right-1)
                
        return [left+1, right+1]
        # # -----x-----x-----      
