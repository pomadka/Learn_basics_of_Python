apartmentsPrice = input("Please enter apartments price: ")
print("You entered " + str(apartmentsPrice))

apartmentsArea = input("Please enter apartments area: ")
print("You entered " + str(apartmentsArea))

squareMetre = apartmentsPrice / apartmentsArea
output = "Cost per square metre is %.2f"
print (output % squareMetre)
