class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSumList = []
        runningSum = 0
        for num in nums:
            runningSum += num
            runningSumList.append(runningSum)
        return runningSumList