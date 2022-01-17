class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # # -----x-----x-----
        # # Solution 1 - Merge, then sort
        # # m=len(nums1), n=len(nums2)
        # # Time complexity = O((m+n)*log(m+n))
        # # Space complexity = O(1)
        
        # Replace zeroes in nums1 with elements of nums2
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
            
        # Sort nums1
        # nums1.sort()
        # # -----x-----x-----

        # # -----x-----x-----
        # # Solution 2 - Start populating from end of nums1
        # # m=len(nums1), n=len(nums2)
        # # Time complexity = O(m+n)
        # # Space complexity = O(1)
        
        if not m:
            nums1[0:n] = nums2
            return
        if not n:
            return
        
        while m+n-1:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
                if not m: break
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                if not n: break
                    
        if m:
            nums1[0:m] = nums1[0:m]
        
        if n:
            nums1[0:n] = nums2[0:n]
        # # -----x-----x-----
