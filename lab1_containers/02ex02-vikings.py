#!/usr/bin/env python3

# The famous Vikings restoraunt from the Monthy Python sketch.

# See the sketch origins video first:
# https://www.youtube.com/watch?v=zLih-WQwBSc


DEF_CHOICE = 8      # how many times to repeat a dish
MENU = ['spam', 'egg', 'sausage', 'bacon']  # that's all combinations
MENU_MULTI = MENU + ['eggs', 'sausages']    # including plurals
JOINTS = [', and ', ', ', ' and ', ' with ', ' and double portion of ']
PREFERED = MENU[0]  # that's what promoted most
FORBIDDEN = {'not', 'without', 'no'}

SONG = ', '.join([PREFERED.capitalize()] + [PREFERED] * DEF_CHOICE) + '!'

D_WELCOME = "Waitress: \"Welcome to the Vikings restaurant. What would you like to eat?\""
D_PROMOTE = "Waitress: \"We highly recommend {dishes}" + f", and {PREFERED}...\""
D_GOOD = "Waitress: \"That\'s a perfect choice. Let\'s have more {dishes}" + f", and {PREFERED}!\""
D_BAD = "Waitress: \"Disgusting. Who eats {dishes}?\""
D_UNAVAILABLE = "Waitress: \"That\'s not on our menu. We have {dishes}.\""

def promote(num_choice=DEF_CHOICE):
    print(D_PROMOTE.format(dishes=get_dishes(num_choice)))
    return

# User dialog logic
def dialog(args):
    entry = args.dish.lower().strip()
    words = args.dish.lower().split()

    print(D_WELCOME)
    print("You: \"" + args.dish.strip() + "\"")
    
    if set(words) & set(MENU_MULTI):
        # user named something on the menu - do further check
        if set(words) & set(FORBIDDEN):
            # user asked not to put common dishes - blame
            print(D_BAD.format(dishes=entry))
            promote(args.amount)
        else:
            # user asked for what's on menu - compliment
            print(D_GOOD.format(dishes=entry))
            print(f'Vikings: "{SONG}"')
        return

    if not words:
        # user haven't selected anything - promote a good menu
        promote(args.amount)
        return
    
    print(D_UNAVAILABLE.format(dishes=get_dishes(args.amount)))
    return

# Form a random combination of dishes
def get_dishes(number):
    sel = list(MENU)

    res = []
    for i in range(number):
        rnd = random.choice(sel)
        #sel.remove(rnd)
        res.append(rnd)
        res.append(random.choice(JOINTS))
    res = res[:-1]      # remove last element
    
    return ''.join(res)

def main(args):
    # command-line argument parser
    p = argparse.ArgumentParser()
    # available arguments: --* are optional, others are mandatory
    p.add_argument('dish',
        help='dish you want to order'
    )
    p.add_argument('--amount', '-a',
        type=int,
        default=DEF_CHOICE,
        help='amount of dishes you want to order'
    )
    args = p.parse_args()
    
    dialog(args)

    return 0

if __name__ == '__main__':
    import sys
    import argparse
    import random
    sys.exit(main(sys.argv))
