def gugudan():
    dan = int(input("몇단을 입력할까요? "))
    for i in range(1, 10):
        print(dan, "x", i, "=", dan * i)

gugudan()