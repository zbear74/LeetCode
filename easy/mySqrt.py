# class Solution:
#     def mySqrt(self, x: int) -> int:

class Solution:        
    def mySqrt(self, l: int) -> int:
        rslt = l
        div = l
        if l <= 0:
            return 0
        while True:
            div =  (l / div + div) / 2
            if rslt > div:
                rslt = div
            else:
                return int(rslt)
      


print(Solution().mySqrt(4))
print(Solution().mySqrt(144))
  