class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for ind ,i in enumerate(nums) :
            need = target - i;

            if need in store :
                return [store[need],ind]
            store[i] = ind
         