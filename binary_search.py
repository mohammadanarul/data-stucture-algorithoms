import timeit

start_time = timeit.default_timer()


def binary_search(L, v):
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left+right) // 2 # integer division
        if L[mid] == v:
            return f'binary search result: {mid}'

        if L[mid] < v:
            left = mid + 1
        else:
            right = mid - 1
    return -1


stop_time = timeit.default_timer()

result = binary_search([1, 2, 5, 85, 6, 56, 54], 2)
print(result)
print("Time spain:", stop_time-start_time)