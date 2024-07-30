# game_map

Game Map is a small game developed purely using Python 3.8 and being displayed in the shell of any operative System.

The game consist about one or multiple players that needs to find the exit square throwing many dices as possible. In the board map they will find multiple types of square where they can fall inside:

## Squares
- Start: The first square where all the players starts the first iteration of the game.
- Monsters: If the character falls into one of these squares, they will fight with the monster during multiple iterations while both of them are alive. Some monster could give some weapons to wear.
- Portals: If a character falls inside into a portal, he/she will be teleported into another portal position. If the character has an specific weapon, then will can choose which portal exit to take.
- Exit: The first character to falls into will win the game.

# Project Structure and internal behaviour

## Project Structure

### Demos
There are, right now, two python scripts with two playable demos: 
- Only walking: The player can throw the dice and moves around the map without enter in any combat/battle. It is finished when any player enters in the Finish Square.
- Walk and Battle: The players can try every square that they want. 
### Game Objects
There are some Weapons that can be added to our Characters to give them better abilities or increase their status. One of the examples could be: get the ability of crossing fake walls or increase your defenses. 
### Tests
There are located the different unit testing for the different classes also testing for printing the boardmap.
## Battle Development
- The Battle class simulates a battle between a character and a monster with a possibility of a surprise attack.
- Damage calculations are influenced by random factors and the respective defenses of the combatants.
- The outcome of the battle updates the character’s status and the game state based on the result of the combat.

## Future Implementations:
- Treasure square: This will include a weapon to help the characters increasing their vital status or giving them any ability: cross fake walls of capacity of choose the exit of a teleport.
- PRINT MAP: The project needs a better way to make the prints of the map into the shell.

## Future Enhancements:
- Docker: Using Docker, create a container where the game is fully playable.
- Create a web application where the game would have a more visual and interactive display.