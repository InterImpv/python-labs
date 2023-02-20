## deposit

Modified script from python course. Original description:

> Calculate deposit percent yield based on time period.

>A simplified task:

>Given the SUM amount of money, and PERCENT yield promised in a FIXED_PERIOD of time, calculate the TOTAL equivalent of money in a SET_PERIOD of time.

> Math formula:

> p = PERCENT / 100

> TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))

Changes:

- script calculates yields for some common periods of time: 1 year, 2.5 years, 5 years;
- script outputs only percents if the initial SUM is not known at the moment the script is run;
- script uses `argparse` to parse command-line;
- tried to do a minor refactor, made it worse;

## vikings

Modified script from python course. Original description:

> The famous Vikings restoraunt from the Monthy Python sketch.

> See the sketch origins video first: https://www.youtube.com/watch?v=zLih-WQwBSc

Changes:

- reworked the script to use `argparse`;
- cleared dialogue;

## task02

A simple roguelike wannabe with an ability to add your own monsters to the game using JSON (**enemies.json**).

To start a new game or restart it if your player-character dies use:

`./task02-game.py --restart` or `./task02-game.py -r`

It resets all player stats and randomly chooses a new monster from a list in **enemies.json**

You can also randomly choose a new monster if it either dies or you just don't like what you've got, without resetting your player-character using:

`./task02-game.py --new` or `./task02-game.py -n`

When you are ready you are free to choose an action for the next turn using:

`./task02-game.py --action <action>` or `./task02-game.py -a <action>`

Available actions are listed below:

- *attack* - rolls a dice between 0 and **damage** and applies it to your enemy. Enemy's **defence** determines how much **damage** will absorbed;
- *defend* - doubles your **defence** stat for a turn;
- *heal* - heals random amount of health between 1 and 6;
- *show* - currently does nothing.

Your enemy can also use *attack*, *defend* and *heal*.

### Modding

You can add your own monsters by adding a new entry to the enemy list in **enemies.json**. Here's a template for that:

```
{
    "name": "Enemy",
    "hp": 10,
    "max_hp": 10,
    "damage": 5,
    "defence": 5,
    "attack_weight": 5,
    "defend_weight": 5,
    "heal_weight": 5
}
```

Currently any error detection is essentialy non-existant so good luck. Also the game will error-out if **enemies.json** is empty or does not exist.

What each parameter does:

- *hp* - current health the enemy has. Should be equal to *max_hp*;
- *max_hp* - maximum health enemy can have;
- *damage* - maximum amount of damage that can be rolled;
- *defence* - amount of damage that can be absorbed;
- *attack_weight* - offensive action probability;
- *defend_weight* - defensive action probability;
- *heal_weight* - healing action probability;
