word = input().upper()
word_list = list(set(word))

countarr = []

for i in word_list:
    countarr.append(word.count(i))
    
if countarr.count(max(countarr)) > 1:
    print("?")
else:
    print(word_list[countarr.index(max(countarr))])
