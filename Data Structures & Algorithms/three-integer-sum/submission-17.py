class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums=list(tuple(sorted(nums)))
        s=set()
        L=[]
        l=len(nums)
        for i in range(l):
            j=i+1
            k=l-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            target=-(nums[i])
            while k>j:
                if nums[k] + nums[j] < target:
                    j += 1
                elif nums[k] + nums[j] == target:
                    
                    trip=tuple([nums[i], nums[j], nums[k]])
                    if trip not in s:
                        s.add(trip)
                        L.append(list( trip))
                    j+=1
                    k-=1
                elif nums[k] + nums[j] > target:
                    k -= 1
        return L