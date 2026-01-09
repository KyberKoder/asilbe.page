fanlar = {}

jami_ball = 0
i = 1

while i <= 10:
    fan = input(f"{i}-fan nomini kiriting: ")
    ball = float(input(f"{fan} fanidan olgan bahongizni kiriting: "))

    fanlar[fan] = ball
    jami_ball += ball

    i += 1

ortacha_ball = jami_ball / 10
fanlar["o'rtacha ball"] = ortacha_ball

print("\nNatija:")
print(fanlar)
