import sys

while True:
    print('Hi! -- enter either 1 or 2 or q (to quit)')
    spam = input()
    if spam == '1':
        print('Hello!')
    elif spam == '2':
        print('Howdy!')
    elif spam == 'q':
        sys.exit()
    else:
        print('Try again')



