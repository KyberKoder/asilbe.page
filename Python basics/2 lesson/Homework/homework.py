son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
belgi = input("kopaytiramizmi bulamzmi, ayiramizmi yoki qoshamiz belgisini kiriting: ")

if belgi == "+":
    natija = son1 + son2
elif belgi == "-":
    natija = son1 - son2
elif belgi == "*":
    natija = son1 * son2
elif belgi == "/":
    natija = son1 / son2
else:
    natija = "belgi xato kiritildi:"

print(f"Natija: {natija}")
