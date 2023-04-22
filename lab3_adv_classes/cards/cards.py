#!/usr/bin/env python3.10
# i broke my system and i am too lazy and afraid to fix this

from enum import Enum
import random
import itertools

class SuitEnum(Enum):
    JOCKER = '\u2605'   #★ - special one, be wary
    SPADES = '\u2660'   #♠
    HEARTS = '\u2665'   #♥
    DIAMONDS = '\u2666' #♦
    CLUBS = '\u2663'    #♣

    def __str__(cls):
        return f'{cls.name.lower()} ({cls.value})'

# jocker, ace, two -> ten, jack, queen, king.
class RankEnum(Enum):
    JOCKER = '%'    #[0] special one, be wary
    TWO = 2         #[1]
    THREE = 3       #[2]
    FOUR = 4        #[3]
    FIVE = 5        #[4]
    SIX = 6         #[5]
    SEVEN = 7       #[6]
    EIGHT = 8       #[7]
    NINE = 9        #[8]
    TEN = 10        #[9]
    ELEVEN = 11     #[10]
    TWELVE = 12     #[11]
    THIRTEEN = 13   #[12]
    JACK = 'J'      #[13]
    QUEEN = 'Q'     #[14]
    KING = 'K'      #[15]
    ACE = 'A'       #[16]

    def __str__(cls):
        return f'{cls.name.lower()} ({cls.value})'

class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def short(self):
        return f'{self.rank.value}{self.suit.value}'

    def full(self):
        return f'{self.rank.name.lower()} of {self.suit.name.lower()}'
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.rank} of {self.suit}>'

class JockerCard(Card):
    def __init__(self):
        super().__init__(RankEnum.JOCKER, SuitEnum.JOCKER)

    def full(self):
        return 'jocker'
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: jocker>'

class CardDeckBase:
    __slots__ = 'cards'

    def __init__(self):
        self.cards = list()

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def get_top(self):
        return self.cards.pop(0) if len(self) else None
    
    def get_bottom(self):
        return self.cards.pop(len(self) - 1) if len(self) else None

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return f'<{self.__class__.__name__}: has {len(self)} card(s) left>'

# feel like deck composition code could be reused,
# but not sure how to do it in a pretty way

# 36-cards: 4 suits and 9 ranks
class StrippedDeck(CardDeckBase):
    def __init__(self):
        super().__init__()
        # ranks and suits used
        ranks = list(RankEnum)[5:10] + list(RankEnum)[13:17]
        suits = list(SuitEnum)[1:]
        # all combinations
        products = itertools.product(ranks, suits)
        # fill in the deck
        for product in products:
            self.cards.append(Card(product[0], product[1]))

# 52-cards: 4 suits and 13 ranks
class FullDeck(CardDeckBase):
    def __init__(self):
        super().__init__()
        # ranks and suits used
        ranks = list(RankEnum)[1:10] + list(RankEnum)[13:17]
        suits = list(SuitEnum)[1:]
        # all combinations
        products = itertools.product(ranks, suits)
        # fill in the deck
        for product in products:
            self.cards.append(Card(product[0], product[1]))
            
# 63-cards: full + 11ths (all suits), 12ths (all suits), 13ths (red suits) + 1 jocker
class ExpandedDeck(CardDeckBase):
    def __init__(self):
        super().__init__()
        # ranks and suits used
        ranks = list(RankEnum)[1:12] + list(RankEnum)[13:17]
        suits = list(SuitEnum)[1:]
        # all combinations
        products = itertools.product(ranks, suits)
        # fill in the deck
        for product in products:
            self.cards.append(Card(product[0], product[1]))
        # both 13 red suits + jocker
        self.cards.append(Card(RankEnum.THIRTEEN, SuitEnum.HEARTS))
        self.cards.append(Card(RankEnum.THIRTEEN, SuitEnum.DIAMONDS))
        self.cards.append(JockerCard())