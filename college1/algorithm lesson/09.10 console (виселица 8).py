words_list = ['яблоко','градус','ливень','мастер','кувшин','компас','росток','брелок','глобус','пароль','собака','пряник']
import random
guess_word = words_list[random.randint(0,len(words_list)-1)].upper()

area = [
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*',"*",'*','*','*','*','*','*'],
    ['*','_','_','_','_','_','_','*'],
    ['*','*','*','*','*','*','*','*']
]

def showArea():
    for i in range(len(area)):
        for j in range(len(area[i])):
            print(area[i][j], end=' ')
        print()

def insertGuessedWord(player_guess,floor):
    for i in range(1,len(area[0])-1):
        area[floor][i] = player_guess[i-1]
        if player_guess[i-1] == guess_word[i-1]:
            area[floor+1][i] = '#'
        if (player_guess[i-1] != guess_word[i-1]) and (player_guess[i-1] in guess_word):
            area[floor+1][i] = '!'

showArea()
print('Добро пожаловать, игра "Виселица"')
print("Угадайте слово из 6-букв за шесть попыток: ")
player_guess = str(input()).upper()
isGuessed = False
tries = 1
floor = 1

while not isGuessed and tries != 6:
    if len(player_guess) != 6:
        print("Введите слово из 6-букв! ")
        player_guess = str(input()).upper()
        continue
    tries += 1

    if player_guess == guess_word:
        isGuessed = True
        insertGuessedWord(player_guess,floor)
        showArea()
        print("Поздравляем, вы угадали слово!")

    if player_guess != guess_word:
        insertGuessedWord(player_guess,floor)
        showArea()
        print("Введите слово: ")
        player_guess = str(input()).upper()

    floor += 2

if isGuessed == False:
    print("К сожалению, вы не угадали загаданное слово: ", guess_word)