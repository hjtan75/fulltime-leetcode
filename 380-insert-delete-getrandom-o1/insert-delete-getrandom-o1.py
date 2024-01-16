class RandomizedSet:
    # Used dictionary to storoe {value, location in the array}
    # Used a list to store value of the set
    # To remove and element, we know the index of the element
    # but to pop at that index, it will take O(n) because of the shift action
    # We could swap the element with the last element in the array, so that
    def __init__(self):
        self.this_set = set()

    def insert(self, val: int) -> bool:
        if val in self.this_set:
            return False
        else:
            self.this_set.add(val)
            return True


    def remove(self, val: int) -> bool:
        if val not in self.this_set:
            return False
        else:
            self.this_set.remove(val)
            return True
        

    def getRandom(self) -> int:
        arr = list(self.this_set)
        rand_int = random.randint(0, len(arr)-1)
        return arr[rand_int]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()