# a = [0, 3, 5, 2, 6, 7]
# b = lambda x: x>0
# print(b(a))

# spisok = [0,1,2,3,4,5]
# if all(map(lambda x:x > 0, spisok)):
# 	print('В списке все больше нуля 1example')
# elif any(map(lambda x: x > 0, spisok)):
# 	print('В списке все больше нуля')


spisok = ['-1', '4', '6','-3', '10' ,'9','-2' ,'3', '1']
spisok = [-1, 4, 6,-3, 10 ,9,-2 ,3, 1]

# a = [x for x in spisok if x < 0] + [x for x in spisok if x >= 0]
# a = list(map(lambda x: x < 0, spisok))
apt = sorted(spisok, key=lambda x: if x < 0, reverse=True)
print(apt)
