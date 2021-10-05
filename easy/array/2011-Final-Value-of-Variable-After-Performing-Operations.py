class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0
        
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                counter -= 1
            else:
                counter += 1 
                
        return counter 
        
