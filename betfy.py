import os
import random
from time import sleep

def clear_screen():
    os.system('clear')

def welcome_message():
    print('\033[1mBEM-VINDO AO SNUCK!!\n\nAPOSTE NA COR E TENTE A SORTE\033[m.')
    sleep(1)
    print('Seu saldo é de \033[1;32mR$25,00\033[m no início do jogo.\n')
    sleep(2)

def get_bet(saldo):
    while True:
        print('\033[1;30mQuanto você quer apostar?')
        aposta = float(input('=== > \033[1;32mR$'))
        if aposta <= saldo:
            return aposta
        print('\033[1;31mVOCÊ NÃO TEM ESSE VALOR!!\033[m')

def get_color_choice():
    while True:
        print('\033[1;33m\nEscolha uma cor\033[m')
        sleep(1)
        print('''
        [1] \033[1;7;40mBranco\033[m
        [2] \033[1;7;31mVermelho\033[m
        [3] \033[1;7;32mVerde\033[m''')
        escolha = int(input('\n=== > '))
        if escolha in [1, 2, 3]:
            return escolha
        print('\033[1;31mOPÇÃO INVÁLIDA!! Digite apenas 1, 2 ou 3\033[m')
        sleep(1)

def print_color_sorteada(cor_sorteada):
    print('\033[1;36m\nA COR SORTEADA FOI\033[m', end='')
    for _ in range(3):
        print('\033[1;36m.\033[m', end='', flush=True)
        sleep(2)
    print('\n{}'.format(cor_sorteada))

def play_again(saldo):
    saldo_formatted = "{:,.2f}".format(saldo)
    print(f'\n\033[1mSALDO ATUAL\033[1;32m R${saldo_formatted}\033[m\n')
    print('\033[1;30mVOCÊ NÃO TEM MAIS SALDO!!\033[m')
    print('\033[1m[1] RECARREGAR\033[m')
    print('\033[1m[2] Para SAIR\033[m')
    while True:
        r = int(input('\033[1m=== > '))
        sleep(1)
        if r == 1:
            print('\033[1mRECARGA, adicione o valor.\033[m')
            rr = float(input('\033[1m=== >\033[m\033[1;32mR$'))
            saldo += rr
            saldo_formatted = "{:,.2f}".format(saldo)
            sleep(1)
            print(f'\033[1mVocê Adicionou com ÊXITO \033[1;32mR${saldo_formatted}\033[m a sua conta!')
            return saldo
        elif r == 2:
            sleep(1)
            print('Até a Próxima!')
            return False
        print('\033[1;31mOPÇÃO INVÁLIDA\033[m')

def snuck_game():
    clear_screen()
    welcome_message()

    saldo = 25.00
    opcoes = ['\033[1;7;40mBranco\033[m ', '\033[1;7;31mVermelho\033[m ', '\033[1;7;32mVerde\033[m ']
    cores_jogadas = []

    while saldo > 0:
        cor_sorteada = random.choice(opcoes)

        saldo_formatted = "{:,.2f}".format(saldo)
        print(f'\n\033[1mSALDO ATUAL\033[1;32m R${saldo_formatted}\033[m\n')
        aposta = get_bet(saldo)

        clear_screen()
        saldo_formatted = "{:,.2f}".format(saldo)
        print(f'\n\033[1mSALDO ATUAL\033[1;32m R${saldo_formatted}\033[m\n')
        escolha = get_color_choice()

        cor_sorteada = random.choice(opcoes)
        cores_jogadas.append(cor_sorteada)

        clear_screen()
        print_color_sorteada(cor_sorteada)

        if cor_sorteada == opcoes[escolha-1]:
            print('\033[1;32m\nACERTO!! Parabéns você acertou\033[m')
            saldo += aposta
        else:
            print('\033[1;31m\nERRO!! Infelizmente você errou\033[m')
            saldo -= aposta

        print('\nCORES SORTEADAS: ', end=' ')
        for cor in cores_jogadas:
            print(cor, end='')
        sleep(1)

        if saldo <= 0:
            saldo = play_again(saldo)
            if not saldo:
                break

snuck_game()
