nums = [2, 7, 11, 15]
target = 9

class solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = nums.index(i) + 1
            rest_nums = nums[next_index: ]
            if j in rest_nums:
                return [nums.index(i), next_index+rest_nums.index(j)]

    
        for i in range(len(nums)):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
            if i != j:
                return [x, y]
    
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in nums:
                dict[nums[i]] = i
            else:
                return[dict[target-nums[i]], i]
                
                
        dict = {}
	     for i, n in enumerate(nums): 
             if n in dict: return [d[n], i]
	          d[target-n] = i

        for i, a in enumerate(nums, start=0):
            for j, b in enumerate(nums[i+1], start=0):
                if a+b == target:
                    return [i, j+i+1]
    
