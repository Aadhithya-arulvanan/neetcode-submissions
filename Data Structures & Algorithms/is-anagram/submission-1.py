class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store ={}
        for chr in s:
            store[chr] = store.get(chr,0)+1;
        for chr in t:
            store[chr] = store.get(chr,0)-1;
        for chr in store.values():
            if chr != 0 :
                return False
        return True