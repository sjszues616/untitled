from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        alist = []
        for i in range(len(nums)):
            a = nums[i]
            for j in range(len(nums[i+1:])):
                b = nums[i+1:][j]
                for z in range(len(nums[i+1:][j+1:])):
                    c = nums[i+1:][j+1:][z]
                    alist.append(a+b+c-target)

        for i in alist:
            if abs(i) == min([abs(i) for i in alist]):
                return i+target

if __name__ == '__main__':
    nums= [-1,2,2,-4]
    target=1
    a = Solution().threeSumClosest(nums,target)
    print(a)