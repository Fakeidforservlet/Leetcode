class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # merged=[]
        # i,j=0,0
        # while i<len(nums1) and j<len(nums2):
        #     if nums1[i]<nums2[j]:
        #         merged.append(nums1[i])
        #         i+=1
        #     else: 
        #         merged.append(nums2[j])
        #         j+=1
        # while i<len(nums1):
        #     merged.append(nums1[i])
        #     i+=1
        # while j<len(nums2):
        #     merged.append(nums2[j])
        #     j+=1
        # return merged  

        #https://www.youtube.com/watch?v=n7uwj04E0I4
        k=m+n-1
        i=m-1
        j=n-1
        while  j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] =  nums2[j]
                j-=1
                k-=1   
        
        return nums1

