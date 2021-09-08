from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        for i in range (len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                queue.append(s[i])
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(queue) == 0:
                    return False
                else:
                    fromQue = queue.pop()
                    if fromQue == "(":
                        waiting = ")"
                        if s[i] == waiting:
                            continue
                        else:
                            return False
                    elif fromQue == "{":
                        waiting = "}"
                        if s[i] == waiting:
                            continue
                        else:
                            return False
                    elif fromQue == "[":
                        waiting = "]"
                        if s[i] == waiting:
                            continue
                        else:
                            return False
        if len(queue) == 0:
            return True

sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("()[}{]{}"))