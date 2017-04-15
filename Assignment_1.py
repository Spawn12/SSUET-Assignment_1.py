##3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
#Make a list that includes at least three people you’d like to invite to dinner . Then use your list to print a message to each person, inviting them to dinner
guest_list=["Ayesha",'Alex',"Kamran"] 
for x in guest_list:
    print(x,"I invite u on dinner at 9:00 clock")

##3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations .
#You’ll have to think of someone else to invite .
print(guest_list[0],"can't come at dinner")
guest_list[guest_list.index("Ayesha")]="Amna"
for x in guest_list:
    print(x,"I invite u on dinner at 9:00 clock")

##3-6. More Guests: You just found a bigger dinner table so now more space is available . Think of three more guests to invite to dinner .
for x in guest_list:
    print(x,"I found a bigger dinner table at resturant")
guest_list.insert(0,"Usman")
guest_list.insert(2,"Mark")
guest_list.append("Elen")
for x in guest_list:
    print(x,"I invite u on dinner at 9:00 clock")

##3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests .
print("I can only invite 2 peoples")
for x in range(2,len(guest_list)):
    print("Sorry ",guest_list.pop(),"you are Not-Invited because of seat shortage....")
for x in guest_list:
    print(x,"I invite u on dinner at 9:00 clock")
for x in range(0,len(guest_list)):
    del guest_list[0]
print(guest_list)

##3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
#use len() to print a message indicating the number of people you are inviting to dinner .
print("No of guest coming in dinner :",len(guest_list))

##3-8. Seeing the World: Think of at least five places in the world you’d like to visit .
list_to_visit=["Prague","Iceland","London","Spain","Paris"]
print(list_to_visit)
sorted_list_to_visit=sorted(list_to_visit)
print(sorted_list_to_visit)
print(list_to_visit)
reverse_sorted_list_to_visit=sorted(list_to_visit,reverse=True)
print(reverse_sorted_list_to_visit)
print(list_to_visit)
list_to_visit.reverse()
print(list_to_visit)
list_to_visit.reverse()
print(list_to_visit)
list_to_visit.sort()
print(list_to_visit)
list_to_visit.sort(key=None,reverse=True)
print(list_to_visit)

##3-10. Every Function: Think of something you could store in a list . For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like .
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once .
x=["cat",2.5,500,True]
print(x)
x[1]="dog" # changing first element of x from 2.5 to dog
print(x)

bike=["honda","yamaha","suzuki"]
del bike[1] #deleting the value at index 1 from x
print(bike)

x=["cat",2.5,500,True]
x.insert(1,"dog")#its insert the element in given position
print(x)

x.append(False)#it will append the element at last
print(x)

y=x.pop(2)#it will pop that element out at given index and remove from that list If no index is specified , list.pop() removes the last item in the list
print(y+1)#you can also play with that pop out no
print("pop",x)

x.remove(False)#it will remove the given elment from the list
print(x)

list_one = [1, 2, 3, 4, 5, 6, 7]  # This is the first list
list_two = [10, 12, 14]           # This is the second list
list_one.extend(list_two)         # Extend list_one by appending all items of list_two
print(list_one)

my_list = [2, 3, 5, 7, 11, 13] # Create a list
my_list.clear()                # Remove all the items from the list
print(my_list) 

my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]# Create a list
my_index = my_list.index("is")                                # Return the index of the first "is"
print("The item was first found at index:", my_index)

my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)

my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

my_list.sort(reverse=True)                             #it will sort list in descending order
print(my_list)

my_list.sort()                             #it will sort list in ascending order
print(my_list)

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.        
print("Copied list looks like:", copied_list)

my_list = ['two', 5, ['one', 2]]
print(len(my_list))


my_list = [5, 3, 6, 1, 2, 4, 7]                  # Create a list
sorted(my_list, reverse=True)             # Sorted the items of the list in sort the item permenantlyorder
print("Sorted list looks like:", my_list)

my_list=['a','g','d','f','t','x','l']
my_list.sort()
print(my_list)

##3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen .
#Change an index in one of your programs to produce an index error . Make sure you correct the error before closing the program .
#list=[65,"alex",'dog']
print ("Intentional Error calling for del element at -4 which is out of range hehehehehe........")
#del list[-4]


##4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
my_list=[24 ,'car', 'tv', 5.3, 'apple', 36]
for x in range(0,3):
    print(my_list[x],"is present at",x,"index")
for x in my_list[:3]:
    print(x,"is present at",my_list.index(x),"index")
for x in my_list[-3:]:
    print(x,"is present at",my_list.index(x),"index")
print("Mid 3 element of my list are ",my_list[int(len(my_list)/2-1.5):int(len(my_list)/2+1.5)])

#4.10 . My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60) . Make a copy of the list of pizzas, and call it friend_pizzas .
#Then, do the following:
##4.11 Including for loops
my_favourite_cars=["Honda","Nisan",'BMW']
my_friend_favourite_cars=my_favourite_cars[:]
my_favourite_cars.insert(0,"Audi")
my_friend_favourite_cars.append("Lamborghini")
print(my_favourite_cars)
print(my_friend_favourite_cars)
x=1
for cars in my_favourite_cars:
    print("My",x,"favorite car is",cars)
    x=x+1
x=1
for cars in my_friend_favourite_cars:
    print("My friend",x,"favorite car is",cars)
    x=x+1

##4.11 Including for loops
my_favourite_cars=["Honda","Nisan",'BMW']
x=1
for cars in my_favourite_cars:
    print("My",x,"favorite car is",cars)
    x=x+1
##4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods, and store them in a tuple
food_in_menu=("Spaheghitit","Biryani","Fried Rice","Macroni","Pizza")
for food in food_in_menu:
    print("We have",food,"in buffet")
#food_in_menu[1]="Nihari" ## Intentional Error
food_in_menu=("Spaheghitit","Sajji","Biryani","Fried Rice","Tikka")
for food in food_in_menu:
    print("We have",food,"in menu")
#**************************** Fibonacia Series ******************************#
