FACTOR = 0.62

print("Hello. This is converter from kilometers to miles")

while True:
    km = int(input("Enter km: "))
    miles = km * FACTOR
    print(miles)

    more = input("You want more? (yes/no): ")
    if more !="yes":
        break
print("Thank you, goodbye.")
