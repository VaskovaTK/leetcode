class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        if len(deck) == 1:
            return deck
        for i in range(0, len(deck)):
            if i < len(deck) - 1:
                while True:
                    if deck[i + 1] < deck[i]:
                        deck[i], deck[i + 1] = deck[i + 1], deck[i]
                        if i - 1 >= 0:
                            i = i - 1
                    else:
                        break
        retDeck = [0]*len(deck)
        dIndex = -2
        rememberedIndex = 0
        for index in range (0, len(deck)):
            dIndex+=2
            if dIndex<len(retDeck):
                retDeck[dIndex] = deck[index]
            else:
                rememberedIndex = index
                break
        index = rememberedIndex
        step =0
        while index != len(deck)-1:
            if len(deck) % 2 != 0 :
                step = 0
            else:
                step = 1
            indexR = 1
            while indexR != len(retDeck)-1:
                if retDeck[indexR] ==0:
                    step+=1
                    if step ==2:
                        retDeck[indexR] = deck[index]
                        step = 0
                        index+=1
                        if index<len(deck)-1:
                            continue
                        else:
                            break
                    else:
                        indexR+=1
                        continue
                else:
                    indexR+=1
        for i in range (1, len(retDeck)):
            if retDeck[i] == 0:
                retDeck[i] = deck[index]
                break
        return retDeck

        #     if len(missed) ==1:
        #         retDeck[missed[0]] = deck[index]
        #         break
        #     while True:
        #         miss+=2
        #         if miss <= len(missed)-1:
        #             if missed[miss] != 0:
        #                 retDeck[missed[miss]] = deck[index]
        #                 missed[miss] = 0
        #                 break
        #             else:
        #                 miss = -2
        #                 continue
        #         else:
        #             if len(deck) %2==0:
        #                 miss = 1
        #             else:
        #                 if len(missed) %2 !=0:
        #                     miss = 1
        #                 else:
        #                     miss = 0
        #                     continue
        #             if missed[miss] != 0:
        #                 retDeck[missed[miss]] = deck[index]
        #                 missed[miss] = 0
        #                 break
        #             else:
        #                 miss = -2
        #                 continue
        # return retDeck

def test(sol, inputTest, expect):
    res = sol.deckRevealedIncreasing(inputTest)
    print('output {}, expected {}, result {}'.format(res, expect, res == expect))

sol = Solution()
# test(sol, [1,2,3,4,5,6,7,8], [1,5,2,7,3,6,4,8])
test(sol, [17,13,11,2,3,5,7], [2,13,3,11,5,17,7])
# test(sol, [1,2,3], [1,3,2])
# test(sol,[1,2,3,4,5,6,7,8,9], [1,9,2,6,3,8,4,7,5])
# test(sol, [1,2,3,4,5], [1,5,2,4,3])