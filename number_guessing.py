import random

secret = random.randint(1, 20)
user_guessing = int(input('guess what i hide: ')) 

while True:
    if user_guessing == secret:
        print('correct')
        break
    elif user_guessing > secret:
        print('High')
    elif user_guessing < secret:
        print('Low')
    else:
        print('Invalid input')
    user_guessing = int(input('Try Again: '))
    
print('Game Over')