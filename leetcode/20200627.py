# 缺失的第一个正数
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 示例
# 1:
# 输入: [1, 2, 0]
# 输出: 3
# 示例
# 2:
# 输入: [3, 4, -1, 1]
# 输出: 2
# 示例
# 3:
# 输入: [7, 8, 9, 11, 12]
# 输出: 1
# 提示：
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间
#
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if i == len(nums):
                result = nums[-1]+1
            elif nums[i]<0 or nums[i+1]==nums[i]+1:
                continue
            else:
                result = nums[i] + 1

        return result


if __name__ == '__main__':
    nums = [1,2,0]
    a = Solution().firstMissingPositive(nums)
    print(a)