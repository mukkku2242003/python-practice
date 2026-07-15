# class student:
#        def __init__(self,fullname,marks):
#         self.name=fullname    
#         self.marks=marks
#         print("adding new student in data basse ")
# s1=student("mukesh",97)
# print(s1.name,s1.marks)
# print(s1.marks)
# s2=student("vijay",88)
# print(s2.name)
# print(s2.marks)


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_ave(self):
#         sum = 0
#         for val in self.marks:
#          sum+= val
#         print("hii",self.name , "your averge score is ",sum/3
#               )

# s1 = student("mukesh",[99.76,45])
# s1.get_ave()



# class mobile:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def show_mobile(self):
#         print("brand",self.name)
#         print("color",self.color)
# m1=mobile("samsung","blue")
# m1.show_mobile()
        

# class employee:
#     def __init__(self,name,sallary,department):
#         self.name=name
#         self.sallary=sallary
#         self.department=department

#     def employee_details(self):
#         print("name",self.name)
#         print("sallary",self.sallary)
#         print("department",self.department)

# s1=employee("mukesh kumar",50000,"aiml engnieer")
# s1.employee_details()

# class Car:
#     def __init__(self, brand, model, price):
#         # yaha attributes set karo
#         self.brand=brand
#         self.model=model
#         self.price=price


#     def car_details(self):
#         # yaha print karo
#         print("brnad",self.brand)
#         print("model",self.model)
#         print("price",self.price)
# c1 = Car("Toyota", "Fortuner", 4500000)
# c1.car_details()        

# class student:
#     def __init__(self,student_name,math_marks,computer_marks,english_marks):
#         self.student_name=student_name
#         self.math_marks=math_marks
#         self.english_marks=english_marks
#         self.computer_marks=computer_marks
#     def student_result(self):
#         total_marks=(self.english_marks + self.math_marks + self.computer_marks)
#         percentage=(total_marks/3)
#         print("student_name",self.student_name)
#         print("math_marks",self.math_marks)
#         print("english marks",self.english_marks)
#         print("computer marks",self.computer_marks)
#         print("total marks",total_marks)
#         print("percentage",percentage)
    
# s1=student("mukesh kumar", 47, 97, 88,)
# s1.student_result()



# class wallet:
#     def __init__(self,balance):
#        self.balance=balance
#     def add_money(self,amount):
#         print("balance",self.balance + amount)
# s1=wallet(5000  )   
# s1.add_money(3000)              





# class car:
#     color="blue"
#     brand="marcades"
# car1=car()
# print(car1.color)
# print(car1.brand)

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def add_grace(self,grace):
#         self.marks=self.marks + grace
#         print("name",self.name)
#         print("marks", self.marks ) 
# s1=student("mukesh kumar", 400)
# s1.add_grace(30)


# class BankAccount:
#     def __init__(self,name ,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#      self.balance=self.balance + amount
#      print("deposite amount",amount)
#      print("balance",self.balance)
     
#     def withdraw(self,amount):
#       if  amount<=self.balance:
#        self.balance=self.balance - amount
#        print("widraw ",amount)
#        print("remaning balance",self.balance)
#        print("name ",self.name)     
#       else:
#             print("balance is infucelent")
            
               
# s1=BankAccount("rohit sexena",10000)
# s1.deposite(3000)
# s1.withdraw(5000)
# s1.withdraw(2000)
# s1.withdraw(6000)


# class employee:
#     def __init__(self,name):
#         self.name=name
#     def show_name(self):
#         print("name",self.name)

# class manager(employee):
#     def aprove(self):
#         print("leave approved")
# m1=manager("rahul")
# m1.show_name()
# m1.aprove()       
        
# print("hello rohit")    

# class person():
#     def __init__(self,name):
#         self.name = name 

#     def show_name(self):
#         print("name ",self.name)

# class student(person):
#     def study(self):
#         print("studen of the year")

# s1=student("mukesh kumar")
# s1.show_name()
# s1.study()


        
    
# class person():
#     def __init__(self,name ,age):
#         self.name=name
#         self.age=age
#     def shown_person(self):
#         print("name",self.name )
#         print("age",self.age)

# class employee(person):
#     def __init__(self,name,age ,salary):
#         super().__init__(name, age)
#         self.salary=salary
#     def show_salary(self):
           
#         print("salary" ,self.salary)

# s1=employee("mukesh kumar ",24,20000)
# s1.shown_person()
# s1.show_salary()



# class vehicle():
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def show_vehicle(self):
#         print("brand", self.brand)
#         print("model",self.model)
# class car(vehicle):
#     def __init__(self,brand,model,price):
#         super().__init__(brand,model)
#         self.price=price
#     def show_price(self):
#         print("price",self.price)
# s1=car("tyota","ertiga 2023 model",123000)
# s1.show_price()
# s1.show_vehicle()

# class animal:
#     def sound(self):
#         print("animal make sound ")

# class dog(animal):
#     def sound(self):
#         super().sound()
#         print("dogs bark")

# d1=dog()
# d1.sound()

# class employee:
#     def __init__(self,name,__salary):
#      self.name=name
#      self.__salary=__salary
#     def show_details(self):
#        print("name",self.name)
#        print("salary",self.__salary)
# s1=employee("mukesh kumar",35000)
# s1.show_details()



# class employee:
#     def __init__(self,name ,salary ):
#         self.name = name 
#         self.__salary=salary
#     def show_detail(self):
#         print("name ",self.name)
#         print("salary",self.__salary)
#     def update_salary(self,new_salary):
#         if new_salary > 0:
#             self.__salary=new_salary
#             print("salary update")
#         else:
#             new_salary<0

#             print("invalid sallary ")
# e1=employee("mukesh kumar ",3000)
# e1.show_detail()
# e1.update_salary(7000)
# e1.show_detail()
# e1.update_salary(-100000)
# e1.show_detail()


# class bike :
#     def start(self):
#         print("bike statr with kick ")
# class car:
#     def start(self):
#         print("car start with  key ")
# vehicles=[car(),bike()]
# for vehicle in vehicles:

#  vehicle.start()

# b1=bike()
# c1=car()

# b1.start()
# c1.start()
# class cash_payment:
#     def pay(self):
#         print("Payment by Cash")

# class upi_payment:
#     def pay(self):
#         print("Payment by UPI")
# payment=[cash_payment(),upi_payment()]
# for payments in payment:
#  payments.pay()

# class email_notification:
#     def send(self):
#         print("email send")
# class sms_notification:
#     def send(self):
#         print("send sms")
# notifications=[email_notification(),sms_notification()]
# for notification in notifications:
#   notification.send()


from abc import ABC ,abstractmethod


class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class upi_payments(payment):
    def pay(self):
        print("pay form upi payments")
class cash_payment(payment):
    def pay(self):
        print("pay from cash payments")
u1=upi_payments()
c1=cash_payment()
u1.pay()
c1.pay()
