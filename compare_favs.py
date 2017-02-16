kyoko_fav_foods = open('kyoko_fav_foods.txt')

kyoko_favs = kyoko_fav_foods.read()

kyoko_fav_foods.close()

sarah_fav_foods = open('sarah_fav_foods.txt')

sarah_favs = sarah_fav_foods.read()

sarah_fav_foods.close()


def compare_faves(favs1, favs2):
    if favs1 == favs2:
        return "Our favorite foods are the same!"
    else:
        return "Our favorite foods are different!"

print compare_faves(kyoko_favs, sarah_favs)
