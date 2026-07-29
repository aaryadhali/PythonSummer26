class Solution(object):
    arr1 = [1,2]
    arr2 = [3,4]
    def findMedianSortedArrays(self, nums1, nums2):
        numbers = nums1 + nums2
        result = sorted(numbers)
        length = len(result)
        #print(length//2)
        lsum = sum(result)
        if length%2 == 1:
            #print("hi")
            return result[length//2] 
        else:
            #print("bye")
            print(result[length//2])
            print(result[length//2 - 1])

            return (result[length//2] + result[length//2-1])/2
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #return numbers

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays(sol.arr1,sol.arr2))
        