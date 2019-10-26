#Fungsi sort
arr_1 = [40, 100, 1, 5, 25, 10]

def fungsi_sort_ascending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def fungsi_sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr    

def minmax(arr):
    angka_min = fungsi_sort_ascending(arr)[0]
    angka_max = fungsi_sort_descending(arr)[0]
    return print('Nilai tertinggi {} dan nilai terendah {}'.format(angka_max,angka_min))

fungsi_sort_ascending(arr_1)
print(arr_1)

fungsi_sort_descending(arr_1)
print(arr_1)

minmax(arr_1)

