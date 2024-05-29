class Solution:
    def numSteps(self, s: str) -> int:
        # The straight forward method is to convert it into integer
        # Then process it to reduce in that way
        
        # The other method would be process it directly in binary
        # If number if even, lsb would be 0, just have to pop it
        # if it is 1, add 1 to the next available zero, the frequency of 1 coontingous to the number of 
        # step. beause it would be zero and we can divide it anyway

        arr = [c for c in s]
        step = 0
        
        while len(arr) > 1:
            print(arr)
            while len(arr) > 1 and arr[-1] == '0':
                step += 1
                arr.pop()

            if len(arr) == 1:
                break

            while len(arr) >= 1 and arr[-1] == '1':
                print('enter')
                step += 1
                arr.pop()
            
            if len(arr) == 0:
                arr.append('1')
            else:
                arr[-1] = '1'
            step += 1

        return step