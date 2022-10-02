import random
secret = random.randint(1, 100)
print("猜数游戏：我想了一个1-100的整数，你最多可以猜六次")
tries = 1
while tries <= 6:
    guess = int(input("please input int number, it is %d time guess"% (tries, )))
    if guess == secret:
        print("conlation" % (tries, secret))
        break
    elif guess > secret:
        print("please bigger number")
    else:
        print("xiaoleyidian")
    tries += 1
else:
    print("upset, do not worried")
