# Maze-Generator

Maze Generator that creates a maze with chosen size and also plots the optimal path to the exit.

## About

In a one-day work, using a Randomized Prim's Algorithm, I created a maze generator. As it was a Friday, I continued doing it until Sunday, when I achieved the final program. The main file consists of one main function and two main processes.

#### > Generating Maze

Using a Randomized Prim's Algorithm in a Square with size n x m, I could create a Maze Generator. Briefly, this algorithm color its tiles in a way that two adjacent tiles will never be the same (wall/path).

#### > Finding Exit Path

Using the A* algorithm to find the way out of the generated maze, I could create the Path Finder function. Besides being very efficient, this algorithm find the way out very fast, even with big mazes.

#### > Path Finder Function

The main function of this program is called **path_finder(n, m)**. When you call it, a maze (with entrance and exit point) is generated and plotted in your output screen. After this, the same program find its exit and color the path in yellow and plot the same maze, but with a yellow path connecting the entrance to the exit. The mean time to run is less than **one second** for small mazes and it can take up to **two seconds** for larger mazes. This program won't work for mazes bigger than 150x150, due to recurrency error.

## Built With

* [Python](https://www.python.org/) - Programming Language used.
* [Algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm) - Where I found Algorithms to generate mazes

## Authors

* **Matheus Assis** - [GitHub](https://github.com/MatheusMAssis)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
