# define the menu for the hotel
menu = {
    "pizza" : 200,
    "burger" : 100,
    "pasta" : 150,
    "coffee" : 50
}

# greet
print("Welcome to our restaurant! Here's our menu" )

print(" pizza : 200 \n burger : 100 \n pasta : 150 \n coffee : 50 ")

total_order = 0

item_1 = input("enter your first item you want to order :")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else :
    print(f"ordered item {item_1} is not available yet")    


another_item = input("Do you want to order anothr item? (yes/no) ")
if another_item == "yes":
    item_2 = input("Enter your seconed item you want to order :")
    if item_2 in menu :
        total_order += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else :
        print(f"ordered item {item_2} is not available yet")  

print(f"your total order is : {total_order} ")

print("Thank you for coming.")
print("Have a nice day !")

    
