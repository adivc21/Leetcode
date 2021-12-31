class Solution:
    def trim(self, test:str) -> str:
        if (test[-2]=='(' and test[-1]==')'
           or test[-2]=='[' and test[-1]==']'
           or test[-2]=='{' and test[-1]=='}'):
            if len(test[:-2])>1:
                return self.trim(test[:-2])
            return test[:-2]
        else:
            return test

    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        test = list()
        
        for char in s:
            test.append(char)
            
            if (len(test)>1):
                test = self.trim(test)
                
        if test:
            return False
        
        return True
        