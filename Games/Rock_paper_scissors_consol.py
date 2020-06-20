import random


class Player:
    def __init__(self, chooses, identification, win):
        self.identification = identification
        self.chooses = chooses
        self.win = win
        self.history = []

    def choose(self, chooses):
        self.chooses = chooses
        self.history.append(self.chooses)

# TODO add class for elements what can chose player

def main():
    print('============================')
    print('|| Hi im Romanua911!      ||')
    print('|| It is game             ||')
    print('|| Rock, paper, scissors  ||')
    print('============================')
    count = count_round()
    print('============================')
    print('||Game start             ||')
    print('============================')
    game(count)
    print(" GAME END ")

def game(count):
    human = Player(0, 1, 0)
    computer = Player(0, 1, 0)
    for i in range(count):
        print("Round:"+str(i+1))
        print("First player choose ")
        print("r - ROCK | p - paper | s - scissor ")
        human.choose(input("Choose:"))
        # TODO add input validator
        print("Computer choose ")
        print("r - ROCK | p - paper | s - scissor ")
        computer.choose(random.choice(['r','p','s']))
        print('Choose:'+computer.chooses)
        checkwinner(human,computer)
    print("Player win {} round".format(human.win))
    print("Computer win {} round".format(computer.win))
    # TODO add ho is winner


def checkwinner(firstplayer, secondplayer):
    if firstplayer.chooses == secondplayer.chooses:
        pass
    elif firstplayer.chooses == 'r' and secondplayer.chooses == 's':
        firstplayer.win += 1
    elif firstplayer.chooses == 's' and secondplayer.chooses == 'p':
        firstplayer.win += 1
    else:
        secondplayer.win += 1


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
