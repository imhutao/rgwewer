from random import randint
r = randint(1, 10)
a = 0

print("угадай число от 1 до 10")
n = int(input())
while True:
    if r == n:
        print("верно!")
        break
    if n != r:
        a =+ 1
        print("неверно. ты потратил", a,"попытку из 5. попробуй снова")
        n = int(input())
