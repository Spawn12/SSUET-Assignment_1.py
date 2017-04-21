#************************************* Assignment_2 ***************************************#

#************************************ 8-3.T-Shirt ******************************************#
def make_shirt(size,message):
    print("The size of shirt is:",str(size),"\nThe text printed on shirt is:",message.title())
make_shirt(32,"Born to Fly")                      #positional argument
make_shirt(message="Guns and roses",size=28)      #keyword argument

#*********************************** 8-4. T-Shirt ***********************************#
def make_shirt(size="large",message="I Love Python"):
    print("The size of the shirt is:",str(size),"\nThe text printed on shirt is",message.title())
make_shirt()
make_shirt(size="medium")
make_shirt(size="small",message="i am to young to code")

#********************************** 8-5. Cities ************************************#
def describe_city(city,country="Pakistan"):
    print(city.title(),"is in",country.upper())
describe_city("karachi",)
describe_city("Lahore")
describe_city("london","England")

#********************************** 8-12. Sandwiches *********************************#
def func(*list):
    print("You have Ordered Sandwich with the following items in your sandwich")
    for item in list:
        print(item.title(),"is added in Sandwich")
    return "\t***********Your Sanwich is Completed***********"
print(func("Onions","Mayo","Chillie Garlic","Cheder Chesse","Steam Chicken"))
print(func("Mayo","Chillie Garlic","Mozzrela Chesse","Steam Lamp"))
print(func("Onions","Hot Peri-Peri","Cheder Chesse","Baked Beef"))

#********************************** 8-13. User Profile *******************************#
def build_profile(first,last,**my_self):
    my_profile={}
    my_profile["first_name".title()]=first
    my_profile['last_name'.title()]=last
    for key,value in my_self.items():
        my_profile[key.title()]=value
    return my_profile
profile=build_profile("Taha","Mashhadi",profession='Student',Hobby='Coding',age=20)
print(profile)

#******************************* 8-14. Cars *************************************#
#******************************** File name: Print_function.py ********************#
def make_car(manufacturer,model_name,**car):
    car_dic={}
    car_dic[manufacturer]=model_name
    for key,value in car.items():
        car_dic[key]=value
    return car_dic
#car=make_car('Toyota','Prius',color="Candy Red",sun_roof=True)
#print(car)
#********************** printing_function *********************#
def printing_func(dict):
    
    for k,v in car_dic.items():
        print("the value of",k,"is",v)
#******************************* 8-15. Printing Models *********************************#
#****************************** File name:Importing_function.py********************************#
#saving this file seprately in same folder 

#import Print_func
#import Print_func as imp
#from Print_func import make_car
#from Print_func import printing_func as p_f
#from Print_func import *

#car=Print_func.make_car('Toyota','Prius',color="Candy Red",sun_roof=True)
#print(car)

#car=imp.make_car('Toyota','Prius',color="Candy Red",sun_roof=True)
#print(car)

#car=Print_func.p_f('Toyota','Prius',color="Candy Red",sun_roof=True)
#print(car)


#********************************** Problem Euler 3 ***********************************#
def most_common_prime_factor(list):
    dict = {}
    for x in range(0,len(list)):
        count = 1
        if list[x] in dict:
            count = count + dict[list[x]]
        dict[list[x]] = count
    for val in dict.values():
        if val>1:
            return max(dict, key=dict.get)
        else :
            return "Null"

def list_of_prime_factor(no):
    num=no
    list=[]
    for x in range(2,num+1):
        while (num % x == 0):
            num = num / x
            list.append(x)
        if num==1:
            break
    print("The List Prime Factors Of ",no,"is :",list,"\nThe Largest Prime Factors is :",max(list))
    return most_common_prime_factor(list)

no=int(input("Enter no for finding largest prime factor :"))
print ("The most common Prime Factors Of ",no,"is",list_of_prime_factor(no))
