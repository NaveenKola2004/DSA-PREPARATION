class Solution:
    def Number_To_Binary(self,number):
        res=""
        while (number>=1):
            if (number%2==1):
                res+='1 '
            else:
                res+='0 '
            number//=2
        return res[::-1]
print(Solution().Number_To_Binary(232))