import ex_class
class Addition():

    def __init__(self,num1,num2,num3):
        self.nummber1=num1
        self.nummber2=num2
        self.nummber3=num3
    def sum(self):
        sum=self.nummber1+self.nummber2+self.nummber3
        return sum
    def max_val(self):
        max_value=max(self.nummber1,self.nummber2,self.nummber3)
        return max_value

addition=Addition(34,56,89)
total_sum=addition.sum()
print(total_sum)
max_value=addition.max_val()
print(max_value)
num1=int(input("num1= "))
num2=int(input("num2= "))
num3=int(input("num3= "))
addition=Addition(num1,num2,num3)
total_sum=addition.sum()
print(total_sum)