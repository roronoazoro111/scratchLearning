#test print
# print("hei", "你好");

# enter string
# name = input("please enter your name:");
# print("Hello, ", name);

# print absolute value of an integer
# a = 100
# if a>=0:
#     print(a)
# else:
#     print(-a)

# s1 = 72
# s2 = 85
# print('提升了 {0:.1f}%'.format((s2-s1)/s1)) #取小数点后一位数


# BMI公式 （体重除以身高的平方）
# height = 1.75
# weight = 80.5
# bmi = weight/(height**2)
# if bmi < 18.5:
#     print("过轻", bmi)
# elif bmi >= 18.5 and bmi < 25:
#     print("正常", bmi)
# elif bmi >=25 and bmi < 28:
#     print("过重", bmi)
# elif bmi >= 28 and bmi < 32:
#     print("肥胖", bmi)
# else:
#     print("严重肥胖", bmi)


# for 循环
# sum = 0
# for x in range(101):# range生成的是0-100的序列
#     sum += x
# print(sum)

# while 循环
# L = ["Bert", "Lisa", "Adam"]
# x = 0
# while x < len(L):
#     print("Hello ", L[x])
#     x = x+1

# continue
# x = 0
# while x < 100:
#     x = x+1
#     if x % 2 == 0:
#         continue
#     print(x)

# dict & set
# a = (1, 2, 3) # (1, [2, 3])
# b = set(a)
# print(a, b)
    
# define function
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError("bad operand type")
#     if(x >= 0):
#         return x
#     else:
#         return -x

# import math
# def quadratic(a, b, c):
#     # if (a, b, c) not isinstance(int, float):
#     #     raise TypeError("bad ")
#     # else:
#         sq = math.sqrt(b*b-4*a*c)# 注意sqrt中的值不能为负数
#         return round((-b+sq)/(2.0*a), 2) , round((-b-sq)/(2.0*a), 2) 
    
# *numbers表示把numbers这个list的所有元素作为可变参数传进去
# def calc(*numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x**2
#     return sum
# arr = [1, 2, 4]
# print(calc(*arr))
# 若定义calc函数参数不带*，则直接传入list或tuple [1, 2, 4] | (1, 2, 4)