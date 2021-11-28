import menu
menu.menu()
menu.order()
option=int(input("enter the option"))

while option != 0:
  if option == 1:
    print("ordered Burger")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} burger is {menu.burger(q)}")
  elif option ==2:
    print("Ordered Pizza")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} pizza is {menu.pizza(q)}")
  elif option ==3:
    print("Ordered biriyani")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} biriyani is {menu.biriyani(q)}")
  elif option ==4:
    print("Ordered alpham")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} alpham is {menu.alpham(q)}")
  elif option ==5:
    print("Ordered mandhi")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} mandhi is {menu.mandhi(q)}")
  elif option ==6:
    print("Ordered shawarma")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} shawarma is {menu.shawarma(q)}")
  elif option ==7:
    print("Ordered muthubak")
    q=int(input("enter the quantity :"))
    print(f"cost for {q} muthubak is {menu.muthubak(q)}")  
  else:
    print("Invalid Option")
  menu.order()
  option=int(input("enter the option"))

print("Thanks for using the program")
print("Total cost = ",menu.totalcost())
