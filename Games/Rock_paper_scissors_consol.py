import random

class Player:
    def __init__(self, chooses, identification, win, history):
        self.identification = identification
        self.chooses = chooses
        self.win = win
        self.history = history

    def choose(self,chooses,history):
        self.history = history.append(self.chooses)
        self.chooses = chooses


def main():
    print('============================')
    print('|| Hi im Romanua911!      ||')
    print('|| It is game             ||')
    print('|| Rock, paper, scissors  ||')
    print('============================')
    count = count_round()
    print('============================')
    print('|| Game start             ||')
    print('============================')
    game()

def game():
    human = Player(0, 1, 0, [])
    computer = Player(0, 1, 0, [])


    return True

def count_round():
    print('============================')
    print('||     How much round ?   ||')
    print('============================')
    while True:
        value = input('Value:')
        try:
            value = int(value)
        except ValueError:
            print('Valid number, please')
            continue
        if 0 < value <= 10:
            break
        else:
            print("Valid range, please: 1-10")
    return value


if __name__ == "__main__":
    main()
