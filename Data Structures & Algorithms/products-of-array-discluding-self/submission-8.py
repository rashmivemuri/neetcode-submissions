class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l=[]
        count=0       
        prod1=1
        prod2=1
        for i in range(len(nums)):
            prod2*=nums[i]
            if nums[i]==0:
                count+=1
                continue
            else:
                prod1*=nums[i]
            
            


        for i in nums:
            if count>=2:
                l.append(0)
            else:
                if i!=0 and prod2==0:
                    l.append(0)
                elif i==0:
                    l.append(prod1)
                elif prod2!=0:
                    l.append(int(prod2/i))
        return l
