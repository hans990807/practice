class MyHashSet:

    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        if (key not in self.hashset) or (key in self.hashset and self.hashset[key] == 0):
            self.hashset[key] = True


    def remove(self, key: int) -> None:
        if key in self.hashset and self.hashset[key] == 1:
            self.hashset[key] = False

    def contains(self, key: int) -> bool:
        if key not in self.hashset:
            return False
        else:
            return self.hashset[key]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)