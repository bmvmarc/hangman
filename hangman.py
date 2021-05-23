import random
from string import ascii_lowercase


class Hangman:
    options = ('python', 'java', 'kotlin', 'javascript')

    @staticmethod
    def menu():
        opt = ''
        print('H A N G M A N')
        while opt != 'exit':
            opt = input('Type "play" to play the game, "exit" to quit:')
            if opt == 'play':
                Hangman().start_game()

    def __init__(self):
        self.right = random.choice(Hangman.options)
        self.hidden = len(self.right) * '-'
        self.guesses = set()
        self.life = 8

    def start_game(self):

        while self.life > 0:
            print('\n' + self.hidden)
            letter = input('Input a letter: ')

            if len(letter) != 1:
                print('You should input a single letter')

            elif letter not in ascii_lowercase:
                print('Please enter a lowercase English letter')

            elif letter in self.guesses:
                print('You\'ve already guessed this letter')

            elif letter in self.right:
                self.guesses.add(letter)
                if letter in self.hidden:
                    print('You\'ve already guessed this letter')
                else:
                    self.hidden = ''.join(
                        self.right[i] if self.right[i] == letter else self.hidden[i] for i in range(len(self.hidden)))
                    if self.hidden == self.right:
                        print('\n' + self.hidden)
                        print('You guessed the word!\nYou survived!')
                        break
            else:
                self.guesses.add(letter)
                print('That letter doesn\'t appear in the word')
                self.life -= 1
        else:
            print('You lost!')


Hangman.menu()
