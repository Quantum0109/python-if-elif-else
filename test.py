shop_bread = 100
user_bread = input("Сколько хлеба надо купить")   # во 2 строке получается str его нельзя сравнить с int
if int(user_bread) <= shop_bread:
	print("Хорошо")
    
else: 
	remainder = user_bread - shop_bread  # считаем сколько хлеба не хватило в
	print("В магазине не хватилоим", remainder, "хлеба")
