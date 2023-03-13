class Demo:

    # n = 0
    # default value
    def __init__(self, name="", list=[], dict={}):
        self.name = name
        self.list1 = list
        self.dict1 = dict

    def searchValue(self, name):
        pass

    def saveValue(self):
        pass

    def deleteValue(self):
        pass

    def __len__(self):
        print("list1 : ", len(self.list1))
        print("dict1 : ", len(self.dict1))
        return len(self.list1) + len(self.dict1)

    def sum(self):
        lsum = sum(self.list1)
        dsum = sum(self.dict1.values())
        print("List1 :", lsum)
        print("dict1 :", dsum)
        return lsum + dsum

    def __iter__(self):
        self.n = 0
        return self  # here we are returning the current object

    def __next__(self):
        if self.n < len(self.list1):
            result = self.list1[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration  # exception will give stop the iteration


# a = Demo("rishabh", [2, 3, 4], {"size": 4, "volume": 3})
# len(a)
# a.sum()
# a.sum(a)
# for i in a:
#     print(i)
# for i in a:
#     print(i)
# for i in a:
#     print(i)
# for i in a:
#     print(i)



# m = iter(a)  # this will give the generator to m
# next(m.)
