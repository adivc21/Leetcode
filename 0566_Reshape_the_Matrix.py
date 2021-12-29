class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        temp_r = temp_c = 0
        
        if (len(mat)*len(mat[0]) == r*c):
            result = list()
            for i in range(r):
                result.append(list())
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    result[temp_r].append(mat[i][j])
                    temp_c += 1
                    if (temp_c == c):
                        temp_c = 0
                        temp_r += 1
                    if (temp_r == r):
                        break
            return result
        else:
            return mat