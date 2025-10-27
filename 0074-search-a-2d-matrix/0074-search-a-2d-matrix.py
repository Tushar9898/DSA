class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        # :type target: int
        # :rtype: bool
        """
        
        
        if not matrix or not matrix[0]:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False

        