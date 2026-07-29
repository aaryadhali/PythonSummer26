#sub = "abcabcbb"
""" check each letter, store it, also populate a string with the checked letters,
 if the next letter matches the comparison one then stop"""

"""another approach: have the string as an array and start taking out all dupes"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set() #to keep unique vals
        #pointers l and r
        l = 0
        result = 0
        for r in range(len(s)):
            #if we get to a dupe update window and set
            while s[r] in charSet:
                charSet.remove(s[l]) #removes left most char
                l+=1 #increments the left ptr by 1
            charSet.add(s[r]) #after rmeoving dupes add rightmost char to the set
            result = max(result, r - l + 1)

        return result

        check = 0
        strlist = list(s)
        #returnstr = ""
        for i in strlist[1:]:
            #returnstr += s[i]
            #check = s[i]
            if strlist[check] == i:
                strlist.insert(i, " ")
                check+=1

        return strlist#returnstr
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))

        