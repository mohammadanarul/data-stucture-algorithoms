import time
# Utility function to swap values at two indices in the list
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Recursive function to perform bubble sort on sublist `A[i…n]`
start = time.time()
def bubble_sort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)

    if n - 1 > 1:
        print(A)
        bubble_sort(A, n - 1)
time.sleep(1)
end = time.time()

if __name__ == '__main__':
    A = [8, 2, 4, 1, 5]
    print(A)
    bubble_sort(A, len(A))

    # print the sorted list
    print(A)
    # total time taken
    print(f"Runtime of the program is {end - start}")