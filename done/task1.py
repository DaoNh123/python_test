# 16
# 17
# 18
# 19
# 20
# n = input()
# print(n.rjust(6, '0'))
# print(n.rjust(6, '#'))
# n = 1
# while n < 5:
#      print(n)
#      n += 1
# else :
#     print("end iterator")

#A1
# A2

# def sum (a, b):
#     res = a + b
#     return res
#
# # print(sum(1, 2))
# def hello(name1, name2, name3):
#     print("Hello :", name1, name2, name3)
#
# def infor(name, job = 'car driver'):
#     print(name, job)
#
# def tongHieu(a, b):
#     tong = a + b
#     hieu = a - b
#     return tong, hieu
#
# if __name__ == '__main__':
#     print(sum(1, 2))
#     hello("A", "B", "C")
#     hello(name3="name3", name1="name1", name2="name2")
#
#     infor("name1")
#
#     a, b = tongHieu(1, 2)
#     print(a, b)
# from math import *
#
# def checkPrime (a):
#     if(a < 0): return False
#     for i in range(2, floor(sqrt(a))+1):
#         if a % i == 0: return False
#
#     return a > 1
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     sumPrimes = 0
#     cnt = 0
#
#     for i in arr:
#         if checkPrime(i):
#             sumPrimes += i
#             cnt += 1
#
#     print('%.3f' % (sumPrimes / cnt))

# a3
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     min = min(arr)
#     cnt = 0
#     for i in arr:
#         if i == min: cnt += 1
#     print(cnt);

# a4
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     x = int(input())
#
#     cntGreater, cntLower = 0, 0
#     for i in arr:
#         if i < x: cntLower += 1
#         elif i > x: cntGreater += 1
#
#     print(cntLower)
#     print(cntGreater)

# a5
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     index = 0
#     check = True
#     for i in arr:
#         if i % 2 == 0 and index % 2 == 0:
#             print(i, end=" ")
#             check = False
#         index += 1
#     if check:
#         print("NONE")

# a6
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     arr.sort()
#
#     k = int(input())
#     cnt = 0
#
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == k:
#                 cnt += 1
#     print(cnt)

# a7
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     arr.sort()
#     minDif = max(arr) - min(arr)
#     for i in range(1, len(arr)):
#         if arr[i] - arr[i - 1] < minDif:
#             minDif = arr[i] - arr[i - 1]
#
#     print(minDif)

# a8
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     seen = set()
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             print(i, end=" ")

# a9
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     freArr = [0] * 1005
#     unique = []
#     for i in range(len(arr)):
#         freArr[arr[i]] = freArr[arr[i]] + 1
#         if arr[i] not in unique:
#             unique.append(arr[i])
#
#     for i in unique:
#         print(i, freArr[i], sep=' ', end='\n')

# a10
# from math import *
# def checkPrime (number):
#     for i in range(2, int(sqrt(number) + 1)):
#         if(number % i == 0): return False
#     return number > 1
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     leftSum = 0
#     rightSum = sum(arr) - arr[0]
#     for i in range(len(arr) - 1):
#         if(checkPrime(leftSum) and checkPrime(rightSum)):
#             print(i, end=" ")
#         leftSum += arr[i]
#         rightSum -= arr[i + 1]

# a11


# if __name__ == '__main__':
#     Fibo = []
#     Fibo.append(0)
#     Fibo.append(1)
#
#     for i in range(2, 93):
#         Fibo.append(Fibo[i - 1] + Fibo[i - 2])
#
#     n = int(input())
#     arr = list(map(int, input().split()))
#     found = False
#     for i in range(len(arr)):
#         if arr[i] in Fibo:
#             print(arr[i], end=" ")
#             found = True
#     if not found:
#         print("NONE")

# a11.2
# if __name__ == '__main__':
#     Fibo = set()
#     a, b = 0, 1
#     Fibo.add(a)
#     Fibo.add(b)
#
#     for i in range(2, 93):
#         tmp = b
#         b = a + b
#         a = tmp
#         Fibo.add(b)
#
#     n = int(input())
#     arr = list(map(int, input().split()))
#     found = False
#     for i in range(len(arr)):
#         if arr[i] in Fibo:
#             print(arr[i], end=" ")
#             found = True
#     if not found:
#         print("NONE")

