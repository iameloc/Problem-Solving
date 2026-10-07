class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if nums == None:
            return []

        list = []
        i = 0
        j = len(nums) - 1
        nums2 = sorted(nums)

        while i<j:
            if nums2[i]+nums2[j] > target:
                j -= 1
            elif nums2[i]+nums2[j] < target:
                i += 1
            else:
                n1 = nums2[i]
                n2 = nums2[j]
                break
                
        for i in range(len(nums2)):
            if nums[i] == n1:
                list.append(i)
            elif nums[i] == n2:
                list.append(i)
            if len(list) == 2: break

        return list


        