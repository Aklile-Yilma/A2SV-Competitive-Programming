class Solution:
    def sortSentence(self, s: str) -> str:
        words= s.split()
        sentence=[None]*len(words)
        
        for i,value in enumerate(words):
            sentence[int(value[-1])-1]=value[:-1]
    
        return " ".join(sentence) 
    
    
        