# # a12
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     minArr = min(arr)
#     maxArr = max(arr)
#     posMin = 0
#     posMax = 0
#     for i in range(len(arr)):
#         if(arr[i] == minArr): posMin = i
#     for i in range(len(arr)):
#         if(arr[i] == maxArr):
#             posMax = i
#             break
#     print(posMin, posMax, sep=' ')

# a13
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     sum = 0
#     multiple = 1
#     mod = 10 ** 9 + 7
#     for i in range(len(arr)):
#         sum += arr[i]; sum %= mod
#         multiple *= arr[i]
#         multiple %= mod
#     print(int(sum))
#     print(int(multiple))

# a14
# from math import *
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(gcd(*arr))

# a15
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     arr.sort(reverse=True)
#     print(arr[0], arr[1], sep= ' ')

# 40
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     cntDict = dict()
#     for i in arr:
#         if i < 0: i = -i
#         if i == 0:
#             if i in cntDict:
#                 cntDict[i] += 1
#             else:
#                 cntDict[i] = 1
#         else:
#             while i > 0:
#                 num = i % 10
#                 if num in cntDict:
#                     cntDict[num] += 1
#                 else:
#                     cntDict[num] = 1
#                 i //= 10
#
#
#     for i in sorted(cntDict):
#         print(i, cntDict[i], sep=" ")

# 26
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     numDict = {}
#     for i in arr:
#         if i in numDict:
#             numDict[i] += 1
#         else:
#             numDict[i] = 1
#     print(len(numDict.keys()))

# 27
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     numDict = {}
#     for i in arr:
#         if i in numDict:
#             numDict[i] += 1
#         else:
#             numDict[i] = 1
#
#     for key, value in sorted(numDict.items()):
#         print(key, value, sep=" ")

# 28
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     numDict = {}
#     for i in arr:
#         if i in numDict:
#             numDict[i] += 1
#         else:
#             numDict[i] = 1
#
#     for key, value in numDict.items():
#         print(key, value, sep=" ")

# # 29
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     numDict = {}
#     for i in arr:
#         if i in numDict:
#             numDict[i] += 1
#         else:
#             numDict[i] = 1
#
#     sortedDict =  dict(sorted(numDict.items(), key=lambda item: (-item[1], item[0])))
#
#     firstKey, firstValue = next(iter(sortedDict.items()))
#     print(firstKey, firstValue, sep=" ")

# 30
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     numDict = {}
#     for i in arr:
#         if i in numDict:
#             numDict[i] += 1
#         else:
#             numDict[i] = 1
#
#     sortedDict =  dict(sorted(numDict.items(), key=lambda item: (-item[1])))
#
#     firstKey, firstValue = next(iter(sortedDict.items()))
#     print(firstKey, firstValue, sep=" ")
# a = 1
# if __name__ == '__main__':
    # dic1 = {1: 10, 2: 20}
    # dic2 = {3: 30, 4: 40}
    # dic3 = {5: 50, 6: 60}
    #
    # finalDict = {**dic1, **dic2, **dic3}
    # print(finalDict)

    # dic1 = {1: 'a'}
    # print("task 1")    # giải nén 1 lần chỉ ra "Key"

    # my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
    # my_dict['profession'] = 'Doctor'
    # print(my_dict['city'])
# if __name__ == '__main__':
#     # my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#     # del my_dict['profession']
#     # for key, value in my_dict.items():
#     #     print(key, value, sep=": ", end="\n");
#
#     # keys = ['Ten', 'Twenty', 'Thirty']
#     # values = [10, 20, 30]
#     #
#     # my_dict = dict(zip(keys, values))
#     # for key, value in my_dict.items():
#     #     print(key, value)
#     # print(my_dict)
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(len(arr)):
#         if i == 0 and (arr[0] * arr[1] < 0):
#             print(arr[0], end=" ")
#         elif (i < len(arr) - 1) and (arr[i] * arr[i + 1] < 0 or arr[i] * arr[i - 1] < 0):
#             print(arr[i], end=" ")
#         elif (i == len(arr) - 1) and (arr[i] * arr[i - 1] < 0):
#             print(arr[i], end=" ")

# a19
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.reverse()
#     for i in arr:
#         print(i, end=" ")

# a20
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(1, len(arr) - 1):
#         if(arr[i] > arr[i-1] and arr[i] > arr[i+1]):
#             print(arr[i], end=" ")

# a21
# if __name__ == '__main__':
#     n, k, x = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr.insert(x - 1, k)
#     for i in arr:
#         print(i, end=' ')

