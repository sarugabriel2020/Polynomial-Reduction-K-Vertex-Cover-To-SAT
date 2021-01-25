# Polynomial Reduction K-Vertex-Cover To SAT

## Objective 

The objective of the project is to identify a k-Vertex-Cover ≤P SAT reduction and implement it in Python language.

## Motivation to use this type of reduction
 
 • Such type of reductions are very useful in solving problems that have not been studied long enough or in which an optimal algorithm has not yet been found.
 
 • For example, if we have an X problem in NP, knowing that the SAT problem has been studied in detail and there are many libraries implementing SAT − Solvers, we can reduce our X problem to SAT, and then solve the resulting SAT problem using a SAT − Solver .
  
 • Thus we will get a result for the SAT problem, which will also be the result for the X problem (k-Vertex-Cover).

## About the  k-Vertex-Cover Problem

- A cover of an undirected graph is a subset of nodes in the graph such that, for any edge of the graph, at least one of its ends is in the subset.

- In other words, it is a selection of nodes that covers all the edges of the graph.

- ***The k-Vertex-Cover problem*** asks whether, given a non-oriented graph G and a natural number k, there is a coverage of size k in the graph G.

## About the SAT Problem

 ***SAT asks*** if a Boolean formula in normal conjunctive form is satisfactory (if there is an interpretation that satisfies the formula). 
 
 In other words, it asks if there is a choice of values (True / False) for the variables of a Boolean formula so that the formula is evaluated to True (to be true).
 
## INPUT Codification

- The program will receive as input an instance of the k-Vertex-Cover problem (an undirected graph G and a natural number k) and will have to return an instance of the SAT Problem (a Boolean formula in CNF), with the property that G contains a coverage of size k if and only if the formula is satisfiable.

***Input will be received as follows:***

· On the first line there is a single natural number K, which represents the size of the coverage sought in the graph G

· On the second line there is a single natural number N,which represents the number of nodes in the graph G (the nodes will be represented by the natural numbers from 1 to N)

· On the third line there is a single natural number M, which represents the number of edges in the graph G

· On the following M lines there are 2 natural numbers with space between them, which represent the nodes that form an edge in the graph G.

## Example of Input:

2
5
7
4 2
4 1
2 3
4 5
2 1
3 4
3 5

For this example:
  K = 2, N = 5, M = 7, G = (V, E),
  V = {1, 2, 3, 4, 5}, E = {(4, 2), (4, 1), (2, 3), (4, 5), (2, 1), (3, 4), (3, 5)}.

## Mention  

The program input is read from stdin and is guaranteed to always be valid.

## OUTPUT Codification

**The output** will have to be a Boolean formula in normal Conjunctive Normal Form (CNF), represented by a string, in which:

· **Variables** will be encoded as consecutive natural numbers, starting with 1 (for example, if you have 5 variables, they will be called 1, 2, 3, 4, 5);
· **Negation** will be encoded using the ‘~’ character;
· **The disjunction** will be coded using the character ‘V’ (capital letter V);
· **The conjunction** will be encoded using the character ‘^’;
· **The clauses** will be enclosed in parentheses ();
