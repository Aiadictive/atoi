import re
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-]*[1-9]+)\D*', str)
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except Exception:
            return 0
def main():
    sol=Solution()
    print(sol.atoi("      -5642"))
if __name__=="__main__":
    main()
