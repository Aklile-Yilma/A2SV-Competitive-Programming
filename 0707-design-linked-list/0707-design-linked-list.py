class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        if self.head is None:
            return -1
        
        currNode = self.head
        idx = 0
        while currNode:
            if idx == index:
                return currNode.val
            idx += 1
            currNode = currNode.next
        return

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return 
        
    def addAtTail(self, val: int) -> None:      
        if self.size == 0:
            self.addAtHead(val)
            return
        
        newNode = Node(val)
        currentNode = self.head
        
        while currentNode.next:
            currentNode = currentNode.next
            
        currentNode.next = newNode   
        self.size += 1
        return
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        newNode = Node(val)
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        prevNode = None
        currNode = self.head
        while currNode.next and index > 0:
            prevNode = currNode
            currNode = currNode.next
            index-= 1
            
        prevNode.next = newNode
        newNode.next = currNode
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if self.head is None:
            return
        
        if index == 0: # if head to delete
            newHead = self.head.next
            self.head = newHead
            self.size -= 1 
            return 
        
        prevNode = None
        currNode = self.head
        while currNode.next and index > 0:
            prevNode = currNode
            currNode = currNode.next
            index-= 1
            
        prevNode.next = currNode.next
        self.size -= 1        
        return
    
    def printNodes(self) -> None:
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" ".join(nodes))

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)