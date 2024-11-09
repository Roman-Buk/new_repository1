class GI:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield i
gen_iter = GI(1, 10)

for value in gen_iter:
    print(value)



