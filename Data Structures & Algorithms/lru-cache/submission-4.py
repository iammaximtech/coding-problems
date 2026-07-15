class ListNode:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.key =key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache= {}
        self.capacity = capacity
        self.left, self.right = ListNode(-1,-1), ListNode(-1,-1)
        self.left.right, self.right.left = self.right, self.left

    def insert(self, node: ListNode):
        left, right = self.right.left, self.right
        node.left, node.right = left, right
        right.left = node
        left.right = node
        
    
    def delete(self, node:ListNode):
        left, right = node.left, node.right
        left.right, right.left = right, left
        node.left = node.right = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
        else:
            self.cache[key] = ListNode(key, value)
            self.insert(self.cache[key])
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            node = self.left.right
            self.cache.pop(node.key)
            self.delete(node)
            
            
        
        