# a22
# if __name__ == '__main__':
#     n, x = map(int, input().split())
#     arr = list(map(int, input().split()))
#     found = False
#     resArr = []
#
#     for i in arr:
#         if i == x and found == False:
#             found = True
#         else:
#             resArr.append(i)
#
#
#     if not found:
#         print("NOT FOUND")
#     else:
#         for i in resArr:
#             print(i, end=" ")

#a23
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     sumArr = []
#     sumArr.append(arr[0])
#     for i in range(1, len(arr)):
#         sumArr.append(sumArr[i - 1] + arr[i])
#
#     for i in sumArr:
#         print(i, end=" ")

# # a24
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     sum = 0
#     for i in range(0, k - 1):
#         sum += arr[i]
#     for i in range(k - 1, n):
#         sum += arr[i]
#         print(sum, end=" ")
#         sum -= arr[i - (k - 1)]

# a25
# if __name__ == '__main__':
#     n, m, p = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#
#     a = a[:(p)] + b + a[(p):]
#     print(*a)

# # a26
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     k %= len(arr)
#
#     arr = arr[(k):] + arr[:(k)];
#     print(*arr)

# # a27
# if __name__ == '__main__':
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     k %= len(arr)
#
#     arr = arr[(n-k):] + arr[:(n-k)]
#     print(*arr)

# a28
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     res = [arr[0]]
#     for i in range(1, n):
#         if arr[i] != arr[i - 1]:
#             res.append(arr[i])
#     print(*res)

# 35
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     res = a[0]
#     for i in range(len(b)):
#         if b[i] == 1:
#             res += a[i + 1]
#         elif b[i] == 2:
#             res -= a[i + 1]
#     print(res)

# 36
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     minArr = min(arr)
#     maxArr = max(arr)
#     print(minArr)
#     for i in range(len(arr)):
#         if arr[i] == minArr:
#             print(i, end=" ")
#     print(maxArr)
#     for i in range(len(arr)-1, -1, -1):
#         if arr[i] == maxArr:
#             print(i, end=" ")
# c = 1111

# def outer():
#     c = 2804
#     def inner():
#         nonlocal c
#         c = 1000
#         print(c)
#     inner()
#     print(c)
#
# if __name__ == '__main__':
#     outer()
#     print(c)

# s = '28tech'
# a = list(s)
# print(a)
# print(type(a[0]))
#
# sumThree =  lambda a, b, c: a+b+c
# print(sumThree(1, 2, 3))
#
# a = [1, 2, 3, 4, 5]
# b = list(map(lambda x: x ** 2, a))
# print(b)  # [1, 4, 9, 16, 25]
#
# a1 = [-1, 2, 3, -4, 5]
# b1 = list(filter(lambda x: x > 0, a1))
# print(b1)  #  [2, 3, 5]

# findMax = lambda x,y: x if x > y else y
# print(findMax(100, 200))  #  200

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [x + 3 for x in a]
# print(b);  #[4, 5, 6, 7, 8, 9, 10, 11]

# def digitSum(n):
#     sum = 0
#     while n != 0:
#         sum += n % 10
#         n //= 10
#     return sum
#
# a = [123, 31, 20, 503, 114]
# b = [x for x in a if digitSum(x) > 5]
# print(b)  #[123, 503, 114]

# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [x for small_list in a for x in small_list]
#
# b = []
# for small_list in a:
#     for x in small_list:
#         b.append(x)

# data = ["28tech", "28tech@gmail.com", 2022]
# name, _, _ = data
# print(name)  # 28tech
#
# s = "CR7"
# a, b, c = s
# print(a, b, c) # C R 7
#
# a, b, c = range(0, 5, 2)
# print(a, b, c)  #  0 2 4

# my_set = {"28tech", "java", "python"}
# a, b, c = my_set
# print(a, b, c)

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# x, *y, z = a
# print(x, y, z)  #  1 [2, 3, 4, 5, 6, 7] 8
#
# a = (1, 2, 3)
# b = ("28tech", "python", "java")
# c = (2804, ) # Create tuple with 1 element need add 1 ","
# d = (2804)
# print(a)  # (1, 2, 3)
# print(b)  # ('28tech', 'python', 'java')
# print(c)  # (2804,)
# print(d)  # 2804

# s = "28tech"
# b = tuple(s)
# c = tuple([1, 2,  3])
# print(b)  # ('2', '8', 't', 'e', 'c', 'h')
# print(c)  # (1, 2, 3)

