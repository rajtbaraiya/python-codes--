for num in range(1,61):
    word = ""
    if num % 4 == 0 and num % 6 == 0:
        word = "ChaiBreak"
    elif num % 4 == 0:
        word = "Chai"
    elif num % 6 == 0:
        word = "Break"
    else:
        word = str(num)
        
    if "3" in str(num)  and word != str(num):
        word = word[::-1]
        
    print(f"{num} -> {word}")