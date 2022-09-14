class Animal:

    count= 0 #クラス変数

    def __init__(self,kind,age):
        self.kind = kind
        self.age = str(age) + '歳'
        Animal.count += 1
        

    def cry(self): #method
        print('私は'+self.kind+'です')

        
pochi = Animal("犬",5)
tama = Animal("猫",3)
# print(pochi.kind, pochi.age)
# print(tama.kind,tama.age)
# print(Animal.count)

pochi.cry()
tama.cry()

#methodと関数の違い
#methodはオブジェクトを指定して呼び出す
#methodの第一引数はselfとかく


class Dog(Animal):  #animalクラスの継承
    #追記しない場合passとかく
    def run(self):
        print('駆け回ります')


class Cat(Animal):

    def __init__(self,kind,age,color):
        super().__init__(kind,age) #親クラスのコンストラクタ
        self.color=color
#継承しつつ、独自のオブジェクトの性質を持ちたいとき

    def cry(self):
        print('にゃーん'+self.kind+'だにゃん。色は'+self.color+'だな。')

pochi = Dog('秋田犬',8)
pochi.cry()
pochi.run()
tama = Cat('三毛猫',4,'黒')
tama.cry()

