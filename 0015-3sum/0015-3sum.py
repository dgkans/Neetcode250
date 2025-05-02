class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n =len(nums)
        answer = []
        for i in range(n):
            if nums[i] > 0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue
            low,high = i+1,n-1 
            while low < high:
                sum = nums[i]+nums[low]+nums[high]
                if sum == 0:
                    answer.append([nums[i],nums[low],nums[high]])
                    low,high = low+1,high-1
                    while low < high and nums[low] == nums[low-1]:
                        low+=1
                    while low < high and nums[high] == nums[high+1]:
                        high-=1
                elif sum < 0:
                    low+=1
                else:
                    high-=1
        return answer

                