# a = ("28tech", [1, 2, 3], "java", "C++")
# a[1][0] = 100
# print(a)  #  ('28tech', [100, 2, 3], 'java', 'C++')

# a = (1, 5, 4, 2, 3)
# a = tuple(sorted(a))
# print(a)  #  (1, 2, 3, 4, 5)

# a = (5, 1, 1, 3, 1)
# print(a.count(1))  # 3
# print(a.index(1))  # 1

# from math import *
# a = [-100, 20, -30, 40, -50, 100]
# a = list(map(lambda x: x**2, a))
# print(a) # [10000, 400, 900, 1600, 2500, 10000]
#
# def add(a, b):
#     return a + b
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#     b = [2, 3, 4, 5]
#     c = list(map(add, a, b))
#     print(c)  # [3, 5, 7, 9]

# def even(num):
#     return num % 2 == 0
#
# if __name__ == '__main__':
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     b = list(filter(even, a))
#     print(b)  # [2, 4, 6, 8, 10]
#
# from math import *
# # stable
#
# if __name__ == '__main__':
#     a = [3, 1, 2, 4, 5]
#     a.sort(reverse = True)
#     print(a)  # [5, 4, 3, 2, 1]

# from math import *
# # stable
#
# if __name__ == '__main__':
#     a = [-3, -1, 2, -4, 5]
#     a.sort(key = abs)
#     print(a)  # [-1, 2, -3, -4, 5]

# from math import *
# # stable
# def sum_digit(n):
#     sum = 0
#     while n != 0:
#         sum += n % 10
#         n = n // 10
#     return sum
#
# if __name__ == '__main__':
#     a = [333, 11, 2, 10, 30, 19, 98, 10, 123, 3303]
#     a.sort(key = sum_digit)
#     print(a)  # [10, 10, 11, 2, 30, 123, 333, 3303, 19, 98]

# from math import *
# # stable
#
# if __name__ == '__main__':
#     a = [[1, 2], [3, 2], [1, 1], [4, 1], [3, 1]]
#     a.sort(key = lambda x: (x[0], -x[1]))
#     print(a)  # [[1, 2], [1, 1], [3, 2], [3, 1], [4, 1]]

# from math import *
# from functools import cmp_to_key
#
# def cmp (a, b):
#     if a < b:
#         return -1   # Tương đương False, giữ nguyên a trước, b sau
#     elif a > b:
#         return 1    # Đổi chỗ a và b
#     else:
#         return 0
#
#
# a = [10, 2, 3, 1, 4, 5, 6, 3, 0]
# a.sort(key = cmp_to_key(cmp)) # [0, 1, 2, 3, 3, 4, 5, 6, 10]
# print(a)

# from math import *
# from functools import cmp_to_key
#
# def sum_digit (num):
#     sum = 0
#     while num != 0:
#         sum += num % 10
#         num = num // 10
#     return sum
#
# def cmp (a, b):
#     if sum_digit(a) != sum_digit(b):
#         return sum_digit(a) - sum_digit(b) # sum_digit increses
#     else:
#         return b - a  # number decreases
#
# a = [30, 30000, 12, 21, 111, 9, 19, 10, 20, 30]
# a.sort(key = cmp_to_key(cmp)) # [10, 20, 30000, 111, 30, 30, 21, 12, 9, 19]
# print(a)

# s = {"28tech", "python", "28tech", "java", "set", "set"}
# print(s)  # {'28tech', 'python', 'set', 'java'}
# t = {1, 2, 3, 1, 2, "abcd"}
# print(t)  # {1, 2, 3, 'abcd'}

# if __name__ == '__main__':
#     s = {1, 2, 3, 4, 5}
#     s.update({1, 2, 8, 9})
#     print(s)  # {1, 2, 3, 4, 5, 8, 9}

# if __name__ == '__main__':
#     infor = {
#         'name': '28tech',
#         'job': 'dev',
#         'salary': 500,
#         'web': '28tech.com.vn',
#         'city' : 'HCM'
#     }
#     print(infor)

    # a = [['name', '28tech'], ['job', 'dev'], ['salary', '500']]
    # b = dict(a)
    # print(b)

    # a = ['name', 'job', 'web']
    # b = ['28tech', 'dev', '28tech.com.vn']
    # c = dict(zip(a, b))
    # print(c)

    # a = ['name', 'job', 'web']
    # defaultValue = ''
    # b = dict.fromkeys(a, defaultValue)
    # print(b)

