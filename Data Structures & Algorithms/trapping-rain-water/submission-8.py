class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)>1:
            water=0
            maxleft=height[1]
            length=len(height)-1
            maxr=[]
            maxright=height[len(height)-1]
            for j in range(len(height)-1,-1,-1):
                r=max(height[j],maxright)
                maxright=r
                maxr.append(r)

            maxr=maxr[::-1]
            maxr=maxr[1:]
            maxr.append(0)
            




        
            for i in range(len(height)-1):
                left=i-1
                right=i+1
                j=length-i
                if left<0:
                    continue
            
                l=max(maxleft,height[left])
                maxleft=l
                r=maxr[i]
                
                if l>height[i] and r>height[i]:
                    
                    water=min(l,r)-height[i]+water
                    


            return water
        return 0
        