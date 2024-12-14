import random 
playing = True 

number = str(random.randint(10,20))
print("I will generate a random number between 10 and 20 and you have to guess the number one digit at a time")

while playing == True:
    guess = input("Enter your guess:")
    if guess == number:
        print("Your guess is correct")
        number = str(random.randint(10,20))
        
    else:
        print("Your guess is wrong")
        print("The number was", number)
        number = str(random.randint(10,20))
