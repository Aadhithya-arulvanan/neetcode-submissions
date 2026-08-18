class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for word in strs:
            freq = [0]*26
            for letter in word:
                freq[ord(letter)-ord('a')] = freq[ord(letter)-ord('a')]+1
            key = tuple(freq)
            if key not in store :
                store[key]= []
            store[key].append(word)
        return list(store.values())    
