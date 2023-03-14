from len import length
 
class Maxi:
    
    def __init__(self):
        pass
    
    
    def maximum(self, list=[]):
        self.val = -1
        for i in range(0, length(list)):
            if self.val < list[i]: 
                self.val = list[i]
        
        return self.val
    
    
m = Maxi()

print(m.maximum([1,2,3,43,4,3,2,3,3,3,3,2]))