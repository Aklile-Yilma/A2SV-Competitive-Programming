class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        directory = []
        
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                if directory:
                    directory.pop()
                continue
            else:
                directory.append(log)
                
        return len(directory)
            