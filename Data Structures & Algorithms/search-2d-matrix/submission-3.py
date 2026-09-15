class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1]<target:
                continue     
            else :
                for k in matrix[i]:
                    if k != target:
                        continue
                    else:
                        return True
                return False
             
        return False
            