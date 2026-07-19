n = int(input("Enter Total Rupees : "))
nperson = int(input("Enter Total Member : "))

modd = n % nperson
div = n // nperson
print(f"Each Pays : {div} | Piggy Bank Gets : {modd}")
# print(div)
# print(modd)
