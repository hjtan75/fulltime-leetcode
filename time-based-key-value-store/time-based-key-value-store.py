class TimeMap:
    hashMap = {}


    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vtPair = self.hashMap.get(key, [])
        vtPair.append((value, timestamp))
        self.hashMap[key] = vtPair

    def get(self, key: str, timestamp: int) -> str:
        vtPair = self.hashMap.get(key, [])
        if len(vtPair) == 0:
            return ""

        l, r = 0, len(vtPair) - 1
        while l <= r:
            m = int((l+r)/2)
            if timestamp == vtPair[m][1]:
                return vtPair[m][0]

            if timestamp > vtPair[m][1]:
                l = m + 1
            else:
                r = m - 1

        # print(timestamp, l, r, m)
        if vtPair[m][1] < timestamp:
            return vtPair[m][0]
        elif m <= 0:
            return ""
        else:
            return vtPair[m-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)