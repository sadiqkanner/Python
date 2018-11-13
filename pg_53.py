name = ''
while not name:
    print('Enter Your Name : ')
    name = input()
    print('How Many Guests will you Have?')
    numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
    
print('Done')