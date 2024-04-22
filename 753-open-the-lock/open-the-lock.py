class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Use a recursive bfs to explore the shortest path from 0000 to target
        # Mark as visited if the element is visited before
        # If a deadend is encountered, return

        # Bfs: use an array to mark the current depth of element
        # Pop element from the front then explore that element, 
        # Append all child element of the explored element to the back of the list
        # Two array is needed to that we can mark the steps
        self.target = target
        self.step = -1
        self.bfs_arr_0, self.bfs_arr_1 = [], ['0000']
        visited = [False] * 10000

        def bfs():
            while len(self.bfs_arr_1) > 0:
                swap = self.bfs_arr_0
                self.bfs_arr_0 = self.bfs_arr_1
                self.bfs_arr_1 = swap
                self.step += 1
                while len(self.bfs_arr_0) > 0:
                    s = self.bfs_arr_0.pop(0)
                    num = int(s)
            
                    if s in deadends or visited[num]:
                        continue
                    if s == target:
                        return self.step

                    visited[num] = True
                    d4 = int(s[0])
                    d3 = int(s[1])
                    d2 = int(s[2])
                    d1 = int(s[3])

                    # print(d1, d2, d3, d4)

                    if d1 == 0:
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, d2, 9])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, d2, 1])))
                        # print(''.join(map(str, [d4, d3, d2, 9])))
                        # print(''.join(map(str, [d4, d3, d2, 1])))
                    else:
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, d2, (d1+1) % 10])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, d2, d1-1])))
                    #     print(''.join(map(str, [d4, d3, d2, (d1+1) % 10])))
                    #     print(''.join(map(str, [d4, d3, d2, d1-1])))
                    # print(d1, d2, d3, d4)
                    if d2 == 0:
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, 9, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, 1, d1])))
                        # print(''.join(map(str, [d4, d3, 9, d1])))
                        # print(''.join(map(str, [d4, d3, 1, d1])))
                    else:
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, (d2+1) % 10, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3, d2-1, d1])))
                    #     print(''.join(map(str, [d4, d3, (d2+1) % 10, d1])))
                    #     print(''.join(map(str, [d4, d3, d2-1, d1])))

                    # print(d1, d2, d3, d4)
                    if d3 == 0:
                        self.bfs_arr_1.append(''.join(map(str, [d4, 9, d2, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, 1, d2, d1])))
                    else:
                        self.bfs_arr_1.append(''.join(map(str, [d4, (d3+1) % 10, d2, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [d4, d3-1, d2, d1])))

                    if d4 == 0:
                        self.bfs_arr_1.append(''.join(map(str, [9, d3, d2, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [1, d3, d2, d1])))
                    else:
                        self.bfs_arr_1.append(''.join(map(str, [(d4+1) % 10, d3, d2, d1])))
                        self.bfs_arr_1.append(''.join(map(str, [d4-1, d3, d2, d1])))
            return -1
        return bfs()
        

            



            