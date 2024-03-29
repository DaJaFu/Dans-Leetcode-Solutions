from typing import List

def twoSum(nums:List[int], target:int) -> List[int]:
    for i in nums:
        if i + nums[nums.index(i)+1] == target:
            return [nums.index(i),nums.index(i)+1]
    return None

print(twoSum([2,7,11,15],9))
print("-"*20)
print(twoSum([3,2,4],6))
print("-"*20)
print(twoSum([3,3],6))