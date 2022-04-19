import time
def menu():
    print(" Main Menu\n")
    print(" 1. Minimum number of rupee  by Greedy Algorithm\n")
    print(" 0. Exit\n")
def greedy(amount):
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var8 = 0
    var9 = 0
    var10 =0
    while(amount != 0):
        if(amount>=2000):
            amount = amount-2000
            var1 = var1+1

5
  elif(amount>=500):
        amount = amount-500
        var2 = var2+1
        elif(amount>=200):
        amount = amount-200
        var3 = var3+1 
        elif(amount>=100):
        amount = amount-100
        var4 = var4+1
        elif(amount>=50):
         amount=amount-50
         var5=var5+1
        elif(amount>=20):
               amount=amount-20
         var6=var6+1
        elif(amount>=10):
              amount=amount-10
              var7=var7+1
        elif(amount>=5):
              amount=amount-5
              var8=var8+1
        elif(amount>=2):
          

6
              amount=amount-2
        var9=var9+1
        else:
        amount=amount-1            
        var10=var10+1
   print(" Indian rupee 2000 :",var1)
   print(" Indian rupee 500 :",var2)
   print(" Indian rupee 200 :",var3)
   print(" Indian rupee 100 :",var4)
   print(" Indian rupee 50 :",var5)
   print(" Indian rupee 20 :",var6)
   print(" Indian rupee 10 :",var7)
   print("Indian rupee 5:",var8)
   print("Indian rupee 2:",var9)
   print("Indian rupee 1:",var10)
   if _name_ == "_main_":
    menu()
    val = input(" Enter your choice: ")
    while val != '0':
        rupee= input("Enter your Indian rupee amount : ")
        change = int(rupee)
        if val=='1':
        begin = time.perf_counter()
        greedy(change)
        end = time.perf_counter()
        print(" Time execution : ",end-begin)
        menu()
        val = input(" Enter your choice: ")
        print(“exiting program”)















