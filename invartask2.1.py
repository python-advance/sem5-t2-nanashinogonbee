class Fibonacci:
    def __init__(self):
        self.result = [0, 1]

    def __iter__(self):
        self.initial = self.result
        return self

    def __next__(self):
        self.initial.append(self.initial[-1] + self.initial[-2])

    def find(self, max):
        while max >= self.result[-1]:
            self.result.append(self.result[-1] + self.result[-2])
        if max < self.result[-1]:
            self.result.pop()
        return self.result


fib = Fibonacci()
print(fib.find(int(''.join(x for x in input(': ') if x.isdigit()))))

