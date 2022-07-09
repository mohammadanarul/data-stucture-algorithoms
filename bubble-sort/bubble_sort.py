"""
    list = [8, 2, 4, 1, 5]

    step-1: [8, 2, 4, 1, 5] => [2, 8, 4, 1, 5]
    step-2: [2, 8, 4, 1, 5] => [2, 4, 8, 1, 5]
    step-3: [2, 4, 8, 1, 5] => [2, 4, 1, 8, 5]
    step-4: [2, 4, 1, 8, 5] => [2, 4, 1, 5, 8]
    step-5: [2, 4, 1, 5, 8] => [2, 1, 4, 5, 8]
    step-6: [2, 4, 1, 5, 8] => [2, 1, 4, 5, 8] # first and second number alredy sorted
    step-7: [2, 1, 4, 5, 8] => [1, 2, 4, 5, 8] # final result the list.
"""
import time

start = time.time()
def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
time.sleep(1)
end = time.time()
if __name__ == '__main__':
    L = [3, 5, 8, 4, 1, 9, -2]
    bubble_sort(L)
    print(L)
    print(f"Runtime of the program is {end - start}")
