# leetcode problems: 455
# Description: Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi,
# which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
    def findContentChildren(self, g, s) -> int:
        # sort the lists
        g.sort()
        s.sort()
        # initialize the counter
        count = 0
        # iterate over the greed factor list
        for i in range(len(g)):
            # iterate over the cookie list
            for j in range(len(s)):
                # check if the cookie size is greater than or equal to the greed factor
                if s[j] >= g[i]:
                    # increment the counter
                    count += 1
                    # remove the cookie from the list
                    s.pop(j)
                    # break out of the loop
                    break
        # return the count
        return count

# this same code using while loop

class Solution:
    def findContentChildren(self, g, s) -> int:
        # sort the lists
        g.sort()
        s.sort()
        # initialize the counter
        count = 0
        # iterate over the greed factor list
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            # check if the cookie size is greater than or equal to the greed factor
            if s[j] >= g[i]:
                # increment the counter
                count += 1
                # remove the cookie from the list
                j += 1
                # break out of the loop
                i += 1
            else:
                j += 1
        # return the count
        return count
