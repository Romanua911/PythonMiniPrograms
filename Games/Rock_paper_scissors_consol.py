import random


def main():
    print('============================')
    print('|| Hi im Romanua911!      ||')
    print('|| It is game             ||')
    print('|| Rock, paper, scissors  ||')
    print('============================')
    count = count_round()

def pve:
    pass

def pvp():
    pass

def count_round():

    print('============================')
    print('||     How much round ?   ||')
    print('============================')
    while True:
        value = input('Value:')
        try:
            count = int(value)
        except ValueError:
            print('Valid number, please')
            continue
        if 0 < value <= 10:
            break
        else:
            print("Valid range, please: 1-10")
    return count

if __name__ == "__main__" :
    main()