tomato_big = 1000
tomato_medium = 500
tomato_small = 100
tomato_user = int(input("Сколько весит помидор? "))

if tomato_user < 100:
	print("Не подходит, слишком маленький помидор")
elif tomato_user >= tomato_small and tomato_user < tomato_medium:
	print("Это маленький помидор")
elif tomato_user >= tomato_medium and tomato_user < tomato_big:
		print("Это средний помидор")
else: 
	print("Это большой помидор")