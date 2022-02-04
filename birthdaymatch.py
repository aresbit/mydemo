# data structure: and algorithm:
# how to sovlve this problem: correct  + efficient
# birthday_match
# static array

class StaticArray:
    def __init__(self, n) -> None:
        self.data = [None] * n
    def at(self, i):
        if not  (0 <= i < len(self.data)): raise IndexError
        return self.data[i]

    def set(self, i, x):
        if not  (0 <= i < len(self.data)): raise IndexError
        self.data[i] = x
    
    def size(self):
        return len(self.data)

def birthday_match(students):
    n = len(students)
    record = StaticArray(n)

    for i in range(n):
        (name, bday) = students[i]
        for j in range(i):
            (name2, bday2) = record.at(j)
            if bday == bday2:
                return True
        record.set(i, (name, bday))
    return False

