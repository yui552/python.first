seasons= ['Spring','Summer','Fall','Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))

english= 'English'
for (i,c) in enumerate(english):
 print(i,c)

dic={'a':1, 'b':2} #キーが数えられる
for(i,k)in enumerate(dic):
    print(i,k)

prices=[100,200,300,400]
quantities=[1,2,3]
for (price,quantity) in zip(prices,quantities):
 print(price*quantity)

menu=['coffee','tea','cake']
for(item,price,quantity)in zip(menu,prices,quantities):
    print(item,price*quantity)

 #zipは二つのオブジェクトから同時に一つずつ取り出す、要素数が少ないものに合わせて止まる


