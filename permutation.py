def permutation(lst:list[int]) -> list[list[int]]:
    res = []
    def dfs(index):
        if index == len(lst):
            res.append(lst.copy())
        else:
            for i in range(index, len(lst)):
                lst[index], lst[i] = lst[i], lst[index]
                dfs(index+1)
                lst[index], lst[i] = lst[i], lst[index]

    index = 0
    dfs(index)