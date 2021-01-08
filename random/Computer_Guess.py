import random
def computer_guess(x):
    number = int(input("Give your number: "))
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        if guess < number:
            feedback = 'l'
            print(f'{guess} is too low')
        elif guess > number:
            feedback = 'h'
            print(f'{guess} is too high')
        else:
            feedback = 'c'
            print(f'{guess} is correct!!')
        if(feedback == 'h'):
            high = guess - 1
        elif (feedback == 'l'):
            low = guess + 1
    print(f'Yah! the computer guess your number , {guess}, correctly!!')
computer_guess(1000)
