n = input("Enter Full Name : ").split()
cname = input("Enter Company Name : ")
name = n[0]
mname = n[1]
sname = n[2]
# print(name.capitalize())
# print(sname.capitalize())
length = len(n)
print(name[0].capitalize(),end=" ")
print(mname[0].capitalize(),end=" ")
print(sname.capitalize(),end=" ")
print(cname.capitalize(),end=" ")
print()
full = f"{name[0].capitalize()} . {mname[0].capitalize()} . {sname.capitalize()} "
c = f"{cname.capitalize()}.Intern"
for i in range(10):
    for j in range(30):
        if i == 0 or i == 9 or j == 0 or j== 29 :
            print("=",end=" ")
        elif i == 4 and j ==2:
            print(full)
        elif i ==6 and  j == 2:
            print(c)
        else :
            print(" ",end=" ")
    print()


# for name in range (len +1  - len) :
#     print(n)
# res = ""
# for name in n:
    
#     res = res + name

# print(res)