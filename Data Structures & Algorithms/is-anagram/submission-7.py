class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = {}
        if len(s) != len(t):
            return False
        for i in s :
            st[i] = st.get(i,0)+1  
    
        for i in t :
            st[i] = st.get(i,0)-1
        for i in st.values() :
            if i != 0 : 
                return False    
        return True 