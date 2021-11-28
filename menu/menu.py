dish={"Burger":50,"Pizza":100,"Biriyani":180,"Alpham":420,"Mandhi":600,"Shawarma":90,"Muthubak":80}
total=0

def totalcost():
    return total

def cost(c):
  global total
  total=total+c
  #print(total)

def menu():
    print("_"*26)
    print("|"," "*8,"Menu"," "*8,"|")
    print("_"*26)
    print("| 1.Burger         | 50  |")
    print("_"*26)
    print("| 2.Pizza          | 100 |")
    print("_"*26)
    print("| 3.Biriyani       |180  |")
    print("_"*26)
    print("| 4.Alpham         |420  |")
    print("_"*26)
    print("| 5.Mandhi         |600  |")
    print("_"*26)
    print("| 6.Shawarma       |90   |")
    print("_"*26)
    print("| 7.Muthubak       |80   |")
    print("_"*26)

def order():
  print("\n") 
  print("[1] Burger")
  print("[2] Pizza")
  print("[3] Biriyani")
  print("[4] Alpham")
  print("[5] Mandhi")
  print("[6] Shawarma")
  print("[7] Muthubak")  
  print("[0] Exit")

def burger(q):
  print("Burger Function")
  cost(dish.get("Burger")*q)
  return(dish.get("Burger")*q)
  
def pizza(q):
  print("Pizza Function")
  cost(dish.get("Pizza")*q)
  return(dish.get("Pizza")*q)
  
def biriyani(q):
  print("Biriyani Function")
  cost(dish.get("Biriyani")*q)
  return(dish.get("Biriyani")*q)

def alpham(q):
  print("Alpham Function")
  cost(dish.get("Alpham")*q)
  return(dish.get("Alpham")*q)

def mandhi(q):
  print("Mandhi Function")
  cost(dish.get("Mandhi")*q)
  return(dish.get("Mandhi")*q)

def shawarma(q):
  print("Shawarma Function")
  cost(dish.get("Shawarma")*q)
  return(dish.get("Shawarma")*q)

def muthubak(q):
  print("Muthubak Function")
  cost(dish.get("Muthubak")*q)
  return(dish.get("Muthubak")*q)
