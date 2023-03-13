import json
class Sample:
    
    dict = {}
    
    def __init__(self, path=""):
        self.pth = path
        
        if path != "":
            with open(path , "r+") as file:
                self.f= file.read()
                file.seek(0) # after the above the line ended and we have to shift the iterator again to the zero and then we can use it to the load function
                self.df = json.load(file)
        else:
            print("please provide the path")
        
    
    def readFileAsJson(self):
        print(self.f)
        
    def readAsDataType(self):
        print(self.df)

    
    def writeJson(self, path, data):
        with open(path , "w+") as file:
            file.write(json.dumps(data, indent=2))
            
        with open(path , "r+") as file:
            print(file.read())
            
        
        
        
    
# S = Sample()
# S.readFileAsJson()
# S.readAsDataType()
# S.writeJson("sample.json", {"name": "Unknown", "url":"Nothing", "Welcome_text":"Greet"})



# genrator : where are some condition or some event driven approach
def Range(n):
    for i in range(n):
        # print (i)
        yield i
        

Range(10)
# for x in Range(10):
#     print(x)
    
# for x in Range(5):
#     print(x)
    
