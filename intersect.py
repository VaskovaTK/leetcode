class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        firstDict = {}
        secondDict = {}
        retList =list()
        for i in range(0,len(nums1)):
            if nums1[i] not in firstDict.keys():
                firstDict[nums1[i]] = 1
            else:
                firstDict[nums1[i]]+=1
        for j in range(0,len(nums2)):
            if nums2[j] not in secondDict.keys():
                secondDict[nums2[j]] = 1
            else:
                secondDict[nums2[j]]+=1
        if len(firstDict)<len(secondDict):
            for k in firstDict.keys():
                if k in secondDict.keys():
                    if firstDict[k]<secondDict[k]:
                        count = firstDict[k]
                        while count > 0:
                            retList.append(k)
                            count -= 1
                    else:
                        count = secondDict[k]
                        while count > 0:
                            retList.append(k)
                            count -= 1
        else:
            for k in secondDict.keys():
                if k in firstDict.keys():
                    if firstDict[k]<secondDict[k]:
                        count = firstDict[k]
                        while count>0:
                            retList.append(k)
                            count-=1
                    else:
                        count = secondDict[k]
                        while count>0:
                            retList.append(k)
                            count-=1
        # print(retList)
        return retList


sol = Solution()
sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2])