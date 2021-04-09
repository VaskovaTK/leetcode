from collections import deque
from pip._vendor.msgpack.fallback import xrange
class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:

        # with the computation of totals we can
        # determine if it's possible to finish the circuit.
        total_gas = 0
        total_cost = 0

        # with the use of a gas_tank we can determine
        # the start index of the circuit by observing
        # when the tank gets emptied and reset to zero
        gas_tank = 0
        start = 0

        for i in range(len(gas)):
            if gas_tank == 0:
                start = i
            gas_tank = max(0, gas_tank + (gas[i] - cost[i]))
            total_gas += gas[i]
            total_cost += cost[i]
        return start if total_gas >= total_cost else -1
    # def canCompleteCircuit(self, gas: list, cost: list) -> int:
    #     if len(gas) == 1:
    #         if gas[0] >= cost[0]:
    #             return 0
    #         else:
    #             return -1
    #     countRemGas = 0
    #     startQueue = deque()
    #     remGas =[0]*len(gas)
    #     for i in xrange (len(gas)):
    #         remGas[i] = gas[i]-cost[i]
    #         countRemGas+=remGas[i]
    #         if remGas[i]>0:
    #             if i+1<=len(remGas)-1:
    #                 if remGas[i]-remGas[i+1]>=0:
    #                     startQueue.append(i)
    #             else:
    #                 if remGas[i]-remGas[0]>=0:
    #                     startQueue.append(i)
    #     if countRemGas<0:
    #         return -1
    #     while len(startQueue) > 0:
    #         lastStation = len(gas)
    #         countStation = 0
    #         gasNow = 0
    #         index = startQueue.popleft()
    #         startIndex = index
    #         while countStation<lastStation:
    #             countStation+=1
    #             gasNow+= remGas[index]
    #             if gasNow <0:
    #                 break
    #             if index+1<=len(gas)-1:
    #                 index+=1
    #             else:
    #                 index=0
    #             if countStation==lastStation:
    #                 if gasNow>=0:
    #                     return startIndex

            # else:
            #     return startIndex
        # return -1

        # startGasStation = deque()
        # for i in range (len(gas)):
        #     if gas[i] > cost[i]:
        #         startGasStation.append(i)
        # while len(startGasStation)>0:
        #     lastStation = len(gas)
        #     countStation = 0
        #     gasNow = 0
        #     index = startGasStation.popleft()
        #     startIndex = index
        #     while countStation<lastStation:
        #         countStation+=1
        #         gasNow+= gas[index]-cost[index]
        #         if gasNow <0:
        #             break
        #         if index+1<=len(gas)-1:
        #             index+=1
        #         else:
        #             index=0
        #     else:
        #         return startIndex
        # return -1










def test(sol, inputTestGas,inputTestCost, expect):
    res = sol.canCompleteCircuit(inputTestGas, inputTestCost)
    print('output {}, expected {}, result {}'.format(res, expect, res == expect))

sol = Solution()
test(sol, [1,2,3,4,5], [3,4,5,1,2],3)
test(sol, [2,3,4],[3,4,3],-1)
test(sol, [4,5,3,1,4],[5,4,3,4,2],-1)
test(sol, [5,1,2,3,4],[4,4,1,5,1],4)
test(sol,[5],[4],0)