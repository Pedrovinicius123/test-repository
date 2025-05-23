# P vs NP research experiment

## Epilogue

An idea I've got

I'm higly suspecting that there is no algorithm that solves a 3-SAT (and forward) problem efficiently, most of the problems have a high time complexity in worst case.
But i have to prove that for **all** problems we have are contained in the worst case. There's a graph that determine it.

![P_neq_NP](https://github.com/user-attachments/assets/9e74f498-3ca5-4e84-be53-51d53f77966f)

 According to [this source](https://www-sciencedirect-com.translate.goog/topics/computer-science/combinatorial-problem): "Combinatorial problems arise in many areas of computer science and other disciplines in which computational methods are applied, such as artificial intelligence, operations research, bioinformatics and electronic commerce. Prominent examples are tasks such as finding shortest or cheapest round trips in graphs, finding models of propositional formulae or determining the 3D-structure of proteins. Other well-known combinatorial problems are encountered in planning, scheduling, time-tabling, resource allocation, code design, hardware design and genome sequencing. These problems typically involve finding groupings, orderings or assignments of a discrete, finite set of objects that satisfy certain conditions or constraints."

 That may be disapointing, but I think that is the right answer: $P \neq NP$. More studies must be done to ensure that. Although, it is very sad for me that this is maybe true...
 
To prove that, we must ensure that there is non-combinatory or heuristic algorithm that can solve, in optimal polinomial time, a SAT problem. This make the graph even more important, because it shows the function $\theta(i) = \frac{\theta!}{i! \cdot (\theta - i)!}$, that is in function of $i$ related to $\theta$ (nothing more, nothing less than $C_{\theta, i}$ in function of $i$, where $i \leq \theta$). In worst case, it leads to huge number of combinations, and for check each of then, we have a high computational complexity. So let's get into it.

## The proof (?) - 1

The algorithm I developed along this research may not be the best to solve an SAT problem, but it sufficient to ensure that there is no combinatory algorithm to solve the problem related to SAT. There is the proof: given an algorithm that takes the intersection of the clauses and gather the non-empty intersections, distribushing then through a series of combinations formed by the own intersections, we can notice something different: in worst cases, the problem suffers a explosive grow on this computational cost. Even if we take every combination rapidly, it would take several time to solve, given the astounding number of iterations necessary to solve it (in worst case). The problem could be described as: "Is there any way to find the correct combination without needing to iterate between all of then?" **And that is exactly the question, in a informal way, that the P vs NP problem asks**. The intuitive answer would be "no", but, in mathematics not everything is intuitive.

If a non-deterministic computer toke a solution from the processed n-SAT problem, by the algorithm, it would, for sure, find the solution in optimal time, but there is not physical non-deterministic way from a process to another, therefore, a parallel processing machine would be successful on this task, but not efficient on real life hardware [more details on this source](https://www.quora.com/What-is-the-point-of-a-non-deterministic-Turing-machine-if-it-cant-be-implemented-Or-is-there-a-way-to-implement-it). Otherwise in **deterministic** computing, there is no way to check all the possibilities by once, such that, even if we implemented an efficient choice heuristic, we still have a factorial complexity in worst cases.

The best aproach we have today is DPLL (Davis-Putnam-Logemann-Loveland), wich is also an combinatory algorithm that solves the problem. Although in a exponential complexity $O(2^n)$, for 2-SAT (wich is not NP-Complete), DPLL have a complexity of $O(n^2)$. I've tried an algorithm that highlights some of the variables in a 3-SAT problem, turning it polynomial, but it don't work since, in a semantic way, the algorithm remains exponential.

## The proof (?) - 2

At 20:54 pm, 05/16/2025, I think I did a massive discovery: an algorithm better than DPLL. I basically got an set $\eta$ of literals and I apply that, within the combinations, the sample would be positive, whereas the restant literals would be negative.

At 21:43 pm I realized that such thing isn't a proof of P = NP, but a counter proof to the conjecture. Here's wy:

Let be a $\eta$ set of literals, from wich I would take a combination of literals $C_{\eta, k}$, negating the restant variables. If, in the result provided by the chunk ($k$) we defined, there is no correct atribuition to the SAT problem, that doesn't mean the problem is whether satisfiable or not. It would imply that, in worst cases, we may have great search costs, leading to an exponential rate.

More studies are required to determine whether this proof is valid or not.

[...](https://www.overleaf.com/read/btsskgtbbgdv#5fdc26)

# FINAL PROOF

There **maybe** is an algorithm that solves a SAT formula in polynomial time, the code is described in the `solver.py` file. Note that I use `pycosat` library when all remaining clauses are within the 2SAT instance ([repository here](https://github.com/conda/pycosat.git)), I do it because the DPLL is ***polynomial*** for 2SAT instances, reaching a complexity of $O(n^2)$ in worst cases. I've also tracked the number of recursive iterations done from 3 up to 30 variables, within 10 up to 100 clauses for the 3SAT instance. There is the graph describing the complexity of the algorithm

![Algorithm](https://github.com/user-attachments/assets/65ce299e-9074-4d51-b713-6291318f3949)

And also, the algorithm alone, for 3 up to 13 literals and 10 up to 300 clauses compared to quadratic and exponential complexities:

![Complexity](https://github.com/user-attachments/assets/22785f3c-e44e-4813-8993-5b4b8364c423)

This may refutate the ETH, which claims that there is no subexponential optimization that we can do in the exponential algorithm. That means, there is no $2^{o(n)}$. It may not solve the P vs NP conjecture, but it neglect a hypotesis much stronger that it. Maybe this is a support to P = NP? Maybe the number of clauses reflect on the final complexity? There is a lot of studies we can do on that algorithm.

