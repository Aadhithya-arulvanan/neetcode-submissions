class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [0]*len(position)
        for i in range(len(position)):
            pairs[i] = (position[i],speed[i])
        pairs.sort(reverse = True)
        for i in range(len(pairs)):
            time = (target-pairs[i][0])/pairs[i][1]
            if not stack or stack[-1]<time:
                stack.append(time)
            else :
                continue
        return len(stack)
