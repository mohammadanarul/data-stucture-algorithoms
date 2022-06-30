def selection_sort(l):
    n = len(l)
    for i in range(0, n - 1):
        index_min = i
        for j in range(i + 1, n):
            if l[j] < l[index_min]:
                index_min = j
            if index_min != i:
                l[i], l[index_min] = l[index_min], l[i]


if __name__ == '__main__':
    Lit = [5, 1, 3, 5, 62, 23, 5, 2, 4, 6, 88, 9, 9, 23, 1]
    print(Lit)
    selection_sort(Lit)
    print(Lit)
