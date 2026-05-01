class Store:
    def __init__(self):
        self.values = list()
        self.map = dict()
        
    def insert(self, value: int) -> None:
        if value in self.map:
            return
        
        self.values.append(value)
        self.map[value] = len(self.values) - 1
        
    def remove(self, value: int) -> None:
        if value not in self.map:
            return
        
        index = self.map[value]
        last_value = self.values[-1]
        
        self.values[index] = last_value
        self.map[last_value] = index
        
        self.values.pop()
        del self.map[value]
        
    def get_random(self) -> int:
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
    
        