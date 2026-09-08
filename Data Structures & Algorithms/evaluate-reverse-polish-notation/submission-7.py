class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens :
            if i not in "+/*-":
                st.append(i)
            else :
                b = int(st.pop())
                a = int(st.pop())
                if i == "+":
                    st.append(a+b)
                if i == "-":
                    st.append(a-b)
                if i == "*":
                    st.append(a*b)
                if i == "/":
                    st.append(int(a/b))
        return int(st[0])
     
        