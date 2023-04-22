#!/usr/bin/env python3.10

def get_adjective_from_suit(card):
    match card.suit:
        case cards.SuitEnum.HEARTS:
            return 'marvelous'
        case cards.SuitEnum.DIAMONDS:
            return 'good'
        case cards.SuitEnum.CLUBS:
            return 'bad'
        case cards.SuitEnum.SPADES:
            return 'terrible'

def fortune_from_card(card):
    fstr = f'The {card.full()} brings {get_adjective_from_suit(card)} '
    match card.rank:
        case cards.RankEnum.TWO:
            return (fstr + 'opposition.')
        case cards.RankEnum.THREE:
            return (fstr + 'creativity.')
        case cards.RankEnum.FOUR:
            return (fstr + 'foundation.')
        case cards.RankEnum.FIVE:
            return (fstr + 'change.')
        case cards.RankEnum.SIX:
            return (fstr + 'adaptation.')
        case cards.RankEnum.SEVEN:
            return (fstr + 'suprise.')
        case cards.RankEnum.EIGHT:
            return (fstr + 'karma.')
        case cards.RankEnum.NINE:
            return (fstr + 'fortune.')
        case cards.RankEnum.TEN:
            return (fstr + 'completion.')
        case cards.RankEnum.ELEVEN:
            return (fstr + 'judgement.')
        case cards.RankEnum.TWELVE:
            return (fstr + 'perfection.')
        case cards.RankEnum.THIRTEEN:
            return (fstr + 'luck.')
        case cards.RankEnum.JACK:
            return (fstr + 'friends.')
        case cards.RankEnum.QUEEN:
            return (fstr + 'love.')
        case cards.RankEnum.KING:
            return (fstr + 'power.')
        case cards.RankEnum.ACE:
            return (fstr + 'beginning.')
        case _:
            return f'The {card.full()} is too cryptic.'

def main(args):
    p = argparse.ArgumentParser()
    # available arguments:
    p.add_argument('--deck', '-d',
        choices=('stripped', 'full', 'expanded'),
        default='full',
        help='deck type',
        required=True
    )
    # Parse
    args = p.parse_args()

    match args.deck:
        case 'stripped':
            deck = cards.StrippedDeck()
        case 'expanded':
            deck = cards.ExpandedDeck()
        case _:
            deck = cards.FullDeck()
    
    deck.shuffle()
    card_n = random.randint(2, 5)

    print(f'You take {card_n - 1} card(s) from deck...')
    for i in range(1, card_n):
        card = deck.get_bottom()
        print(f'{i})\t{fortune_from_card(card)}')
    
    return 0

if __name__ == '__main__':
    import sys
    import random
    import argparse
    import cards
    sys.exit(main(sys.argv))