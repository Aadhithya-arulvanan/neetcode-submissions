class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store ={}
        if len(s) != len(t):
            return False
        for i in s :
            store[i] = store.get(i,0)+1
        for i in t :
            store[i] = store.get(i,0)-1
        x= tuple(store.values())
        for i in x:
            if i != 0 :
                return False 
        return True
        