class Solution:
    def Sum(self,n):
        add=0
        while(n>0):
            digit=n%10
            add+=digit
            n//=10
        return add
    def Count(self,n):
        count=0
        while(n>0):
            count+=1
            n//=10
        return count
    def Solution(self,n):
        added=self.Sum(n)
        count=self.Count(added)
        while(count>1):
            added=self.Sum(added)
            count=self.Count(added)
        return added
n=int(input())
for i in range(n):
    k=int(input())
    print(Solution().Solution(k))