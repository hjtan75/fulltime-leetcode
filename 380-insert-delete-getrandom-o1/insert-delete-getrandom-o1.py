class RandomizedSet:
    # Used dictionary to storoe {value, location in the array}
    # Used a list to store value of the set
    # To remove and element, we know the index of the element
    # but to pop at that index, it will take O(n) because of the shift action
    # We could swap the element with the last element in the array, so that
    # pop only require O(1)
    # Have to update the dictionary of the new location.
    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.arr.append(val)
            self.dict[val] = len(self.arr) - 1
            return True


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        else:
            idx_to_be_remove = self.dict[val]
            val_to_be_swapped = self.arr[-1]
            self.arr[idx_to_be_remove], self.arr[-1] = self.arr[-1], self.arr[idx_to_be_remove]
            self.arr.pop()
            self.dict[val_to_be_swapped] = idx_to_be_remove
            del self.dict[val]
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()