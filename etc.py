d = {"key1" : "item1", "key2": "item2", "kucing" : [3, "Jerapah"]}

for item in d.keys():
    print(item)

# for item in d.values():
#     print(item)

# for item in d.items():
#     print(item)

# d['Burung'] = {'Buku': 'Tas'}

print(d.keys())
# print(d.values())    

# t = (1, [0, 'test'], {'a1':True})

# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1] = 'mark'
# print(t[1])

# list_1 = [1,2,'String']
# list_2 = ['Kucing', 'Buku', 3 ]

# for i, j,k in zip(list_1, list_2, range(5)):
#     print(i, j, k)

# for item in zip(list_1, list_2,range(3)):
#     print(item)

# s  ={1, 3, 1, 2, 2, 3, 'string', 'string'}
# print(s)
# # print(s[2])
# print(list(s)[2])

# newList = [1,3, 2, 3, 'test2', 'test1', 'test1']
# s = set(newList)

# print(s)
# print(list(s)[2])

# listNum = [1,2,3,4,5]
# listNum = ['Nomor {} {}'.format(item, item1) for item in listNum if item > 2 for item1 in range(5) if item1 <3]
# print(listNum)

# dictNum = {i:j for i, j in zip(listNum, range(5))}
# print(dictNum)


# ##Without Lambda
# def times2(num):
#     return num * 2

# listNum = [1,2,3,4,5]
# listNum = map(times2, listNum)
# print(listNum)

# ##With Lambda
# listNum = [1,2,3,4,5]
# listNum = list(map(lambda num: num*2, listNum))
# print(listNum)

# ##Without Lambda
# def genap(num):
#     return num % 2 == 0

# listNum = [1,2,3,4,5]
# listNum = list(filter(genap, listNum))
# print(listNum)

# #With Lambda
# listNum = [1,2,3,4,5]
# listNum = list(filter(lambda num: num%2 == 0, listNum))
# print(listNum)


# numList = [1,2,3]

# numDict = {1:'String', 'Not':'true'}
# input = 'x'

# check1 = input in numList
# check2 = 'x' in ['x', 'y', 'z']
# check3 = 'ka' in 'kurakas'

# check4 = 'true' in numDict
# check5 = 1 in numDict

# print(check1)
# print(check2)
# print(check3)
# print(check4)
# print(check5)

print('| |')
print('| |')
print(' __ ')
print('|  |')
print('__')