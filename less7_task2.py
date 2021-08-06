from random import randint

massive = [randint(0,50) for x in range(10)]
print(f'Исходный массив:\n{massive}')


def sort_merge(l, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        sort_merge(l, start, mid)
        sort_merge(l, mid, end)
        merge_list(l, start, mid, end)


def merge_list(l, start, mid, end):
    left = l[start:mid]
    right = l[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid) and (mid + j < end):
        if left[i] <= right[j]:
            l[k] = left[i]
            i = i + 1
        else:
            l[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            l[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            l[k] = right[j]
            j = j + 1
            k = k + 1


sort_merge(massive, 0, len(massive))
print(f'\nОтсортированный массив:\n{massive}')
