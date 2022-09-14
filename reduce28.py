from functools import reduce

result = reduce(lambda x,y: x*y, [1,2,3,4,5])
print(result)

#reduce関数の返り値は整数