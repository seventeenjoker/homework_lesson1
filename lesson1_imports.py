from collections import Counter

phones = ['iphone', 'samsung', 'lg', 'smthelse', 'iphone']

count = Counter(phones)
print(count)

text = 'Ехыл Грека через реку видит Грека в реке рак'
count2 = Counter(text.lower().replace(' ', ''))
print(count2)