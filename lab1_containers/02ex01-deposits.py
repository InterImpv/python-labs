#!/usr/bin/env python3

# Calculate deposit percent yield based on time period.

# Imagine your friend wants to put money on a deposit.
# He has got many offers from different banks:
# - First bank declares +A% each day;
# - Second bank promises +B% each month;
# - Third bank offers +C% by the end of the year;
# - The 4th bank promotes +D% in a 10-year term;
# - ... and so on ...

# Your friend gets a terrible headache calculating all this stuff,
# and asks you to help checking everything. You quickly realize
# it is a common task and having a simple script is a great idea.

# Let's implement this.

# A simplified task:
# Given the SUM amount of money, and PERCENT yield promised in a
# FIXED_PERIOD of time, calculate the TOTAL equivalent of money
# in a SET_PERIOD of time.

# Math formula:
# p = PERCENT / 100
# TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))

# TODO: add lines to calculate yields for some common periods
#       of time (e.g. 1 month, 1 year, 5 years, 10 years)
# TODO: change the script to output the 1-year percent yield
#       as well
# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run

# Calculate deposit yield.
def deposit(initial_sum, percent, set_period, fixed_period):
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth

# Switch-case for time unit aliases
def get_full(alias):
    alias_table = {
        'D': 'daily',
        'M': 'monthly',
        'Y': 'yearly'
    }
    ret = alias_table.get(alias)
    return alias if ret is None else ret
    
# Switch-case for time units
def get_form(time, unit):
    alias_table = {
        'D': 'day',
        'M': 'month',
        'Y': 'year',
        'daily': 'day',
        'monthly': 'month',
        'yearly': 'year'
    }
    noun = alias_table.get(unit)
    return (noun + 's') if time > 1.0 else noun

# If initial sum is not provided only percents will be calculated
# This formatting is VERY MESSY AND PAINFUL TO LOOK AT, but essentialy goes like this:
# "{sum} -> {result}, ({delta}), with {percent}% {daily, monthly, yearly} per {period} {day/days, month/months, year/years} for {full_period} {day/days, month/months, year/years}"
# "{delta}%, with {percent}% {daily, monthly, yearly} per {period} {day/days, month/months, year/years} for {full_period} {day/days, month/months, year/years}"
# At this point I am doing these for fun
def calculate(args):
    if args.sum is None:
        d = deposit(1.0, args.percent, args.set_period, args.fixed_period) - 1.0
        print(f'{(d * 100.0):.2f}%, with {args.percent:.2f}% {get_full(args.time)} per {args.set_period:.1f} {get_form(args.set_period, args.time)} for {args.fixed_period} {get_form(args.fixed_period, args.time)}')
    else:
        d = deposit(args.sum, args.percent, args.set_period, args.fixed_period) - args.sum
        print(f'{args.sum:.2f} -> {(args.sum + d):.2f} ({d:.2f}), with {args.percent:.2f}% {get_full(args.time)} per {args.set_period:.1f} {get_form(args.set_period, args.time)} for {args.fixed_period} {get_form(args.fixed_period, args.time)}')

def main(args):
    # Available time period units
    time_units = ['D', 'M', 'Y', 'daily', 'monthly', 'yearly']
    # Command-line argument parser
    p = argparse.ArgumentParser()
    # Available arguments: --* are optional, others are mandatory
    p.add_argument('--time', '-t',
        choices=time_units,
        default='yearly',
        help='time period unit'
    )
    p.add_argument('--sum', '-s',
        type=float,
        help='initial sum of money'
    )
    p.add_argument('--common', '-c',
        action='store_true',
        help='prints yields for 1, 2.5 and 5 years'
    )
    p.add_argument('percent',
        type=float,
        help='promised percent yield'
    )
    p.add_argument('set_period',
        type=float,
        help='set period of time to calculate'
    )
    p.add_argument('fixed_period',
        type=float,
        help='total term'
    )
    # Parse
    args = p.parse_args()
    # User input
    print('User input:')
    calculate(args)
    # Flag check
    if not args.common:
        return 0
    # Common
    print('\nCommon time periods:')
    args.fixed_period = 10.0
    args.time = 'Y'
    # 1 year
    args.set_period = 1.0
    calculate(args)
    # 2.5 years
    args.set_period = 2.5
    calculate(args)
    # 5 years
    args.set_period = 5.0
    calculate(args)

    return 0

if __name__ == '__main__':
    import sys
    import argparse
    sys.exit(main(sys.argv))
