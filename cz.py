import random 

def sapxep(n):
    lct =[]
    for n in range(n):
     hh = random.randint(0,100)
     lct.append(hh)
    return lct


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def main():
    lst= sapxep(6)
    print("day so ban dau la\n", lst)
    merge_sort(lst)
    print("day moi la\n", lst)

if __name__ =='__main__':
    main()
