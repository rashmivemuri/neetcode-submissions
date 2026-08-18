class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxh=0
        
        while j>i:
            max=(j-i)*min(heights[i],heights[j])
            if max>maxh:
                maxh=max
            if (heights[i]>heights[j]):
                j-=1
            elif(heights[i]<heights[j]):
            
                i+=1
            else:
                i+=1
                j-=1

        return maxh


        