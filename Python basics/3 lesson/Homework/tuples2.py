ismlar = ('Asilbek', 'Ozodbek', 'Shahzod', 'Odiljon', 'Bekmirza')
ismlar = list(ismlar)
ismlar.append('Murtazo')
ismlar.remove('Ozodbek')
ismlar[1] = 'Muhammadjon'
ismlar = tuple(ismlar)
print(ismlar)