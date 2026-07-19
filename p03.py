n = input("Enter Password To Check : ")
score = 0
dig = False
upper = False
lower = False
sp = False
special = "@$#%"

if len(n) > 8:
    score = score + 1
for ch in n:
    if ch.isupper():
        upper = True
    if ch.islower():
        lower = True
    if ch.isdigit():
        dig = True
        break
    if ch in special:
        sp = True
    
if upper == True and lower == True:
    score = score + 1
if dig == True:
    score = score + 1
if sp == True:
    score = score + 1
    
    
if score <= 1:
    print(f"week ! {score}/4")
elif score <= 2:
    print(f"Good ! {score}/4")
elif score <= 3:
    print(f"fStrong! {score}/4")
else:
    print(f"Excellense! {score}/4")
    






    