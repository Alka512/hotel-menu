menu={
    "water":20,
    "roti":30,
    "daal":40,
    "rice":50,
    "shahi paneer":120,
    "spring roll":60

};
#greet
print("WELCOME TO ANYA RESTAURANT")
print("water: Rs20\nroti: Rs30\ndaal: Rs40\nrice: Rs50\nshahi paneer: Rs120\nspring roll: Rs60")

order_total=0
first_item=input("enter the name of item you want to order:")
if first_item in menu:
    order_total += menu [first_item]
    print(f"item {first_item} added to your order")
else:
    print(f"the{first_item} is not available yet!")

another_order=input("do you want to order another item ? (yes/no)")
if another_order =="yes":
    second_item=input("enter the name of second item:")
    order_total += menu[second_item]
    if second_item in menu:
        print(f"item {second_item} is added to your order")
    else:
        print(f"the{second_item}is not available yet!")
print(f"the amount of your order to pay:{order_total}")
