# uyga vazifa

# 1. inputga 20 ta misol
# 2.  kalkulyatorga 5ta amalga misol ishlash
# 3. 61- betgacha o`qish (majburiy)
# 4. 90gacha (kayfiyatga qarab)

# ism = input("Ismingizni kiriting: ")
# print(f"salom {ism}")

# son = float(input("yilingizni kiriting: "))

# shahar = input("Shahringizni kiriting: ")
# print(shahar)

# son1 = float(input("1-sonni k: "))
# son2 = float(input("2-sonni k: "))
# print(f"ayirma {son1-son2}")

# ismlar = ["ali", "ali", "vali", "Oysha", "Sobir", "obid", ['olim', 'ali', 'ali']]
# # print(ismlar[2])
# # print(ismlar[1:])
# # ismlar2 = ismlar.copy()
# # ismlar.clear()
# ismlar.append("Setora")
# ismlar.extend([1,2,3])
# ismlar.remove("ali")
# ismlar.sort(reverse=True)
# print(ismlar)
# print(len(ismlar))

#DATA TYPES
# int 120, -4, 0
# float 12.0, -7.6, 100.90943
# str "3", "120", "Ali", "[1,m2,3,4]"
# list [12,34,34,12,12,12,"ALi"]
# tuples (123, 458)
# my_tuple = (12,34,5,7)
# print(type(my_tuple))
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))
# my_list.append("New el")
# my_tuple = tuple(my_list)
# print(my_tuple)

# LOOP (SIKL)
# for loopi
my_list = [12,34,34,12,12,12,"ALi"]
my_list2 = [1,2,3,4,5,6,7,8,9]
my_list3 = list(range(1, 100))
# print(my_list2)
# print(my_list3)
# for num in range(120, 100, -5): #0 dan boshlab, 100 gacha 100 kirmaydi!
#     # 120 boshlanish nuqta, 100 oxirgi nuqta, -5 qadam
#     print(num)
juft_son_yig = 0
# juft_son_yig = 2
# juft_son_yig = 6
# juft_son_yig = 12
# juft_son_yig = 20 
# juft_son_yig = 30
# juft_son_yig = 42
for juft_son in range(2, 21, 2):
    juft_son_yig+=juft_son
    print(f"yig'indining hozirgi holat: {juft_son_yig}")
    # juft_son_yig+=10
    # juft_son_yig = juft_son_yig + juft_son
    # print(juft_son)
# print(juft_son_yig)