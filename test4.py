# def poisk(argument):
# 	return 's' in argument.lower()# Так как мы не знаем будущего списка

# def lower(f):
# 	return f.lower()

# g = ['poisk', 'google', 'microsoft', 'spaceX', 'neirolink', 'FACEBOOK', 'WHATSAPP']

# a = list(filter(poisk, g))	
# b = list(map(lower, a))
# # print(b)

# # c = list(map(lambda string:string.lower(),a))
# # print(c)

# f = list(filter(lambda a: 's' in a.lower(), g))
# print(f)

# c = list(map(lambda string:string.lower(),f))
# print(c)


# spisok = [0,1,2,3,4,5]
# if all(map(lambda x:x > 0, spisok)):
# 	print('В списке все больше нуля 1example')
# elif any(map(lambda x: x > 0, spisok)):
# 	print('В списке все больше нуля')


# Разница между ними в том, что any () возвращает True, когда хотя бы один эле­
# мент удовлетворяет условию, в то время как
# элементы удовлетворяют условию. Функция
# all()
# all()
# True, если все
# также возвратит True для
# возвращает
# пустой итерации, так как ни один элемент не является False

