#!/usr/bin/env python3

def avg(*args):
    average = 0
    length = 0
    # this feels so bad but funny
    try:
        for arg in args:
            average += sum(arg)
            length += len(arg)
        average = average / length
    except TypeError:
        average = sum(args) / len(args)
    return average

def main(args):
    # find averages of multiple args, lists, tuple, dictionary and a set
    print(avg(1, 1, 2, 3, 5, 8, 13))
    print(avg([1, 1, 2], [3, 5], [8, 13]))
    print(avg([1, 1, 2, 3]))
    print(avg((1, 2)))
    print(avg({1:'one', 2:'two', 5:'three'}))
    print(avg({1, 2, 4, 8, 16, 32}))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
