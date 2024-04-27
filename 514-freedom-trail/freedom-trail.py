class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Create a dict where the key is the character and value is the list of position
        # Resursively call a function which will find the find the minimum steps
        # Use visited to mark visted combination with current string index and position of 
        # the ring

        visited = {}
        lock = defaultdict(list)
        for i in range(len(ring)):
            lock[ring[i]].append(i)

        return self.dfs(0, 0, ring, key, lock, visited)


    def dfs(self, key_idx, lock_pos, ring, key, lock, visited):
        if (key_idx, lock_pos) in visited:
            return visited[(key_idx, lock_pos)]
        
        if key_idx >= len(key):
            return 0

        min_steps = 10001
        for i in lock[key[key_idx]]:
            if lock_pos > i:
                steps = min(lock_pos - i, len(ring) - lock_pos + i)
            else:
                steps = min(i - lock_pos, len(ring) - i + lock_pos)
            min_steps = min(min_steps, steps + self.dfs(key_idx+1, i, ring, key, lock, visited))
        print(key[key_idx], min_steps)
        visited[(key_idx, lock_pos)] = min_steps + 1
        return min_steps + 1