#Solution 1
'''
hint:
1.num[i]+num[j]=target
2.i not equal to j
3.range i+1, len(nums)
'''
#O(n^2)
# class Solution(object):
#     def twoSum(self,nums,target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]


#Solution2
#hash table
'''
hint:
num[j] = target-num[i]
hash table
'''
# class Solution(object):
#     def twoSum(self, nums, target):
#         d = {}
#         for i in range(len(nums)):
#             num1 = nums[i]
#             num2 = target - num1
#             if num2 in d:
#                 return [d[num2], i]
#             d[num1] = i
        

#Solution3
#two pointer
'''
i=0
j=len(nums)-1
'''

class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        
        while (nums[i] + nums[j] != target):
            if (nums[i] + nums[j] > target):
                j = j - 1
            else:
                i = i + 1
                
        return [i, j]

nums=[3,2,4]
target=6
obj=Solution()
print(obj.twoSum(nums,target))


