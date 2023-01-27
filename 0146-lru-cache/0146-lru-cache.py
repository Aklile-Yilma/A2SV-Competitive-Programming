class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key  in self.cache:
            self.put(key, self.cache[key]) # Call to put to handle LRU placement
        return self.cache.get(key, -1) # Return a default of '-1' if key does not exist
        

    def put(self, key: int, value: int) -> None:
        self.cache.pop(key, None)   # Remove key-value if it exists
        self.cache[key] = value # Insert key-value at top of key stack
        
        if len(self.cache) > self.capacity:
            del self.cache[next(iter(self.cache))]   # Delete LRU (bottom of key stack)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.capacity = capacity
        

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.put(key, self.cache[key])                 # Call to put to handle LRU placement
#         return self.cache.get(key, -1)                     # Return a default of '-1' if key does not exist
        

#     def put(self, key: int, value: int) -> None:           # Method adds key-value to cache and pops the LRU item
#         self.cache.pop(key, None)                          # Remove key-value if it exists
#         self.cache[key] = value                            # Insert key-value at top of key stack
#         if len(self.cache) > self.capacity:
#             del self.cache[next(iter(self.cache))]         # Delete LRU (bottom of key stack)