class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.num_list = [] # to avoid creating the list in getRandom method as it will lead to O(n)

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            self.num_list.append(val)
            return True    

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.num_list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        # return random.choice(list(self.set))
        return random.choice(self.num_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
