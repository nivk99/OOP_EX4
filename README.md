# OOP_Ex4

![](https://camo.githubusercontent.com/b803cfcca0b874c6116fab9bbc05878b4ab7096770ea51b1a30a7bbc8e2de3f5/68747470733a2f2f7777772e617269656c2e61632e696c2f77702f736974652f77702d636f6e74656e742f75706c6f6164732f73697465732f332f323031382f30372f417269656c5f555f6c6f676f322e6a7067)

## ❓Weighted and Directed graph❓

A weighted directed graph is represented as a list of (vertex-edgelist) pairs, where the pairs are in standard order , the edgelist is a list of (neighbor-weight) pair also in standard order, every weight is a nonnegative integer, and every neighbor appears as a vertex even if it has no neighbors itself." A common operation on weighted (directed) graphs is the shortest-path computation; the determination of the path(s) from two nodes A and B such that the sum of the weights of the vertices on the path is minimal

## ❓What is a graph❓
Graph is a structure amounting to a set of objects in which some pairs of the objects are in some sense "related". The objects correspond to mathematical abstractions called vertices (also called nodes or points) and each of the related pairs of vertices is called an edge (also called link or line). Typically, a graph is depicted in diagrammatic form as a set of dots or circles for the vertices, joined by lines or curves for the edges. The edges may be directed or undirected

## 💡Digraphs💡
A directed graph (or digraph) is a set of vertices and a collection of directed edges that each connects an ordered pair of vertices. We say that a directed edge points from the first vertex in the pair and points to the second vertex in the pair.

The outdegree of a vertex is the number of edges pointing from it.

The indegree of a vertex is the number of edges pointing to it.

![](https://user-images.githubusercontent.com/6517308/71645678-802cd500-2ca1-11ea-96fb-11a71fd95191.jpg)

## 🔎Applications🔎
Graphs are directly applicable to real-world scenarios. For example, we could use graphs to model a transportation network where nodes would represent facilities that send or receive products and edges would represent roads or paths that connect them (see below).
![](https://camo.githubusercontent.com/ec0724a977b3aa31374644f12f6b70e99c8a7fd4ce99e7429a41c652d1ad82be/68747470733a2f2f7777772e66726565636f646563616d702e6f72672f6e6577732f636f6e74656e742f696d616765732f323032302f30362f696d6167652d3132312e706e67)


![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/640px-International_Pok%C3%A9mon_logo.svg.png)
![](https://www.animatedimages.org/data/media/1446/animated-pokemon-image-0076.gif)
## 💡The Pokemon game💡
 “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible. The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk)  the proper edge to “grab” the pokemon .
Your goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max)
The game is being played on a “server” 
The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, e.g.,  <java -jar Ex4_Server_v0.0.jar 0>  (where the “0” parameter is a case between [0-15]).
After the server is running a client can connect to it (play with it) 
In this assignment, we are mainly interested in maximizing the overall score - which is denoted as “grade” - the sum of all the pokemon weight as caught by all the “Agents”.


![](https://www.animatedimages.org/data/media/1446/animated-pokemon-image-0007.gif)
![](https://www.animatedimages.org/data/media/1446/animated-pokemon-image-0089.gif)
![](https://www.animatedimages.org/data/media/1446/animated-pokemon-image-0016.gif)



## 💡My algorithm💡:
    Algorithm: Given a list of Pokemon and agents the algorithm finds for each Pokemon the best agent for it by a number of actions:
    1. Check the location of the Pokemon
    2. Check the location and agent according to the Pokemon.
    3. Check if the agent is close to the Pokemon - if so then the agent will take the Pokemon.
    4. Checks if one of the agents is available and does nothing.
    5. Check the shortest distance between agents and Pokemon - The shortest distance between agent and Pokemon will be best.
    6. Once an algorithm finds the best agent for Pokemon it adds it to the list of Pokemon that is in each agent.
    7. Finally it is sent to the tsp method which finds the agent the best way to switch between all the Pokemon.
    In addition:
    A. Initially a function that sorts the list of Pokemon by the highest value to the lowest
    B. A function that initially calculates where to place the agent according to the center of all the Pokémon.
    c. A function that balances the state of the moves

## Explanation of the project

the OOP_Ex4 wiki! [For more explanation for each Class click here](https://github.com/nivk99/OOP_Ex4/wiki)

## 💡Reported results💡



## ❓how to run❓
1. [Run the server](https://github.com/nivk99/OOP_Ex4/blob/main/Ex4_Server_v0.0.jar):
 The server is a simple .jar file that can be run on any java machine (JDK 11 or above) in a command line, 
 
 e.g.,  <java -jar Ex4_Server_v0.0.jar 0> 

 (where the “0” parameter is a case between [0-15]).


2. [Activate the customer](https://github.com/nivk99/OOP_Ex4/blob/main/src/Ex4.py):
 Open the command prompt and run the Ex4 file.

Example for running the python program: python Ex4.py


![](https://github.com/nivk99/OOP_Ex4/blob/main/images/AA.png)



## 🔗Links🔗:
[https://www.youtube.com/watch?v=qR49hsdfzHA](https://www.youtube.com/watch?v=qR49hsdfzHA)

[What is Pokémon?](https://www.youtube.com/watch?v=eIJLjYf6B7M)

[The History of Pokemon | A Brief History](https://www.youtube.com/watch?v=Offw-N3PkoA)

[Graph Data Structure 4. Dijkstra’s Shortest Path Algorithm](https://www.youtube.com/watch?v=pVfj6mxhdMw)


## ✨Diagram class✨
![https://github.com/nivk99/OOP_Ex4/blob/main/images/algo_pokemon.png]

## ©️license & copyright©️:

© Kotek Niv 📧 <niv.kotek@msmail.ariel.ac.il >

© Shevach Aviv 📧 <aviv.shevach@msmail.ariel.ac.il >


![](https://images1.calcalist.co.il/PicServer3/2016/07/11/620912/1-lm.jpg)
