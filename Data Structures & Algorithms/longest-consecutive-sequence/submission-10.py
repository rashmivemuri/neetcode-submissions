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
            l.append(nums[i])
            L.append(l)
            if len(l)>len(L[0]):
                L.clear()
                L.append(l)  
        
        if (len(L)==0 or len(L[0])==0):
            return 0
        else:
            return len(L[0])
            