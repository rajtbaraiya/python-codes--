raw = ['  divyesh BALAI', 'rajat  ', 'Divyesh Balai', 'RAJAT', 'khushi shah', ' Khushi  Shah ']
clean = []
for name in raw:
    name = " ".join(name.strip().split())
    name = name.title()
    clean.append(name)
    
print(clean) 

uni = []
duplicate = 0
for name in clean:
    if name not in uni:
        uni.append(name)
    else:
        duplicate = duplicate + 1
uni.sort()

print("Clean List : ",uni)
print("Duplicate are Removed : ",duplicate)