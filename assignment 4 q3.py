import random
print("Welcome to the game")
for num in range(0,10):
    num1=random.randint(2,12)
    num2=random.randint(2,12)
    answer=num1*num2 
    print("What is",num1,"X",num2,":")
    guess=int(input("Answer:"))
    if guess==answer:
        print("This is the correct answer")
    elif guess!=answer:
        print("This is not the correct answer")
    else: 
        print("Enter the valid guess")