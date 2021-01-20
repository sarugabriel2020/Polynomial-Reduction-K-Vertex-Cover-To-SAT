# Polynomial-Reduction-K-Vertex-Cover-To-SAT

In this project the objective was to identify a a polynomial reduction k-Vertex-Cover ≤P SAT and its implementation in the Python language.

--- IMPORTANCE ---

• Such reductions are very useful in solving problems that have not been studied long enough or in which an optimal algorithm has not yet been found.
• For example, if we have an X problem in NP, knowing that the SAT problem has been studied in detail and there are many libraries that implement SAT − Solvers, we can reduce our X problem to SAT, and then solve the resulting SAT problem using a SAT − Solver .
• Thus we will get a result for the SAT problem, which will also be the result for the X problem (k-Vertex-Cover).

------------------------------------------------
The program will receive as input an instance of the k-Vertex-Cover problem (an undirected graph G and a natural number k) and will have to return an instance of the SAT problem (a Boolean formula in CNF), with the property that G contains a coverage of size k if and only if the formula is satisfiable.

Input will be received as follows:

· On the first line there is a single natural number K, which represents the size of the coverage sought in the graph G

· On the second line there is a single natural number N, which represents the number of nodes in the graph G (the nodes will be represented by the natural numbers from 1 to N)

· On the third line there is a single natural number M, which represents the number of edges in the graph G

· On the following M lines there are 2 natural numbers with space between them, which represent the nodes that form an edge in the graph G.

Example of input:
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
  V = {1, 2, 3, 4, 5}, E = {(4, 2), (4, 1), (2, 3), (4, 5), (2, 1), (3, 4),
(3, 5)}.

The program input is read from stdin and is guaranteed to always be valid.
Output

The output will have to be a Boolean formula in normal conjunctive form, represented by a string.
