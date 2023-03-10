from functools import reduce
class Iterable:
    def __init__(self, n, records) -> None:
        self.current = 0
        self.n = n
        self.records = records
        pass

    def __next__(self):
        output = ''
        if self.current < len(self.records):
            for r in self.records[self.current: self.current+self.n]:
                output += str(r)
            self.current += self.n
            return output
        raise StopIteration
    
class Records:
    def __init__(self, records) -> None:
        self.records = records
        self.current = 0
        pass


    def iterator(self, n):
        current = 0
        while current < len(self.records):
            group_number = current // n + 1
            output = reduce(lambda s, t: str(s) + str(t), 
                        self.records[current:current+n], f'{group_number} group:\n')
            yield output
            current += n
    
rec = Records([3, 4, 5, 6, 7, 8, 9, 0, 7])

gen = rec.iterator(4)
print(next(gen))
print(next(gen))
print(next(gen))







