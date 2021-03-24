class Solution:
    def camelMatch(self, queries: list, pattern: str) -> list:
        returnArray = [True]*len(queries)
        for qIndex in range (0, len(queries)):
            flag = False
            for qqIndex in range(0, len(queries[qIndex])):
                if flag ==True:
                    break
                for pIndex in range (0, len(pattern)):
                    if queries[qIndex][qqIndex].isupper():
                        if pattern[pIndex].isupper():
                            if pattern[pIndex] != queries[qIndex][qqIndex]:
                                returnArray[qIndex] = False
                                break
                            else:
                                continue
                        else:
                            if pattern[pIndex] == queries[qIndex][qqIndex]:
                                continue
            return returnArray




def test(sol, inputQueries, inputPattern, expect):
    res = sol.camelMatch(inputQueries,inputPattern)
    print('output {}, expected {}, result {}'.format(res, expect, res == expect))

sol = Solution()
# test(sol, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB", [True,False,True,True,False])
# test(sol, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa", [True,False,True,False,False])
# test(sol, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT", [False,True,False,False,False])
test(sol, ["CompetitiveProgramming","CounterPick","ControlPanel"], 'CooP', [False,False,True])