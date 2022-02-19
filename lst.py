
def length(lst):
    if lst == []:
        return 0
    else:
        hd, tl = lst[0], lst[1:]
        return 1 + length(tl)

def length_acc(lst, acc):
    if lst == []:
        return acc
    else:
        hd, tl = lst[0], lst[1:]
        return length_acc(tl, acc + 1)

def length2(lst):
    return length_acc(lst, 0)



def sum(lst):
    if lst == []:
        return 0
    else:
        hd, tl = lst[0], lst[1:]
        return hd + sum(tl)


def sum_acc(lst, acc):
    if lst == []:
        return acc
    else:
        hd, tl = lst[0], lst[1:]
        return sum_acc(tl, acc + hd)

def sum2(lst):
    return sum_acc(lst, 0)


def odds(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        if hd % 2 == 1:
            return [hd] + odds(tl)
        else:
            return odds(tl)


def odds_acc(lst, acc):
    if lst == []:
        return acc
    else:
        hd, tl = lst[0], lst[1:]
        if hd % 2 == 1:
            return odds_acc(tl, acc + [hd])
        else:
            return odds_acc(tl, acc)

def odds2(lst):
    return odds_acc(lst, [])

def my_append(lst1, lst2):
    if lst1 == []:
        return lst2
    else:
        hd, tl = lst1[0], lst1[1:]
        return [hd] + my_append(tl, lst2)

def my_append_acc(lst1, lst2, acc):
    if lst2 == []:
        return acc
    else:
        hd, tl = lst2[0], lst2[1:]
        return my_append_acc(lst1, tl, acc + [hd])  


def my_append2(lst1, lst2):
    return my_append_acc(lst1, lst2, lst1)   

def rev(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return rev(tl) + [hd]

def rev_acc(lst, acc):
    if lst == []:
        return acc
    else:
        hd, tl = lst[0], lst[1:]
        return rev_acc(tl,  [hd] + acc)

def rev2(lst):
    return rev_acc(lst, [])




if __name__ == '__main__':
    # print(length([1, 2, 3, 4, 5]))
    # print(sum([1, 2, 3, 4, 5]))
    # print(length2([1, 2, 3, 4, 5,8,9,10]))
    # print(sum2([1, 2, 3, 4, 5, 6]))
    # print(odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # print(odds2([1, 2, 3, 4, 5, 6, 7, 8, ]))
    # print(my_append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12,18, 19, 20]))
    # print(my_append2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 20]))
    print(rev([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(rev2([1, 2, 3, 4, 5, 6, 7, 8, 9]))




