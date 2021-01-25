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


## About the Implementation 

➔ For the respective transformation we built N * K variables, where N is the number of nodes in the graph, and K is the size of the sought coverage, and in this way we can say that to each node in the graph we will associate K variables.
➔ The respective transformation is in O (n ^ 3) because we observe an iteration that is in another iteration.

The transformation has in itself 2 parts:

► **First part:**

• Between two variables in a given clause, more precisely from 1 to n; from n + 1 to 2n and so on to (k-1) n +1 to kn, and then we will form a clause.

►**The second part:**

• It is represented by the fact that for each edge of the graph, we will construct a clause with all the variables associated to all the nodes in the edge, concatenated by V, and the clauses connected by ^.

► **The implication in part ‘=>’** is demonstrated if k-vertex-cover is true, then we will know that there is a coverage of size k, so that the k nodes that were chosen to cover all the edges of the graph.

So then there will surely be an interpretation to satisfy all the clauses of the generated formula, and according to the transformation, at most one variable in each clause can be true for the first part of the formula to be satisfactory, then it follows that we will choose maximum k true variables , and those k variables correspond to the k nodes in the vertex because all edges are covered by the k chosen nodes, this implies that the second part of the formula is satisfactory, then in the end this implies that the SAT is true.

► **The implication in the ‘<=’ part** is demonstrated if the SAT is true, and this means that each clause is satisfied. So in all the clauses in the second part of the formula there must be at least one of the k variables that must be true from the first part of the form, for it to be satisfying, and the choice of k variables that cover all the edges The graph results from the fact that there is a coverage of size k which leads to the fact that k vertex cover is true.


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

· **Variables** will be encoded as consecutive natural numbers, starting with 1 (for example, if you have 5 variables, they will be called 1, 2, 3, 4, 5)

· **Negation** will be encoded using the ‘~’ character

· **The disjunction** will be coded using the character ‘V’ (capital letter V)

· **The conjunction** will be encoded using the character ‘^’

· **The clauses** will be enclosed in parentheses ()
