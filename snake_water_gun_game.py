import random
user = 0
computer = 0
turns = 0
while (turns<10):
    a = ['Snake','Water','Gun']
    pc = random.choice(a)
    print(pc)
    turns +=1
    dic = {1:'Snake',2:'Water',3:'Gun'}
    b = int(input('1.Snake,2.Water,3.Gun'))
    if b in dic:
        print(dic[b])
        if pc == 'Snake':
            if dic[b] == 'Snake':
                print('its tie')
            elif dic[b] == 'Water':
                print('PC wins')
                computer +=1
            elif dic[b] == 'Gun':
                print('user wins')
                user+=1
                
        elif pc == 'Water':
            if dic[b] == 'Snake':
                print('user wins')
                user+=1
            elif dic[b] == 'Water':
                print('its tie')
            elif dic[b] == 'Gun':
                print('computer wins')
                computer +=1
         elif pc == 'Gun':
            if dic[b] == 'Snake':
                print('PC wins')
                computer+=1
            elif dic[b] == 'Water':
                print('user wins')
                user+=1
            elif dic[b] == 'Gun':
                print('its a tie')
    else:
        print('retry entry')

print('Game over', 'user:',user,'computer:',computer)
