def lenear_search(L, v):
    n = len(L)
    i = 0
    while i < n:
        if L[i] == v:
            print(f'result {i}')
            return i
        i += 1
    i = -1
    return i


result = lenear_search([1, 5, 85, 6, 56, 54, 2], 2)
print(result)