# if __name__ == '__main__':
#     a = [1, 2, 3, 4]
#     d1 = dict({})
#     for x in a:
#         d1[x] = x ** 2
#
#     #dict comp
#     d2 = {x : x ** 2 for x in a}
#     print(d1)
#     print(d2)

# from collections import Counter
#
# if __name__ == '__main__':
#     a = [1, 2, 1, 3, 1, 4, 1, 0, 2, 5]
#     c = Counter(a)  #
#     c_dict = dict(c)                # Counter to Dict
#     c_list = list(dict(c.items())) # Counter to List
#     print(c)  # Counter({1: 4, 2: 2, 3: 1, 4: 1, 0: 1, 5: 1})

# s = "28tech  python C++"
# a = s.split()
# print(a) # ['28tech', 'python', 'C++']

# a = ['28tech', 'python', 'C++']
# t = ','.join(a)
# print(t)        # 28tech,python,C++
# u = '##'.join(a)
# print(u)        # 28tech##python##C++

# s = '%s is %d years old' % ('CR7', 37)
# t = 'Pi = %.2f' % (3.14159)
# print(s)        # CR7 is 37 years old
# print(t)        # Pi = 3.14

# s = '{0} is {1} years old!'.format('CR7', 37)
# print(s)        # CR7 is 37 years old!
#
# name = 'CR7'
# age = 37
# s = f'{name} is {age} years old!'
# print(s)        # CR7 is 37 years old!

# class Person:
#     nationality = 'Vietnam'     # Class attribute
#
#     def __init__(self, name, job, salary):
#         self.name = name        # public
#         self._job = job         # protected
#         self.__salary = salary  # private
#
#     def greet(self):
#         print('Hello')
#
#     def showInfor(self):
#         print('Name = {}, Job: {}, Salary: {}'.format(self.name, self._job, self.__salary))
#
#     def get_name(self):
#         return self.name
#     def get_job(self):
#         return self._job
#     def set_name(self, name):
#         self.name = name
#     def set_job(self, job):
#         self._job = job
#
# if __name__ == '__main__':
#     p = Person('John', 'Python', 20000)
#     p.showInfor()   # Name = John, Job: Python, Salary: 20000
#
# class SoPhuc:
#     def __init__(self, thuc, ao):
#         self.thuc = thuc
#         self.ao = ao
#
#     def __add__(self, other):
#         self.thuc += other.thuc
#         self.ao += other.ao
#         return SoPhuc(self.thuc, self.ao)
#
#     def __str__(self):
#         return f'{self.thuc} + {self.ao}j'
#
# if __name__ == '__main__':
#     s1 = SoPhuc(2, 3)
#     s2 = SoPhuc(3, 1)
#     s3 = s1 + s2
#     print(s3)       # 5 + 4j

# class Nguoi:
#     def __init__(self):
#         print('Ham khoi tao cua lop cha')
#     def xinchao(self):
#         print('Nguoi xin chao! \n')
#
# class SinhVien(Nguoi):
#     def __init__(self):
#         print('Ham khoi tao cua lop con')
# class GiaoVien(Nguoi):
#     pass
# class NhanVien(Nguoi):
#     pass
#
# if __name__ == '__main__':
#     s = SinhVien()
#     s.xinchao()
#
#     g = GiaoVien()
#     g.xinchao()

# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#
# class Student(Person):
#     def __init__(self, name, birth, gpa):
#         super().__init__(name, birth)
#         self.gpa = gpa

# class Person:
#     def __init__(self, name, birth):
#         self.name = name
#         self.birth = birth
#     def show(self):
#         return f'{self.name} is {self.birth} years old'
#
# class Student(Person):
#     def __init__(self, name, birth, gpa):
#         Person.__init__(self, name, birth)
#         self.gpa = gpa
#     def display(self):
#         print(f'{self.name}, {self.birth}, {self.gpa:.2f}')
#     # def show(self):
#     #     return Person.show(self) + ' ' + f'{self.gpa:.2f}'
#     def show(self):
#         return super().show() + ' ' + f'{self.gpa:.2f}'
#
# if __name__ == '__main__':
#     s = Student('John', 19, 2.5)
#     print(s.show())
# import os
#
# if os.path.exists('text.txt'):
#     print("Found text.txt")
# else:
#     print("Not found text.txt")
#
# if os.path.exists('test2.txt'):
#     print("Found test2.txt")
# else:
#     print("Not found test2.txt")