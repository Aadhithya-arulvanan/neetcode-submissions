class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store ={}

        for num in nums:
            store[num] = store.get(num,0)+1
            
            
        freqlist = []
        for _ in range(len(nums)+1):
            freqlist.append([])
        for num , freq in store.items():
            freqlist[freq].append(num)
        res=[]
        for x in range(len(nums),0,-1):
            for num in freqlist[x]:
                res.append(num)
            if len(res)==k:
                return res
                       
        