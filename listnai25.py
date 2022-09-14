nums= [i for i in range(10)]
print(nums)

nums2=[i*i for i in range(10)]
print(nums2)

nums3=[i for i in range(10) if i %2 == 0]
print(nums3)

nums4=[i if i %2 == 0 else i*i for i in range(10)]
print(nums4)

#リスト内包表記　短く、早くリストの初期化ができる

nums5=[i*j for i in range(10) for j in range(10)]
print(nums5)