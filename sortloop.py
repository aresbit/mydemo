
# sort by recursion

def sort(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return insert(sort(tl), hd)

def insert(lst, x):
    if lst == []:
        return [x]
    else:
        hd, tl = lst[0], lst[1:]
        if x <= hd:
            return [x] + lst
        else:
            return [hd] + insert(tl, x)


# sort by iteration
def sort_bubble(lst):
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst





if __name__ == '__main__':
    print(sort([1, 5, 3, 4, 2, -1 , -2, -3]))
    print(sort_bubble([1, 5, 3, 4, 2, -1 , -2, -3]))


