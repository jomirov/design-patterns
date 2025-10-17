import pygame
pygame.init()
screen = pygame.display.set_mode((1280,720))
running = True
fieldRow = 0

words_list = ['яблоко','градус','ливень','мастер','кувшин','компас','росток','брелок','глобус','пароль','собака','пряник']
import random
guess_word = words_list[random.randint(0,len(words_list)-1)].upper()

def drawCells():

    for row in range(6):
        for col in range(6):
            pygame.draw.rect(screen,'grey',(screen.get_width() / 2.55 + row * 50,screen.get_height() / 4.2 + col * 50,40,40))

def renderWords():
    for row in range(len(player_guesses)):
        letter_list = list(player_guesses[row])
        temp_guess_word = list(guess_word)

        for col in range(6):
            color = (90,90,90)
            if letter_list[col] == temp_guess_word[col]:
                color = 'green'
                temp_guess_word[col] = ''
                letter_list[col] = ''
            elif letter_list[col] != '' and letter_list[col] in temp_guess_word:
                color = 'yellow'
                temp_guess_word[temp_guess_word.index(letter_list[col])] = ''

            letter_font = pygame.font.SysFont('',30)
            word_letter = letter_font.render(player_guesses[row][col],True,color)
            screen.blit(word_letter,(screen.get_width() / 2.5 + col * 50,screen.get_height() / 4 + row * 50))

    if not guess_word in player_guesses and len(player_guesses) != 6:
        for col in range(len(player_guess)):
            letter_font = pygame.font.SysFont('',30)
            word_letter = letter_font.render(player_guess[col],True,(50,50,50))
            screen.blit(word_letter,(screen.get_width()/2.5 + col * 50,screen.get_height()/4+fieldRow*50))
    elif guess_word in player_guesses:
        winner_text = medium_Font.render('Поздравляем, вы угадали слово!', True,'green')
        task_text2 = medium_Font.render('Нажмите Enter, чтобы начать заново', True, 'yellow')
        screen.blit(winner_text, (screen.get_width()/3+50,500))
        screen.blit(task_text2, (screen.get_width()/3+35,550))

    elif not guess_word in player_guesses and len(player_guesses) == 6:
        lose_text = medium_Font.render('К сожалению, вы не угадали слово.',True,'yellow')
        task_text2 = medium_Font.render('Нажмите Enter, чтобы начать заново',True,'yellow')
        screen.blit(lose_text,(screen.get_width() / 3 + 40,500))
        screen.blit(task_text2,(screen.get_width() / 3 + 35,550))

player_guesses = []
player_guess = ""
returnedTime = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pressedKey = pygame.key.name(event.key)
            print(event.unicode, pressedKey)
            if pressedKey == 'backspace':
                player_guess = player_guess[:-1]
            elif len(player_guess) == 6 and pressedKey == 'return':
                fieldRow += 1
                player_guesses.append(player_guess.upper())
                player_guess = ''
                print(guess_word,player_guesses)
            elif len(player_guess) <= 5 and (len(pressedKey) == 1 or event.unicode in ['э','ю','ж','ъ','х','б']) and fieldRow < 6 and not guess_word in player_guesses:
                player_guess += event.unicode.upper()

            if guess_word in player_guesses and pressedKey == 'return':
                pressedKey = None
                returnedTime += 1
                if returnedTime == 2:
                    fieldRow = 0
                    player_guesses = []
                    guess_word = words_list[random.randint(0,len(words_list)-1)].upper()
                    returnedTime = 0

    screen.fill('white')

    pygame.draw.rect(screen,'grey',(0,0,400,720))
    pygame.draw.rect(screen,'grey',(900,0,400,720))

    drawCells()
    renderWords()

    big_Font = pygame.font.SysFont('',40)
    medium_Font = pygame.font.SysFont('',30)
    welcome_text = big_Font.render('Добро пожаловать в "Висилицу"',True,'black')
    task_text = medium_Font.render('Найдите слово из 6-букв за 6 попыток:',True,'black')


    screen.blit(welcome_text,(screen.get_width()/3,50))
    screen.blit(task_text,(screen.get_width()/3+30,100))
    pygame.display.flip()


pygame.quit()