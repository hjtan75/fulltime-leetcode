class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dot_cnt = 0
        sem_cnt = 0

        if len(queryIP) > 39:
            return 'Neither'
            
        for c in queryIP:
            if c == '.':
                dot_cnt += 1
            if c == ':':
                sem_cnt += 1

        if dot_cnt == 3 and sem_cnt == 0:
            classes = queryIP.split('.')
            if len(classes) != 4:
                return 'Neither'
            for cla in classes:
                if cla.isnumeric():
                    if len(cla) > 1 and cla[0] == '0':
                        return 'Neither'

                    num = int(cla)
                    if num > 255:
                        return 'Neither'
                else:
                    return 'Neither'
            return 'IPv4'


        if sem_cnt == 7 and dot_cnt == 0:
            classes = queryIP.split(':')
            if len(classes) != 8:
                return 'Neither'
            for cla in classes:
                if len(cla) < 1 or len(cla) > 4:
                    return 'Neither'
                for c in cla:
                    if c not in '0123456789' and c.lower() not in 'abcdef':
                        return 'Neither'
                
            return 'IPv6'

        return 'Neither'
