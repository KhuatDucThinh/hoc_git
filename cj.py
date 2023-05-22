def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst=(1,5,7,2,4)
bz=bubble_sort(lst)
print(bz)
