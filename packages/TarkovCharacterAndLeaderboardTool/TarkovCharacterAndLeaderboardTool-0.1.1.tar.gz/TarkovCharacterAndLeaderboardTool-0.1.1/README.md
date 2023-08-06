# <p align="center"> Tarkov Character Tool and Leaderboard Ranking</p>

<p align="center">
<img src="https://www.escapefromtarkov.com/themes/eft/images/logo.png" alt="Escape from Tarkov Logo"/></p>

A tool designed to allow users to create characters for the franchise "Escape from Tarkov" and access a number of
functions to follow along with their progress. As well as users being able to utilise leaderboards which rank characters
that have been created by the user's choice. Either by the character level, or the amount of kills.

The leaderboards that are available aren't just set to be organised by the character level or the amount of kills, 
leaderboards can also be sorted explicitly by a specific faction. So there is a global leaderboard, for all characters, 
and then individual leaderboards for 'USEC' and 'BEAR' faction characters.

Users are also able to make use of other functions, such as determining their journey to unlocking the Kappa Container.

-----

### Kappa Container

#### What is the Kappa Container?

The Kappa Container is an in-game item, acquirable by the user. However, it is only obtainable once the user has
completed a set amount of prerequisites. Such as, completing the quest line, and being the relevant level.

#### What's the purpose of the function within this project?

The function takes the character's level and subtracts that by the required level needed to unlock the item. Then, the
function returns to the user how far they are from acquiring the container, or, if they are already eligible to unlock
the container.

----

### Features

- Ability to create characters of different types, and a part of different factions.
- Free to access pre-existing characters.
- See Kappa Container progression of chosen character.
- View a variety of leaderboards, which are able to be sorted by the user, to display relevant information to the
  preference of the user. Ranking in descending order.

-----

### Install

The tabulate library is required for this code, which needs to be installed.

```
pip install tabulate
```

-----

### Usage

Certain parts of the code will work on their own. However, setting up a database, preferably a mySQL database, will
allow characters that have been created to be saved, to be called upon later, and it allows the leaderboard function to
work as intended.

So, firstly, you're going to want to navigate to the utility_funcs.py file and view the create_db_connection() method.
Then from there, you're going to want to replace the relevant host, user, password, and database information with your
own created database, or existing database. This ensures that the code can connect to a working database and for any
query statements which have been executed to run correctly.

If that is set up correctly, the main.py file is able to be executed. 

Once the code runs, it will display to the user "Welcome to the Tarkov Character Creation and Leaderboard Tool." and
then the user is prompted with a number of options.

Dependent on the input from the user, it will progress through those functions.

When the user enters "1" into the input, the code will take in a number of inputs to determine the character name, type,
faction, voice, level, and the amount of kills that the user wants to assign to their created character.

When the user enters "2" the user is asked to provide a character name. If that name matches a preexisting character
name, it will print the relevant information relating to that character to the user. Although, if a user enters a name
that doesn't already exist, the code will print an invalid input to the user, telling them that, that character
doesn't exist, and if they would like to create a character instead.

When the user enters "3" to view the leaderboard rankings, the code presents options back to the user. The user has the
ability to access the Global Leaderboard, USEC Leaderboard, or the BEAR Leaderboard. The user can access this function
regardless of if they have created a character or not. This is where the user can decide for themselves whether they 
wish to sort the chosen leaderboard by "Level" or "Kills" as previously mentioned.
