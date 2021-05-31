"""
Define class FoodItem
The below Python program accepts the name and the price of N food items as the input. The program sorts the food items based on the price in ascending order. If two or more food items have the same price, then the program must sort those food items in the order of their occurrence. Finally, the program prints the name and the price of the N sorted food items as shown in the Example Input/Output section.Please define the class FoodItem so that the program runs successfully.

Example Input/Output 1:
Input:
5
Chapati 50
GobiManchurian 100
Idly 20
ChilliParotta 80
OnionDosa 45

Output:
Idly:20
OnionDosa:45
Chapati:50
ChilliParotta:80
GobiManchurian:100

Example Input/Output 2:
Input:
7
PaneerTikka 170
Salad 90
Pizza 350
GheeRoast 100
EggPasta 90
FrenchFries 90
ChickenNoodles 125

Output:
Salad:90
EggPasta:90
FrenchFries:90
GheeRoast:100
ChickenNoodles:125
PaneerTikka:170
Pizza:350


"""
#Solution

class FoodItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __repr__(self):
        return str(self.name)+":"+str(self.price)
    def __lt__(self,other):
        return self.price<other.price
N = int(input())
foodItems = []
for ctr in range(N):
    name, price = input().strip().split()
    foodItems.append(FoodItem(name, int(price)))
foodItems.sort()
for food in foodItems:
    print(food)
    
 




#more examples

class FoodItem: 
    def __init__(self,a,b): 
        self.a = a 
        self.b = b 
    def __gt__(self,obj): return self.b > obj.b
    def __lt__(self,obj): return self.b < obj.b 
    def __ge__(self,obj): return self.b >= obj.b 
    def __le__(self,obj): return self.b <= obj.b
    def __eq__(self,obj): return self.b == obj.b
    def __repr__(self): return str((self.a + ':' + str(self.b)))
    

