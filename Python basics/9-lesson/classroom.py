# def davlatlar():
#     return {
#     'uzbekistan': 'toshkent',
#     'russia': 'moskva',
#     'usa': 'washington',
#     'japan': 'tokyo',
#     'germany': 'berlin',
#     'turkey': 'ankara',
#     'france': 'paris',
#     'china': 'beijing',
#     'india': 'delhi',
#     'italy': 'rome'
# }

# print("\nDavlatlar alifbo tartibida:")
# for davlat in sorted(davlatlar()):
#     print(davlat.title())

# print("\nPoytaxtlar alifbo tartibida:")
# for poytaxt in sorted(davlatlar().values()):
#     print(poytaxt.title())

def func_nomi(t_yil, h_yil=2025):
    yosh = h_yil - t_yil
    v_yetgan = False
    if yosh >= 18:
        v_yetgan = True
    return dict(yosh=yosh, voyaga_yetgan=v_yetgan)
print(func_nomi(t_yil=2009, h_yil=2000))
print(func_nomi(t_yil=2003, h_yil=2015))
print(func_nomi(t_yil=2005))
    