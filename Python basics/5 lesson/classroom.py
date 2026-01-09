# a = 7
# b = 7
# if a >=b:
#     print("A")
# else:
#     print("B")


# # AND , OR , NOT operatorlari

# # and -----> va
# # or ------> yoki 
# # not -----> emas

# yosh = 40
# print(yosh !=7)

# if not(yosh <= 7 or yosh > 65):
#     print("Bepul")
# else:
#     print("Pullik")

# numbers = []
# for number in range(1, 11):
#     numbers.append(number)
# print(numbers)

# # a = 5
# # 12345
# # b = 3
# # 123

# n = int(input("Raqam kiriting: "))

# for n in range(1, n+1):
#     print(f"{n}")

# n = 5
# while n > 0:
#     print(f"{n}")

# ismlar = ["Ali","Vali","Bek","Xon","Oysha"]
# for ism in ismlar[1:4]:
#     print(f"Assalomu alaykum {ism}")

# a = 5
# b = 0
# for a in range()


import random
kom_num = random.randint(1, 10)
print(kom_num)
n = 1
while n < 6:
    user_guess = int(input(f"{n}-taxmin raqamni kiriting: "))
    if user_guess == kom_num:
        print(f"{n}-urinishda topdingiz va {(6-n)*10} ball oldingiz!")
        print("Siz yutdingiz!!!")
        break
    n+=1