class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        la=[]

        aa=[]

        for i in range(len(strs)):
        
            d={}

            for j in range(len(strs[i])):
                if strs[i][j] in d:
                    d[strs[i][j]]+=1
                else:
                    d[strs[i][j]]=1
            
            la.append(d)
            
            

        ll=[]
        s=set()
        for i in range(len(la)):
            
                if i not in s:
                    for j in range(i+1,len(la)):
                        if la[i]==la[j]:
                            ll.append(strs[j])
                            s.add(j)
                   
                    aa.append([strs[i]]+ll) 
                s.add(i)
                
                ll.clear()
            

        return aa

        