import sys
name = input('whats your name? ')
print('Hello, ' + str(name))
word = 'saleh7mo'
turn = 10
guess = ''
while turn > 0:
    i = input('Please Inter a Character:‌ ')
    if len(i) != 1:
        print('please inter exactly "one" character')
        continue
    guess += i
    if i not in word:
        turn -= 1
        print('wrong!')
        print('You have ' + str(turn) + ' turn!')
    win = True
    for c in word:
        if c in guess:
            sys.stdout.write(c)
        else:
            sys.stdout.write('_')
            win = False
    print()
    if win == True:
        print('Congratulation! You win the game!')
        break
print()
if win == False:
    print('You lose the game!')