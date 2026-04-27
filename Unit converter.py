
# first machine banayenge def ka use karke
def km_to_miles(km):
    return km * 0.621
def kg_to_pounds(kg):
    return kg * 2.205
def clescius_to_farenheit (celscius):
    return (celscius * 9/5) +32

# ab input lenge user se ke kitne karna hai

print("Welcome to the unit converter!^_^")
print("1.Kilometer to miles")
print("2.Kilograms to pounds")
print ("3.celscius to farenheit")

# ab yaha bhi user coose karega 1/2/3
choice =int(input("enter you choice 1/2/3:"))

# yaha pe km use ka enter km hoga fir machinee run karke mile shoga
if choice == 1:
    km=float(input("enter Km: "))
    print ("Miles:",km_to_miles(km))
elif choice == 2:
    kg=float(input("enter kg:"))
    print("pounds:",kg_to_pounds(kg))
elif choice == 3:
    celscius=float(input("enter celscius:"))
    print("farenheit:",clescius_to_farenheit(celscius))
else:
    print("invalid choice choose form the 1/2/3 only")

