
son = 0
n = int(input("Nechta raqam kiritimoqchisiz?: "))
for sons in range(1, n+1):
    user_num = float(input(f"{sons}-raqamni kiriting: "))
    son+=user_num

print(f"Natija: {son}")