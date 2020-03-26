class Solution:
    def findMedianSortedArrays(self,nums1,nums2) ->float:
        m = len(nums1)
        n = len(nums2)
        if m<n:
            nums1,nums2,m,n = nums2,nums1,n,m
        if n == 0:
            raise ValueError

        imin,imax,half_len = 0,m,(m+n+1)/2
        while imin<=imax:
            i = (imin + imax)/2
            j = half_len - i
            if i<m and nums2[j-1]>nums1[i]:
                imin = i+1
            elif i>0 and nums1