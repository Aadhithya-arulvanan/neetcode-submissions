class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = sorted(s)
        n = sorted(t)
        st = {}
        tt = {}
        for i in m :
            st[i] = st.get(i,0)+1
        for i in n :
            tt[i] = tt.get(i,0)+1
        if st == tt :
            return True 
        return False 