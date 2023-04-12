class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.deads = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def preorder(name):
            
            if self.graph[name] == []:
                return [name]
            
            order = [name]
            for child in self.graph[name]:
                order += preorder(child)
                
            return order
        
        order = preorder(self.king)
        result = []
        
        for node in order:
            if node not in self.deads:
                result.append(node)
                
        return result
        
                
            
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()