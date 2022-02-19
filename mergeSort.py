def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

def merge(llst, rlst):
    if len(llst) == 0:
        return rlst
    if len(rlst) == 0:
        return llst
    if llst[0] <= rlst[0]:
        return [llst[0]] + merge(llst[1:], rlst)
    else:
        return [rlst[0]] + merge(llst, rlst[1:])

if __name__ == '__main__':
    print(merge_sort([1, 5, 3, 4, 2, -1 , -2, -3]))
