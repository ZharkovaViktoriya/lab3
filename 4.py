import random
n=0
k=0
while n!=3:
    a=random.randint(1,10)
    b=random.randint(1,10)
    s=str(a)+ "+" + str(b) + "="
    c=int(input(s))
    if a+b==c:
        k+=1
        print("Правильно!")
    else:
        n+=1
        print("Ответ неверный")
if n==3:
    print("Игра окончена. Правильных ответов:", k)


