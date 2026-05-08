class Store:
    def __init__(self):
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        self.values = list()
        self.map = dict()
        
    def insert(self, value: int) -> None:
        # Time Complexity: O(1) average for dict lookup and list append
        # Space Complexity: O(1)
        if value in self.map:
            return
        
        self.values.append(value)
        self.map[value] = len(self.values) - 1
        
    def remove(self, value: int) -> None:
        # Time Complexity: O(1) average for dict operations
        # Space Complexity: O(1)
        if value not in self.map:
            return
        
        index = self.map[value]
        last_value = self.values[-1]
        
        self.values[index] = last_value
        self.map[last_value] = index
        
        self.values.pop()
        del self.map[value]
        
    def get_random(self) -> int:
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        import random
        return random.choice(self.values)
        
if __name__ == "__main__":
    store = Store()
    store.insert(1)
    store.insert(2)
    store.insert(3)
    store.remove(2)
    print(store.values)
    print(store.map)
    
        