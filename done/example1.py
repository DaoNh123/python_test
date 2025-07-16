from math import gcd

# print(gcd(4,8))
#
# # print
# print('python', 'java', 'C++', sep=' ', end = '!\n')

"""
    Comment type 2
    sdfadsf
"""

# L4: Variable and type
"""
  variable name can not have "space"
    type: int, floating numbers, complex numbers (Số phức có phần ảo)    
"""
# a = 100
# print("type of (a): ", type(a), end='\n')
# print(a)
#
# A = 100
# print("\ntype of (A): ", type(A), end='\n')
# print(A)
# B = 100.0
# print("\ntype of (B): ", type(B), end='\n')
# print(B)
#
# # print follow a format
# c = 100.12945
# print('%.2f' % c)
# print('%.3f' % c)
# print('{:.2f}'.format(c), end = '___')
# print('{:.3f}'.format(c))
#
# d = 5 + 4j
# print(type(d), end='\n')
#
# e = True
# print(type(e), end = '\n')
#
# #  force type
# s = '1234.1234'
# print(type(float(s)), end='\n')

# L5: Operator in python
# m, n, p = 1, 2, 3
# print(m, n, p, sep = ' ', end='\n')
# a , b = 100, 200
# a, b = b, a
# print(a, b) # 200 100
# print(a**2)
# print('   \n')
# print('and(20==20)and(1<0): ', (20==20)and(1<0))
#
# c = [1,2,3]
# d = [1,2,3]
# print(c == d)    # True
# print(c is d)   # False
#
# s = '28tech C++ programing python java 28tech.com.vn'
# print ('28tech.com.vn' in s)    # True ('in' kiểm tra 1 chuỗi là chuỗi con của chuỗi khác không, hoặc áp dụng với list, array)

# L6: input, output from keyboard
# input will read whole line of input
# x1, y1, z1, t1 = map(float, input('Enter 4 numbers').split())
# print(x1, y1, z1, t1)

# L7: common function in Python (sqrt, pow, floor, factorial, gcd, sum...)
# from math import *
# print(sqrt(35)) # 6.0
# print(isqrt(3)) # 1
# print(pow(2, 10))   # 1024.0
# print(ceil(2.3))
# print(ceil(6.8))
# print(factorial(5))
# print(comb(10, 2))
# print(fabs(-10.234))

# L8: If else
# if 20 < 30:
#     print('python')

# n = 101
# if n % 2 == 0:
#     print('Even')
# else :
#     print('Odd')

# a, b = 300, 200
# if a < b:
#     print(a, ' less than ', b)
# elif a == b:
#     print(a, ' equal ', b)
# else:
#     print(a, ' greater than ', b)

# a, b = 100, 200
# res = '28tech' if a > b else 'python'
# print(res)

# a = input()
# print(a, "Hello World !", "28tech C++ programming !", sep='\n')
# a = input(); print(a, end='\n')
# b = input(); print(b, end='\n')
# c = input(); print(c, end='\n')
# d = float(input()); print('%.2f' % d, end='\n')
# e = float(input()); print('%.9f' % e, end='\n')

