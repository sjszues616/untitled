# 给定一个含有 n
# 个正整数的数组和一个正整数s ，找出该数组中满足其和 ≥ s
# 的长度最小的连续子数组，并返回其长度。
# 如果不存在符合条件的连续子数组，返回0。

# 示例：
#
# 输入：s = 7, nums = [2, 3, 1, 2, 4, 3]
# 输出：2
# 解释：子数组[4, 3]
# 是该条件下的长度最小的连续子数组。


from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mincount = float('inf')
        left = 0
        sumcount = 0
        count = 0
        if not nums:
            return 0
        for right in range(len(nums)):
            sumcount += nums[right]
            if sumcount < s:
                count = right - left + 1
            while sumcount > s or sumcount == s:
                count = right - left + 1
                sumcount -= nums[left]
                left += 1
                mincount = min(count, mincount)
        if sum(nums) < s:
            return 0
        else:
            return mincount


if __name__ == '__main__':
    nums = [5,1,3,5,10,7,4,9,2,8]
    target = 15
    a = Solution().minSubArrayLen(target, nums)
    print(a)
