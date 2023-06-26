from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            # Ensure nums1 is the smaller array for convenience
            nums1, nums2, m, n = nums2, nums1, n, m
        
        left, right = 0, m
        half_length = (m + n + 1) // 2
        
        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = half_length - partition_nums1
            
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # Found the correct partition, calculate the median
                if (m + n) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            
            elif max_left_nums1 > min_right_nums2:
                # Go left in nums1
                right = partition_nums1 - 1
            else:
                # Go right in nums1
                left = partition_nums1 + 1
        
        # If the program reaches here, the input arrays are not sorted or contain invalid values
        raise ValueError("Invalid input arrays.")

# Example usage
s = Solution()
nums1 = [1, 3]
nums2 = [2]
median = s.findMedianSortedArrays(nums1, nums2)
print("Median:", median)
