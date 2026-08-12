class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        L=[]
        for i in range(len(nums)):
            if nums[i]-1 in s:
                continue
            l=[]
            num=nums[i]
            for j in range(len(nums)):
                
                if num+1 in s:
                    l.append(num+1)
                    num=num+1
            l.insert(0,nums[i])
            L.append(l)
        
        if nums!=[]:
            max=len(L[0])
            for i in range(1,len(L)):
                if len(L[i])>max:
                    max=len(L[i])
             
               
        
            return max
        return 0