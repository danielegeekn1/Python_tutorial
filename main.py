i = 0
while i <= 10:
    i = i + 1
    print(i)

anime = ['Demon Slayer', 'One Piece', 'Naruto', 'Dragon Ball']
for ani in anime:
    print(ani)
for index in range(len(anime)):
    print(index)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 2))