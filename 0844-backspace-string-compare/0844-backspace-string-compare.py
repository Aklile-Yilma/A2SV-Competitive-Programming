class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_stack = []
        t_stack = []
        
        for char_s in s:
            
            if char_s == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(char_s)
                
        for char_t in t:
                
            if char_t == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(char_t)
                
        print(s_stack, t_stack)
                
        s = ''.join(s_stack)
        t = ''.join(t_stack)
        
        return s == t