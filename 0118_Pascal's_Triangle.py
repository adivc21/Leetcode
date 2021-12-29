class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        result = list()
        
        for i in range(numRows):
            result.append(list())

            if (i == 0):
                result[0].append(1)
                
            else:
                for j in range(i+1):
                    if (j==0 or j==i):
                        result[i].append(1)
                    else:
                        result[i].append(result[i-1][j-1] + result[i-1][j])

        return result