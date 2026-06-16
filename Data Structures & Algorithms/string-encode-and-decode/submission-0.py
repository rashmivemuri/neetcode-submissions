class Solution:

    def encode(self, strs: List[str]) -> str:
        global s
        s=''
        for i in strs:
            s=s+(i+'`')
        return s

    def decode(self, s: str) -> List[str]:
     
            
        l= s.split('`')
        return l[:-1]
