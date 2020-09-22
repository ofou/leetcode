from functools import reduce
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        for i, n in enumerate(nums, start=1):
            suma = functools.reduce(lambda a,b: a+b, nums[0:i], 0)
            temp.append(suma)
        return temp