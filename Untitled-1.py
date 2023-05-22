from queue import *
if __name__ == '__main__':
    q= Queue(-1)

    print('----- Put -----')
    for x in range(1,6):
        print(f'Put {x}')
        q.put(x)

    print('----- Get -----')
    while not q.empty():
        gt = q.get()
        print(f'Get ->{gt}')

    

