from multiprocessing import Process


class Multiprocessing:

    def __init__(self, arg, process=1):
        self.a = []
        self.pr = process
        self.n = len(arg)//process
        for i in range(0, len(arg), self.n):
            self.a.append(arg[i: i+self.n])

    @staticmethod
    def f(ls):
        print(ls)

    def start(self):
        for i in self.a:
            p = Process(target=self.f, args=(i,))
            p.start()
            p.join()


if __name__ == '__main__':
    M = Multiprocessing(["start", "Go", "Stop", "Run", "Sleep", "Wake"], 3)
    M.start()
    # Multiprocessing.f(["error"])
