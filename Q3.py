class Solution:
    def findMedianSortedArrays(self, x, y):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x, y = (x, y) if len(x) <= len(y) else (y, x)
        total_len_even = (len(x) + len(y)) % 2 == 0
        left, right = 0, len(x)
        while left <= right:
            partition_x = (left + right) // 2

            half_el_count = (len(x) + len(y) + 1) // 2
            partition_y = half_el_count - partition_x 

            max_left_x = float('-inf') if partition_x == 0 else x[partition_x - 1]
            min_right_x = float('inf') if partition_x == len(x) else x[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else y[partition_y - 1]
            min_right_y = float('inf') if partition_y == len(y) else y[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0 if total_len_even else float(max(max_left_x, max_left_y))
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1