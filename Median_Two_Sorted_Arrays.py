class Solution:
    def findMedianSortedArrays(self, num1, num2):
        merged_array = num1 + num2

        sorted_array = sorted(merged_array)

        total_length = len(sorted_array)

        if total_length % 2 == 0:
            median_position_1 = int(total_length / 2)    
            median_position_2 = int(median_position_1 + 1)   

            median = ( sorted_array[median_position_1 - 1] + sorted_array[median_position_2 - 1] ) / 2

            return median
    
        else:
            median_position = int(( total_length + 1 ) / 2)

            median = sorted_array[median_position - 1]

            return median
        
