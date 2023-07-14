"""
You have given a string A having Uppercase English letters.
You have to find how many times subsequence "AG" is there in the given string
"""
class Solution:
    """
    Approach: first find the Count of A in array and update it to res when we find "G" in string
    """
    def SpecialSubsequences(self,string):
        result,count_of_A=0,0
        for i in range(len(string)):
            if string[i]=="A":
                count_of_A+=1
            if string[i]=="G":
                result+=count_of_A
        return result

if __name__ == '__main__':
    string=input()
    print(Solution().SpecialSubsequences(string))