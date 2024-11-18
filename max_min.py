ma_liste = [2, 1, 5, 4, 3]
max_num = max(ma_liste)
min_num = min(ma_liste)
print(f"Max: {max_num}\nMin: {min_num}")
print(ma_liste)
ma_liste.sort()
nouv_liste = ma_liste
print(f"Max: {nouv_liste[4]}\nMin: {nouv_liste[0]}")
print(ma_liste)