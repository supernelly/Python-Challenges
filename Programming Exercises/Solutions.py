class Question1():
    def __init__(self):
        a = []
        for i in range(2000, 3201):
            if (i % 7 == 0) and (i % 5 != 0):
                a.append(str(i))
        print(','.join(a))

class Question2():
    def __init__(self, num):
        print(self.factorial(num))
        
    def factorial(self, num):
        if num == 0: 
            return 1
        else: 
            return num * self.factorial(num - 1)
            
class Question3():
    def __init__(self):
        a=1
# Test
#Question1()
#Question2(6) # Positive Integer
#Question3()
#Question4()
#Question5()
#Question6()
#Question7()
#Question8()
#Question9()
#Question10()
#Question11()