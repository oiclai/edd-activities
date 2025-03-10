exemplo = [5, 9, 7, 21, 18, 1, 4]
print(exemplo)


def bubble_sort(array:list)->list:
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# exemplo_depois = bubble_sort(exemplo)
# print(exemplo_depois)

'''
len(array) = 7
primeiro loop (6, 0, -1) [i] -> ao contrario pq joga o maior p final ja o deixando na sua posição ordenada
    primeiro loop (6) [j]
        se 5 > 9:
        se 9 > 7:
            troca
        5, 9, 7, 21, 18, 1, 4
'''

def selection_sort(array:list)->list:
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]
    return array

exemplo_depois = selection_sort(exemplo)
print(exemplo_depois)

'''
len(array) = 7
primeiro loop (6) [i]
    min = 0
    primeiro loop (1) [j]
        se 9<5:
        se 7<5
        se 21<5
        se 18<5
        se 1<5
            min = j
        se 4<1
        5, 9, 7, 21, 18, 1, 4

'''

def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        fofo = array[i]
        j = i-1
        while j >= 0 and fofo < array[j]:
            array[j+1] = array[j] 
            j -= 1
        array[j+1] = fofo 
    return array

exemplo_depois = insertion_sort(exemplo)
print(exemplo_depois)
'''
        5, 9, 7, 21, 18, 1, 4
len(array) = 7

primeiro loop (1, 7) [i]
    fofo = array[1] (9)
    j = 1 - 1 (0)
    enquanto 0 >= 0 and 9 < 5:
        n entra
    array[0+1] = fofo (9)
5, 9, 7, 21, 18, 1, 4
    - segundo loop
    enquanto 1 >= 0 and 7 < 9:
        entra
        array[1+1] = array[1] -> 9 vai p frente
        j = 1 - 1

5, 7, 9, 21, 18, 1, 4
        '''