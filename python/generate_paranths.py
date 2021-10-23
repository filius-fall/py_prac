# p = ["(",")"]
# p_list = []

# def possible(n):
#     if n == 1:
#         p_list.append(p[0] + p[1])
#         return p_list
    
#     else:
#         for i in 

# k = possible(1)

# print(k)

# class Solution(object):
#     def generateParenthesis(self, n):
#         def generate(A = []):
#             if len(A) == 2*n:
#                 if valid(A):
#                     ans.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()

#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(': bal += 1
#                 else: bal -= 1
#                 if bal < 0: return False
#             return bal == 0

#         ans = []
#         generate()
#         return ans



def generateParenthesis(n: int):
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            print(S)
            backtrack(S, left+1, right)
            print("After Back Left")
            S.pop()
            print(S)
        if right < left:
            S.append(")")
            print(S)
            backtrack(S, left, right+1)
            print("After Back Right")
            S.pop()
            print(S)
    print("Going to main")
    backtrack()
    return ans


k = generateParenthesis(2)
print(k)