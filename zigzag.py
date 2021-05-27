class Solution:
    def convert(self, s: str, r: int) -> str:
        n = len(s)
        if r == 1:
            return s
        elif r == 2:
            return s[0:n:2] + s[1:n:2]
        else:
            matrix = [[-1] * n for _ in range(r)]
            row = 0     # current row number
            col = 0     # current column number
            ind = 0     # current index in the input string
            dire = 0    # direction -> 0 means down, 1 means up
            while ind < n:
                matrix[row][col] = s[ind]
                if dire == 0:
                    if row == r - 1:
                        row -= 1
                        col += 1
                        dire = 1
                    else:
                        row += 1
                else:
                    if row == 0:
                        dire = 0
                        row += 1
                    else:
                        row -= 1
                        col += 1
                ind += 1
            res = ""
            for u in matrix:
                for t in u:
                    if t != -1:
                        res += t
            return res