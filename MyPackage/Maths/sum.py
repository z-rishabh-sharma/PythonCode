class Sum:
    
    def __init__(self):
        pass
        
    def sum(self, list=[], start=0):
        self.list = list
        sum = 0
        for i in range(start, len(self.list)):
            sum+=self.list[i]
        
        return sum
    
    
# tested
# s = Sum()
# print(s.sum([1,2,3,4,5,7], 3))