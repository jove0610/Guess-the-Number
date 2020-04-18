import random, sys

num = random.randint(1, 20)
print('Guess a number between 1 and 20. You have 6 attempts.')
for i in range(5):
    while True:
        myNumber = input()
        try:
            myNumber = int(myNumber)
            if myNumber == num:
                print('Congratulations! It took you ' + str(i + 1) + ' attempts.')
                input('Press any key to exit.')
                sys.exit()
            elif myNumber < num:
                print('Your number is too low. (Remaining Attempts: ' + str(5 - i) + ')')
                break
            else:
                print('Your number is too big. (Remaining Attempts: ' + str(5 - i) + ')')
                break
        except ValueError:
            print('Please put an integer. (No fraction or decimal)')
print('You have used all your 6 attempts. The correct answer is ' + str(num) + '.')
