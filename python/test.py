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
L = ["Bert", "Lisa", "Adam"]
x = 0
while x < len(L):
    print("Hello ", L[x])
    x = x+1