print("自然数を入力してください")
number = int(input("入力された自然数を素数か判断します"))
safe ="true"
if number > 1:
    for x in range(number-1):
        if x > 1 and number % (x + 1) == 0:
            safe ="false"
            
elif number == 1:
    safe = "false"
elif number < 1:
    print("自然数ではありません")
    safe = "Other"

if safe =="true":
    print("素数")
elif safe == "false":
    print("素数ではない")
