import math
class Den:
    ints = []
    strs = []
    def getInf(self):
        a = []
        a = input().split()
        return a
    def distribution(self,a):
        for i in a:
            try:
                int(i)
                self.ints.append(int(i))
            except ValueError:
                self.strs.append(i)
        return self.ints, self.strs
    def go(self):
       return self.distribution(self.getInf())
den = Den()
print(den.go())
#TIMOF



