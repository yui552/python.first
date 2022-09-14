nums = map(int,['1','2','3']) 
#第一引数の関数を第二引数の要素すべてに実行する
for num in nums:
    print(num)

def is_even(num):
    return num % 2  == 0 

print(is_even(2))
print(is_even(5))

nums = map(int,['1','2','3']) 
even_nums = filter(lambda x: x % 2 == 0,nums)
#第一引数の関数実行時にtrueのものだけ
#取り出す
#lambaは関数に名前を付けない、他でその関数を使わないとき
print(list(even_nums))
#iterableなobjectはlist関数でリスト型に変更