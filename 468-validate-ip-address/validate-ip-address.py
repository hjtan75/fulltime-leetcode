class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            try:
                num = int(s)
                return str(num) == s and num <= 255
            except:
                return False

        def isIPv6(s):
            try:
                return len(s) <= 4 and int(s, 16) >= 0
            except:
                return False

        if queryIP.count('.') == 3 and all(isIPv4(i) for i in queryIP.split('.')):
            return "IPv4"

        if queryIP.count(':') == 7 and all(isIPv6(i) for i in queryIP.split(':')):
            return "IPv6"
        return 'Neither'