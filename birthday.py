

class StaticArray:
    def __init__(self, n):
        self.data = [None] * n
    def at(self, i):
        return self.data[i]
    def set(self, i, x):
        if not 0 <= i < len(self.data):
            raise IndexError('index out of range')
        self.data[i] = x
    def __len__(self):
        return len(self.data)

def birthday_match(student):
    n = len(student)
    record = StaticArray(n) 
    for k in range(n):
        (name1, birthday1) = student[k]
        for j in range(k):
            (name2, birthday2) = record.at(j)
            if birthday1 == birthday2:
                return (name1, name2)
        record.set(k, (name1, birthday1))
    return None

        
         