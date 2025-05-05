print("自然数を入力してください")
number = int(input("ここに入力"))
safe ="true"
if number > 1:
    for x in range(number-1):
        print(x)
        if x > 1 and number % (x + 1) == 0:
            safe ="false"
            
elif number == 1:
    safe = "false"

if safe =="true":
    print("素数")
else:
    print("素数ではない")