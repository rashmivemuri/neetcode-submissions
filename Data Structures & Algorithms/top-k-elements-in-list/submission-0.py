class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
       

        prev_max=0
        curr_max=0
        l=[]
        for p in range(k):
            for i,j in dict.items():
                if j>prev_max:
                    prev_max=j
                    d=i
            l.append(d)
            dict.pop(d)
            prev_max=0
        return l
    
        